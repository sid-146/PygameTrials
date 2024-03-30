import pygame
from pygame.locals import *
import random

NUM_STARS = 400
FORWARD = 1
BACKWARD = 0
LIGHTGRAY = 180, 180, 180
DARKGRAY = 120, 120, 120
GOLDEN = (255, 192, 0)
SCREEN_SIZE = (1200, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# pygame.display.init()


def initial_stars(window):
    stars = []

    for _ in range(0, NUM_STARS):
        # co ordinate of single star
        x = random.randint(0, window.get_width() - 1)
        y = random.randint(0, window.get_height() - 1)
        star = [x, y]
        stars.append(star)

    return stars


def moveStars(window, stars, start, end, direction):

    for i in range(start, end):
        if direction == BACKWARD:
            if stars[i][0] != 1:
                stars[i][0] = stars[i][0] - 1
            else:
                stars[i][1] = random.randint(0, window.get_width() - 1)
                stars[i][0] = random.randint(0, window.get_height() - 1)
        elif direction == FORWARD:
            if stars[i][0] != window.get_width() - 1:
                stars[i][0] = stars[i][0] + 1
            else:
                stars[i][1] = random.randint(0, window.get_height() - 1)
                stars[i][0] = 1

    return stars


def setup():
    window = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
    # window = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Star Field")
    window.fill(BLACK)
    return window


def main():
    pygame.init()
    window = setup()

    # Controller variable
    direction = FORWARD
    speed = 6
    increment = 2

    stars = initial_stars(window)

    # Place first stars
    for i in range(0, 100):
        window.set_at(stars[i], WHITE)

    running = True
    while running:

        # Inputs event handler
        event = pygame.event.poll()
        if event.type == QUIT:
            break
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                break
            elif event.key == K_UP:
                if speed >= 2:
                    speed = speed - 1
            elif event.key == K_DOWN:
                if speed <= 16:
                    speed = speed + 1
            elif event.key == K_LEFT:
                direction = BACKWARD
            elif event.key == K_RIGHT:
                direction = FORWARD

        # Used to create far distance motion
        increment += 1
        #! If we do not remove stars before plotting them they will create tails
        # Erase First Star fields
        for ii in range(0, 100):
            window.set_at(stars[ii], BLACK)

        # Check first star collision to end of window
        stars = moveStars(window, stars, 0, 100, direction)

        # Second Star field
        if increment % 2 == 0:
            # Erase second star field
            for i in range(101, 200):
                window.set_at(stars[i], BLACK)

            # check second star field collision with end of window
            stars = moveStars(window, stars, 101, 200, direction)

            # Placing Lightgrey stars
            for i in range(101, 200):
                window.set_at(stars[i], LIGHTGRAY)

            #  Third star field
            if increment % 5 == 0:
                # Erase third star field
                for i in range(201, NUM_STARS):
                    window.set_at(stars[i], BLACK)

                stars = moveStars(window, stars, 201, NUM_STARS, direction)

                #  Place Darkgrey Stars
                for i in range(201, NUM_STARS):
                    window.set_at(stars[i], DARKGRAY)

            if increment % 10 == 0:
                #  Erase golden stars
                for i in range(100, 201):
                    window.set_at(stars[i], BLACK)

                stars = moveStars(window, stars, 100, 201, direction)

                #  Draw golden stars
                for i in range(100, 201):
                    window.set_at(stars[i], GOLDEN)

        for i in range(0, 10):
            window.set_at(stars[i], WHITE)

        pygame.time.delay(speed)

        if increment == 500:
            increment = 2

        pygame.display.update()


if __name__ == "__main__":
    main()
