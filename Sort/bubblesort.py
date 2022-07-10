import pygame
from column import Column, GREY
from Columns import Columns


def algorithm(win, column_width, total_columns, columns):
    last_pair = (columns[0], columns[1])

    for i in range(0, len(columns)-1):
        for j in range(0, len(columns)-i-1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if columns[j].get_value() > columns[j+1].get_value():
                for item in last_pair:
                    if item.color != GREY:
                        item.make_deselect()
                columns.swap(j, j+1)
                last_pair = (columns[j], columns[j+1])
            
            columns.draw(win)

        columns[len(columns)-i-1].make_set()
    columns[0].make_set()

    return columns 

