# atari pong from openai gym
* https://gym.openai.com/envs/Pong-v0/
* http://karpathy.github.io/2016/05/31/rl/

## env
* Pong-v0
* observation: Box(210, 160, 3)
* action: Discrete(6)
```
>>> env.action_space.n
6
>>> env.unwrapped.get_action_meanings()
['NOOP', 'FIRE', 'RIGHT', 'LEFT', 'RIGHTFIRE', 'LEFTFIRE']
```

## reward formulation:
* type 1: (n_episodes == n_rallies) (used here)
  * +1: ball is out in the opponent's area; a rally(==episode) ends
  * -1: ball is out in the own area; a rally(==episode) ends
  * 0: else
* type 2: (n_episodes == n_rounds == n_games, each round/game consists of, at least, 21 rallies)
  * +1: win a round
  * -1: loose a round
* type 3: (n_episodes == n_matches, each match consists of 3 rounds)
  * +1: win a game
  * -1: loose a game

## follow-up
### numpy
* https://github.com/llSourcell/Policy_Gradients_to_beat_Pong
* https://github.com/dhruvp/atari-pong
### tensorflow
* https://github.com/PacktPublishing/TensorFlow-1x-Deep-Learning-Cookbook/blob/master/Chapter09/policy_gradients_pong.py
  * https://github.com/tttor/TensorFlow-1x-Deep-Learning-Cookbook/blob/devel/ch09/05_policy_gradients_pong.py
* https://github.com/AbhishekAshokDubey/RL/tree/master/ping-pong

## support
* https://ai.stackexchange.com/questions/2449/what-are-different-actions-in-action-space-of-environment-of-pong-v0-game-from/3422#3422
  * Each action is repeatedly performed for a duration of k frames,
    where k is uniformly sampled from {2,3,4}
  * UP: 2 or 4 and DOWN: 3 or 5
* http://southerntasbadminton.com.au/SimplifiedRules.html
