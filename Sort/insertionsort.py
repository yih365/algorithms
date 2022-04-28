import pygame
from column import Column, draw, swap, print_columns, GREY


def algorithm(win, column_width, total_columns, columns):
    last_swap = None
    for i in range(1, len(columns)):
        index = i
        while index > 0 and columns[index].value < columns[index-1].value:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            if last_swap:
                last_swap.make_deselect()
            last_swap = columns[index-1]
            swap(columns, index, index-1)

            draw(win, columns)

            index -= 1
        columns[index].make_deselect()

    for i in range(0, len(columns)):
        columns[i].make_set()

    return columns