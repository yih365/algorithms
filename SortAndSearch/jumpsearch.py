import pygame
from column import Column
from Columns import Columns
import quicksort
import math 

def algorithm(win, columns_width, total_columns, columns):
    # Sort columns
    quicksort.algorithm(win, columns_width, total_columns, columns)
    columns.clear()

    jumpSize = math.floor(math.sqrt(total_columns))
    index = jumpSize
    while(index < total_columns and columns[index].get_value() < columns.selected.get_value()):
        columns.check(columns[index])
        index += jumpSize

    for i in range(index - jumpSize, index):
        if columns.check(columns[i]):
            break

    return columns