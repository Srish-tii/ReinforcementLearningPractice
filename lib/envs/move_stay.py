import numpy as np
import sys
from gym.envs.toy_text import discrete
import gym


MOVE = 0
STAY = 1

SA = 0
SB = 1


class MoveStayEnv(discrete.DiscreteEnv):
    metadata = {"render.modes": ["human", "ansi"]}
    name = "MoveStay"

    def __init__(self):
        self.shape = 2

        nS = 2
        nA = 2

        P = {}
        for s in range(nS):
            P[s] = {a: [] for a in range(nA)}
            P[s][MOVE] = [(1.0, 1 - s, 0, False)]
            P[s][STAY] = [(1.0, s, 1, False)]
        print(P)

        isd = np.zeros(nS)
        isd[SA] = 1.0

        super(MoveStayEnv, self).__init__(nS, nA, P, isd)

    def render(self, mode="human", close=False):
        self._render(mode, close)

    def _render(self, mode="human", close=False):
        if close:
            return

        outfile = StringIO() if mode == "ansi" else sys.stdout

        for s in range(self.nS):
            if self.s == s:
                output = " x "
            elif s == SA:
                output = " A "
            elif s == SB:
                output = " B "
            else:
                raise ValueError("Invalid state: {}".format(s))

            outfile.write(output)
        outfile.write("\n")