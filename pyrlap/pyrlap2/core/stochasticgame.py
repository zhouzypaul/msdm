from typing import Iterable, Mapping, Hashable
from abc import ABC, abstractmethod

from pyrlap.pyrlap2.core.distributions import Distribution

class StochasticGame(ABC):
    """
    SGs are defined by:
    - variables, which determine states and joint actions
    - action distributions, which bias actions at each state
    - initial state distributions
    - next state distributions
    """

    def __init__(self, agentList):
        self._agentList = agentList
        
    @property
    def agents(self):
    	return self._agentList

    @abstractmethod
    def getInitialStateDist(self) -> Distribution:
        pass

    @abstractmethod
    def getJointActionDist(self, s: "state") -> Distribution:
        pass

    @abstractmethod
    def getNextStateDist(self, s: "state", ja: "jointaction") -> Distribution:
        pass

    @abstractmethod
    def getJointRewards(self, 
            s: "state", 
            ja: "jointaction",
            ns: "nextstate",
        ) -> Mapping[Hashable, float]:
        pass

    def __and__(self, other: "StochasticGame"):
        """
        This is not strictly an abstract base class method, but it
        should be overwritten by derived abstract base classes
        so that AND-composed POSGs can inherit from them.
        """
        return ANDStochasticGame(self, other)


class ANDStochasticGame(StochasticGame):
    """Simplest AND SG - only assumes function calls can be combined"""

    def __init__(self, sg1, sg2):
        raise NotImplementedError
    #     self.mdp1 = mdp1
    #     self.mdp2 = mdp2
    #     variables = sorted(set(mdp1.variables + mdp2.variables))
    #     MarkovDecisionProcess.__init__(self, variables)

    # def getNextStateDist(self, state, action) -> Distribution:
    #     d1 = self.mdp1.getNextStateDist(state, action)
    #     d2 = self.mdp2.getNextStateDist(state, action)
    #     return d1 & d2

    # def getReward(self, state, action, nextstate) -> float:
    #     r1 = self.mdp1.getReward(state, action, nextstate)
    #     r2 = self.mdp2.getReward(state, action, nextstate)
    #     return r1 + r2

    # def getActionDist(self, state) -> Distribution:
    #     a1 = self.mdp1.getActionDist(state)
    #     a2 = self.mdp2.getActionDist(state)
    #     return a1 & a2

    # def getInitialStateDist(self) -> Distribution:
    #     s1 = self.mdp1.getInitialStateDist()
    #     s2 = self.mdp2.getInitialStateDist()
    #     return s1 & s2
