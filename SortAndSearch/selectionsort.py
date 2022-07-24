import pygame
from column import Column, GREY
from Columns import Columns


def algorithm(win, column_width, total_columns, columns):
    for i in range(0, len(columns)-1):
        smallestIndex = i
        columns[smallestIndex].make_swapped()
        for j in range(i+1, len(columns)):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if columns[j].value < columns[smallestIndex].value:
                columns[smallestIndex].make_deselect()
                smallestIndex = j
                columns[smallestIndex].make_swapped()

            columns.draw(win)

        columns.swap(i, smallestIndex)
        columns[smallestIndex].make_deselect()
        columns[i].make_set()
    columns[len(columns)-1].make_set()

    return columns
        