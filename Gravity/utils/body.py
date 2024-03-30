import pygame as pg
import numpy as np

# Screen refresh is set as below that is why it is multiplier for velocity


class Body:
    TIME_DELAY = 0.0005

    def __init__(self, positionVector, mass, color, radius: int = 15) -> None:
        self.velocity: np.array = np.array([[0, 0, 0]])
        self.force: np.array = np.array([[0, 0, 0]])
        self.mass: int = mass
        self.radius: int = radius
        self.position = positionVector
        self.thickness = self.radius * 2
        self.color = color

    def draw(self, space: pg.Surface):
        pg.draw.circle(
            space,
            self.color,
            (self.position[0][0], self.position[0][1]),
            self.radius,
            self.thickness,
        )

    def updateVelocity(self, velocity: np.array):
        self.velocity += velocity

    def move(self):
        # u = v + at
        self.velocity = self.velocity + (self.force / self.mass) * self.TIME_DELAY
        # d = s*t
        self.position = self.position + self.velocity * self.TIME_DELAY

    def add_force(self, forces):
        self.force = self.force + forces
