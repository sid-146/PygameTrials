import pygame as pg
import time
import sys
import utils.colors as colors
from utils.logger import console
from utils.physicsEngine import PhysicsEngine


class Simulate:
    engine = PhysicsEngine()

    def __init__(self):
        self.run: bool = None
        self.space: pg.display = None
        self.bodies = None  # update dtype for this

    def initialiseEnv(self, bodies: list):
        # Number elements on the screen
        self.bodies = bodies
        spaceSize = (1000, 800)
        self.run = True

        pg.init()
        self.space = pg.display.set_mode(spaceSize)

        # Define bodies
        self.engine.defineBodies(bodies=bodies)

    def explore(self):
        # Game loop
        while self.run:
            # test += 1
            # console.info(rf"\t\t\{test}")
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            
            self.space.fill(colors.black)
            
            # Calculate force
            netForces = self.engine.CalcForce()
            for i,body in enumerate(self.bodies):
                body.force = netForces[i]

            # Add body
            for body in self.bodies:
                body.draw(self.space)

                # print(body.velocity)
                # print(body.position)

            # move body
            for body in self.bodies:
                body.move()

            time.sleep(0.0005)
            pg.display.update()
