#! /usr/bin/env python

import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"  # hide pygame prompt message
import pygame
from gamepad import Gamepad
from pygame.locals import *
from shapes import draw_filled_polygon, draw_filled_rectangle


class CarpetGame:
    def __init__(self, fullscreen=True):
        pygame.init()

        self.dspl_ino = pygame.display.Info()
        self.size = (self.dspl_ino.current_w, self.dspl_ino.current_h)
        self.bkgrnd = 124, 124, 124

        print(f"New Game - {self.size}")
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)

        self.controller = None

        self.poly_sides= 6
        self.poly_rad= 50

    def add_gamepad(self, gamepad: Gamepad):
        print('add_gamepad')
        self.controller = gamepad
        self.controller.bind_a_button(self.increse_sides)
        self.controller.bind_y_button(self.decrese_sides)

        self.controller.bind_b_button(self.increse_rad)
        self.controller.bind_x_button(self.decrese_rad)

    def increse_sides(self, value):
        if value == 0:
            return
        print('increse_sides')
        self.poly_sides = self.poly_sides + 1
        
    def decrese_sides(self, value):
        if value == 0:
            return
        if self.poly_sides == 3:
            return
        print('decrese_sides')
        self.poly_sides = self.poly_sides - 1

    def increse_rad(self, value):
        if value == 0:
            return
        print('increse_rad')
        self.poly_rad = self.poly_rad + 10

    def decrese_rad(self, value):
        if value == 0:
            return
        if self.poly_rad == 10:
            return
        print('decrese_rad')
        self.poly_rad = self.poly_rad - 10

    def main(self, callback=None):
        self.game_running = True
        self.screen.fill(self.bkgrnd)

        while self.game_running:
            # Loop through all active events
            for event in pygame.event.get():
                # Close the program if the user presses the 'X'
                if event.type == pygame.QUIT:
                    self.game_running = False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.game_running = False

            if self.controller is not None:
                self.controller.process(False)

            self.loop()

            if callback is not None:
                callback()

            # Update our display
            pygame.display.update()

    def loop(self):
        # print("draw a rectaangle on surface and blit onto screen")

        surf = pygame.Surface(self.size)

        Mouse_x, Mouse_y = pygame.mouse.get_pos()

        poly_color = (255, 128, 0)
        floor_h = 100
        
        screen_size = list(self.size)
        screen_w = screen_size[0]
        screen_h = screen_size[1]

        # Drawing from centre
        #
        # Thus to draw floor:
        #   Left = 0 + (screen_w / 2)
        #   Top = screen_h - (floow_h / 2)
        draw_filled_rectangle(surf, int(screen_w/2), screen_h - int(floor_h/2), screen_w, floor_h, (255, 255, 0))
        # Draw Player
        draw_filled_rectangle(surf, Mouse_x, Mouse_y, 50, 70, (200, 10, 150))

        draw_filled_polygon(surf, Mouse_x, Mouse_y - 35, self.poly_sides, self.poly_rad, poly_color)

        self.screen.blit(surf, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    from pprint import pprint

    try:
        new_game = CarpetGame()
        new_game.main()
    except Exception as e:
        print("Error")
        pprint(e)

    print("done")
