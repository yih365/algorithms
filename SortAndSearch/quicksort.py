from itertools import count
import pygame
from column import Column, GREY
from Columns import Columns


def algorithm(win, column_width, total_columns, columns):
    quicksort(win, columns, 0, len(columns)-1)
    for column in columns.get_columns():
        column.make_set()
    return columns


def quicksort(win, columns, low, high):
    if low < high:
        # Sort smaller elements to left of pi
        # and larger elements to right of pi
        pi = partition(win, columns, low, high)
        columns.draw(win)

        quicksort(win, columns, low, pi-1)
        quicksort(win, columns, pi+1, high)


def partition(win, columns, low, high):
    pivot = columns[high]
    i = low-1

    last_swapped = None

    for j in range(low, high):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if columns[j].value < pivot.value:
            # Deselect last swapped
            if last_swapped:
                for item in last_swapped:
                    item.make_deselect()

            # Swap i and j
            i += 1
            columns.swap(i, j)
            last_swapped = (columns[i], columns[j])

        columns.draw(win)
        
    columns.swap(i+1, high)

    # Deselect last swapped
    columns[i+1].make_deselect()
    columns[high].make_deselect()
    if last_swapped:
        for item in last_swapped:
            item.make_deselect()

    pivot.make_set()
    return i+1
