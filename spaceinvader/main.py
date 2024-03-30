import pygame as pg
from pygame.locals import *
import helpers
import os
import sys

CWD = os.getcwd()
RESOURCE = os.path.join(CWD, "spaceinvader", "resource")
icon = os.path.join(RESOURCE, "spaceship32.png")

DARKGRAY = (120, 120, 120)


def get_display():
    screen = pg.display.set_mode((1000, 700))
    pg.display.set_caption("PATTHAR TOD GAME")
    return screen


def get_player(screen, player_coordinates):
    player_path = os.path.join(RESOURCE, "spaceship64.png")
    player = pg.image.load(player_path)
    # player_coordinates = (450, 550)
    screen.blit(player, player_coordinates)

    return player


if __name__ == "__main__":
    pg.init()

    screen = get_display()
    spaceship = pg.image.load(icon)
    pg.display.set_icon(spaceship)
    screen.fill((240, 240, 240))

    running = True
    x, y = 450, 550
    while running == True:
        # event = pg.event.poll()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            # running = False
            # Keydown means key pressed
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                # handling Y axis movement
                if event.key == K_DOWN:
                    print("Keydown")
                    if y <= screen.get_height() - 1:
                        y += 5
                        print(y)
                if event.key == K_UP:
                    if y >= 0:
                        y -= 0.5
                # keyup means key is released
            if event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    print("Keyup")

        get_player(screen=screen, player_coordinates=(x, y))
        pg.display.update()
