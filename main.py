import pygame as pg
import sys
import random
from settings import *
from sprites import *
from arb import Arb, ArbColors


def stopAll():
    pg.quit()
    sys.exit()


class Game:
    def __init__(self):
        # vars setup
        self.particles = []
        self.selectedParticleIndex = None

        # pygame setup
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)  # not sure if necessary

        self.playing = True
        self.dt = 0

    def new(self):
        for x in range(P_COUNT_X):
            for y in range(P_COUNT_Y):
                pos = pg.math.Vector2(x * P_RECT_SIZE.x, y * P_RECT_SIZE.y) + P_HALF_RECT_SIZE
                val = P_INIT_VALUE_LOW  # random.randint(P_INIT_VALUE_LOW, P_INIT_VALUE_HIGH)
                self.particles.append(Particle(self, pos, val, Arb.DEFAULT, ArbColors[Arb.DEFAULT]))

    def run(self):
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.lateUpdate()

    def resetParticles(self):
        for particle in self.particles:
            particle.arb = Arb.DEFAULT
            particle.arbColor = ArbColors[Arb.DEFAULT]
            particle.connections.clear()
            particle.dValue = 0
            particle.value = 0

    def update(self):
        self.screen.fill(BG_COLOR)

        for particle in self.particles:
            particle.update()
            particle.draw()

    def lateUpdate(self):
        for particle in self.particles:
            particle.lateUpdate()
            particle.lateDraw()

        if self.selectedParticleIndex:
            pg.draw.circle(self.screen, P_SELECTED_COLOR, self.particles[self.selectedParticleIndex].pos, P_SELECTED_RADIUS)

        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                stopAll()
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                idx = getParticleIndex(x, y)
                if not self.selectedParticleIndex:
                    self.selectedParticleIndex = idx
                elif idx == self.selectedParticleIndex:
                    self.selectedParticleIndex = None
                else:
                    Particle.updateConnection(self.particles[self.selectedParticleIndex], self.particles[idx])
                    self.selectedParticleIndex = None
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    stopAll()
                elif event.key == pg.K_BACKSPACE:
                    self.resetParticles()

                if self.selectedParticleIndex:
                    if event.key == pg.K_v:
                        (self.particles[self.selectedParticleIndex]).value = (random.random() - 0.5) * 2 * P_ABS_HIGH_VALUE
                        self.selectedParticleIndex = None
                    elif event.key == pg.K_0:
                        particle = self.particles[self.selectedParticleIndex]
                        particle.arb = Arb.CONSERVATION
                        particle.arbColor = ArbColors[Arb.CONSERVATION]
                        self.selectedParticleIndex = None
                    elif event.key == pg.K_1:
                        particle = self.particles[self.selectedParticleIndex]
                        particle.arb = Arb.FLOW
                        particle.arbColor = ArbColors[Arb.FLOW]
                        self.selectedParticleIndex = None
                    elif event.key == pg.K_2:
                        particle = self.particles[self.selectedParticleIndex]
                        particle.arb = Arb.RANDOM
                        particle.arbColor = ArbColors[Arb.RANDOM]
                        self.selectedParticleIndex = None


g = Game()
g.new()
g.run()
