import pygame
from column import Column
from Columns import Columns

def algorithm(win, columns_width, total_columns, columns):
    for i in range(0, len(columns)-1):
        if columns.check(columns[i]):
            break

    return columns