#! /usr/bin/env python

from shapes import draw_filled_polygon
import pygame
from typing import Tuple, Callable


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        pass


class RoundRectangle:
    def __init__(self, width: int, height: int, border_radius: int = 10):
        self.width = width
        self.height = height
        pass


class Square:
    def __init__(self, width: int, rect: Callable[int, int]):

        self.rect = rect(width, width)
        self.width = width
        pass


width = 10
x = Square(width, Rectangle.__init__)
y = Square(width, RoundRectangle.__init__)


class Platform:
    def __init__(self):
        self.height = 100
        self.color = (255, 255, 255)
        pass

    def floor(self):
        # draw_filled_polygon()
        print(f"floor {self.height}")
        pass

    def player(self, x: int, y: int):
        pass


if __name__ == "__main__":
    # floor()
    game = Platform()
    game.floor()

    # print(Platform.height)
