# this file is used to define rules of arbitrization

from enum import Enum
from random import random


def arbConservation(self):  # conservation using acceleration. produces SHM
    if len(self.connections) == 0:  # this is an arbitrary condition
        self.dValue = 0
    for particle in self.connections:
        self.dValue += (particle.value - self.value) * self.game.dt * 10


def arbFlow(self):
    self.dValue = 0
    for particle in self.connections:
        self.dValue += (particle.value - self.value) * self.game.dt * 50


def arbRandom(self):  # random entropy that propagates arbitrization
    self.value = (random() - 0.5) * 100


class Arb(Enum):  # structure: function, then color
    CONSERVATION = arbConservation
    FLOW = arbFlow
    RANDOM = arbRandom
    DEFAULT = CONSERVATION


ArbColors = {
    Arb.CONSERVATION: (23, 64, 195),
    Arb.FLOW: (183, 212, 3),
    Arb.RANDOM: (0, 0, 0),
}
