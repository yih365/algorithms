from itertools import count
import pygame
from column import Column, draw, swap, print_columns, GREY


def algorithm(win, column_width, total_columns, columns):
    last_pair = None
    swapped = True
    start = 0
    end = len(columns) - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if columns[i].get_value() > columns[i+1].get_value():
                if last_pair:
                    for item in last_pair:
                        if item.color != GREY:
                            item.make_deselect()
                last_pair = (columns[i], columns[i+1])
                columns = swap(columns, i, i+1)
                swapped = True
            draw(win, columns)
        if last_pair:
            for item in last_pair:
                if item.color != GREY:
                    item.make_deselect()
        columns[end].make_set()

        if not swapped:
            break

        swapped = False

        end -= 1

        last_pair = None

        for i in range(end-1, start-1, -1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if columns[i].get_value() > columns[i+1].get_value():
                if last_pair:
                    for item in last_pair:
                        if item.color != GREY:
                            item.make_deselect()
                last_pair = (columns[i], columns[i+1])
                columns = swap(columns, i, i+1)
                swapped = True
            draw(win, columns)
        if last_pair:
            for item in last_pair:
                if item.color != GREY:
                    item.make_deselect()
        columns[start].make_set()

        start += 1

    for i in range(0, len(columns)):
        columns[i].make_set()

    return columns
