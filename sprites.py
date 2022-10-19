import pygame as pg
from settings import *


class Particle:
    @staticmethod
    def updateConnection(a, b):
        try:
            a.connections.remove(b)
            b.connections.remove(a)
        except ValueError:
            a.connections.append(b)
            b.connections.append(a)

    def __init__(self, game, pos, value, arb, arbColor):
        self.game = game
        self.screen = self.game.screen

        self.pos = pos
        self.radius = P_RADIUS

        self.value = value
        self.dValue = 0
        self.connections = []

        self.arb = arb
        self.arbColor = arbColor

    def update(self):
        self.arb(self)

    def lateUpdate(self):
        self.value += self.dValue * self.game.dt

    def draw(self):
        con_radius = getParticleConnectionRadius(self.dValue)
        pg.draw.circle(self.screen, self.arbColor, self.pos, con_radius, P_CON_WIDTH)
        for particle in self.connections:
            midpoint = (self.pos + particle.pos) / 2
            pg.draw.line(self.screen, self.arbColor, self.pos, midpoint, P_CON_WIDTH)

    def lateDraw(self):
        pg.draw.circle(self.screen, getParticleColor(self.value), self.pos, self.radius)
