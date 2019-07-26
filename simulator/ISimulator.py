from abc import abstractmethod


class ISimulator(object):
    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod
    def step(self, a):
        raise NotImplementedError

    @abstractmethod
    def nActions(self):
        raise NotImplementedError

    # shape of the environment state [int for vector state; (tuple) for image]
    @abstractmethod
    def dState(self):
        raise NotImplementedError

    @abstractmethod
    def sampleAction(self):
        raise NotImplementedError

    @abstractmethod
    def prettifyState(self, rawState):
        raise NotImplementedError
