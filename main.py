from constants import *
import pygame as pg
import time
import sys


# The main Program class
class Program:
    # Runs on initialization
    def __init__(self):
        # Pygame initialization
        pg.init()

        # Sets windowsize and canvas to display everything on.
        self.window = pg.display.set_mode(WINDOW_SIZE)
        self.canvas = pg.Surface(WINDOW_SIZE)

        # Sets up clock and time
        self.clock = pg.time.Clock()
        self.prevTime = time.time()

        # Starts up the game loop.
        self.run()

    # Does everything related to time and returns the current time and deltatime
    def tickClock(self):
        # Ticks self.clock
        self.clock.tick(FPS)
        pg.display.set_caption(f"{round(self.clock.get_fps())}")
        # Sets up current time, and deltatime
        curTime = time.time()
        deltatime = curTime - self.prevTime
        # Set prevTime to curTime
        self.prevTime = curTime

        # Returns curTime and deltatime
        return curTime, deltatime

    # Tracks events and handles what to do when said events occur.
    @staticmethod
    def eventHandler(player):
        for event in pg.event.get():
            # Allows the game to be able to close
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # What happens if a key is pressed.
            if event.type == pg.KEYDOWN:
                player.keyDown(event.key)
            # What happens if a key is released.
            if event.type == pg.KEYUP:
                player.keyUp(event.key)

    # The main game loop everything happens on.
    def run(self):
        from player import Player
        # Declares class instances
        player = Player(400, 300, 32, 32)  # x, y, width, height

        # Runs every frame.
        while True:
            # Ticks the clock while also setting the values of
            curTime, deltatime = self.tickClock()
            # Calls eventHandler
            self.eventHandler(player)

            # Gets the position of the mouse.
            mousePos = pg.mouse.get_pos()

            # Updates class instances or runs functions
            player.update(mousePos, deltatime)

            # Refreshes the screen
            self.canvas.fill(COLOR["black"])

            # Draws the player
            pg.draw.ellipse(self.canvas, COLOR["blue"], player)
            # Draws a line between the player and the mouse cursor.
            pg.draw.line(self.canvas, COLOR["blue"], player.rect.center, mousePos)

            # Blits canvas onto the window and updates the screen to reflect changes
            self.window.blit(self.canvas, (0, 0))
            pg.display.flip()


# This is the entry point! Run this first!
if __name__ == '__main__':
    program = Program()

