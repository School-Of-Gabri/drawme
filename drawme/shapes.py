#! /usr/bin/env python

import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"  # hide pygame prompt message
import pygame
import math


class InvalidPolygonException(Exception):
    pass


def draw_filled_rectangle(surf: pygame.Surface, x: int, y: int, width: int, height: int, color: tuple):
    points = []

    rad_x = width / 2
    rad_y = height / 2

    x1 = x + rad_x
    y1 = y - rad_y

    x2 = x - rad_x
    y2 = y - rad_y
    
    x3 = x - rad_x
    y3 = y + rad_y
    
    x4 = x + rad_x
    y4 = y + rad_y
    

    points = [
        (x1, y1),
        (x2, y2),
        (x3, y3),
        (x4, y4),
    ]
    
    # bounding_box = pygame.draw.rect(surf, color, points)
    bounding_box = pygame.draw.polygon(surf, color, points)
    return bounding_box


# def draw_filled_ellipse(surf: pygame.Surface, x: int, y: int, width: int, color: tuple):
#     filled_rect = pygame. Rect(x, y, width, height)
#     pygame.draw.rect(surf, color, filled_rect)
#     return filled_rect


def draw_filled_polygon(surf: pygame.Surface, x: int, y: int, sides: int, radius: int, color: tuple):
    if sides < 3:
        raise InvalidPolygonException('Too few sides')
    
    segment_angle = int(round(360 / sides, 0))
    
    diameter = 2*radius
    size = (diameter, diameter)
    points = []
    
    print(f'Segment angle: {segment_angle}; Size: {size};')

    for angle in range(0, 360, segment_angle):
        x_off = int(round(radius * math.cos(angle), 0))
        y_off = int(round(radius * math.sin(angle), 0))
        point = (x + x_off, y + y_off)
        points.append(point)
        print(f'Angle: {angle}; Point: {point};')

    bounding_box = pygame.draw.polygon(surf, color, points)

    return bounding_box
