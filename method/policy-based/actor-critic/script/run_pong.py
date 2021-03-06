#!/usr/bin/env python3
import sys
import time

import numpy as np

from agent import ActorCriticAgent
from environment import AtariPong

def main():
    if len(sys.argv) != 5:
        print('USAGE:')
        print('python3 pong.py <train/test> <n_episodes> <log_dir> <render/norender>')
        return

    mode = sys.argv[1]; assert mode in ['train', 'test']
    train = (True if mode=='train' else False)
    n_episodes = int(sys.argv[2])
    log_dir = sys.argv[3]
    render = (True if sys.argv[4]=='render' else False)

    run(train, n_episodes, log_dir, render)

def run(train, n_episodes, log_dir, render=False):
    ## init
    env = AtariPong(gamma=0.999, seed=1)

    obs = env.initial_observation()
    agent = ActorCriticAgent( env.n_actions(), initial_observation=obs )

    step_idx = 0 # an episode consists of n>=1 steps
    episode_idx = 0 # an "episode" refers to a "rally" in Pong
    game_idx = 0 # a game consists of n>=1 episodes
    discounted_returns = [0]*n_episodes # from the start state of every episode

    ## bookkeeper per game because training is done at then of a game
    if train == True:
        training_data = {'obss': [], 'rewards': [], 'labels': []}

    ## main loop
    while (episode_idx < n_episodes):
        ## msg
        print('episode_idx= '+str(episode_idx)+ \
              ' @step_idx= '+str(step_idx)+ \
              ' @game_idx= '+str(game_idx))
        if render:
            env.render()
            time.sleep(1/60.0)

        ## step!
        action, label = agent.act(obs)
        obs, reward, info = env.step(action)

        discounted_returns[episode_idx] += ((env.gamma**step_idx) * reward)

        ## collect data for training
        if train == True:
            training_data['obss'].append(obs)
            training_data['rewards'].append(reward)
            training_data['labels'].append(label)

        ## close an episode(== a rally)
        if info['end_of_episode']:
            print('episode_idx= '+str(episode_idx)+ \
                  ': ended with G= '+str('%.3f'%discounted_returns[episode_idx]))

            episode_idx += 1
            step_idx = 0

            if info['end_of_game'] or (episode_idx == n_episodes):
                ## train
                if train == True:
                    print('training...')

                    ## finalize training data
                    for k in training_data.keys():
                        training_data[k] = np.vstack(training_data[k])
                    training_data['returns'] = env.compute_returns(training_data['rewards'])

                    ## train!
                    agent.train(training_data)

                    ## reset training data
                    training_data = {'obss': [], 'rewards': [], 'labels': []}

                ## set for the next game
                obs = env.initial_observation()
                game_idx += 1
        else:
            step_idx += 1

    ## closure
    env.close()

    if train == True:
        print('discounted_returns for the last 10 training episodes:')
        print(str(discounted_returns[-10:]))

if __name__ == '__main__':
    main()
