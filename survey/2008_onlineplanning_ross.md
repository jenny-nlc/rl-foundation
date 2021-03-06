# Online planning algorithms for POMDPs
* S. Ross, J. Pineau, S. Paquet and B. Chaib-draa
* Journal of Artificial Intelligence Research 2008
* http://www.jair.org/papers/paper2567.html

## abs
* focus on online approaches that 
  alleviate the computational complexity by computing good **local policies at each decision step during the execution**
* to survey the various existing online POMDP methods
* state-of-the-art online heuristic search methods can handle large POMDP domains efficient

## misc
They pointed out that heuristic search approaches, i.e. AEMS2 and HSVI-BFS, outperforms others.
They also suggested combining offline and online approaches.
Most approches utilizes belief trees, some that do not include RTDP-BEL~\cite{Geffner1998}, SOVI~\cite{Shani2005}.
Approaches that use belief trees differ mostly in $ChooseNextNodeToExpend()$ and $Expand()$.
The latter constructs the next reachable belief under the selected leaf for some pre-determined expansion depth and
evaluates the approximate value function for all newly created nodes.

Based on those two core functions, we can classify online POMDP planning into 3 categories as follows.
* branch-and-bound pruning
  This requires upper and lower bounds on the value function.
  If an action~$a_1$ in $b$ has an upper bound that is lower than the lower bound of another action~$a_2$.
  Then, $a_1$ is suboptimal in $b$.
  Hence, branch to $a_1$ can be pruned.
  Branch-and-bound pruning lowers the complexity related to the action space size.
  This includes RTBSS~\cite{Paquet2005}.
* monte carlo sampling
  The core concept here is to sample (via a generative model) a subset of observations at each expansion and
  to considers only beliefs reached by these sampled observations.
  This reduces the branching factor and allows for deeper search.
  Monte Carlo sampling has been used to lower the complexity related to the observation space size, and
  could also potentially be used to reduce the complexity related to the action space size (by sampling a subset of actions).
  This includes \cite{McAllester1999,Bertsekas1999,HyeongSooChang,Thrun2000}.
* heuristic search
  This uses heuristics to select the best fringe belief node to expand.
  Search heuristics lower the complexity related to actions and observations by
  orienting the search towards the most relevant actions and observations
  This includes \cite{Chaib-draa2007}.
