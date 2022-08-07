import pygame
from column import Column
from Columns import Columns
import quicksort

def algorithm(win, columns_width, total_columns, columns):
    # Sort columns
    quicksort.algorithm(win, columns_width, total_columns, columns)
    columns.clear()

    high = total_columns-1
    low = 0
    while(low < high):
        mid = (high+low)//2
        if columns.check(columns[mid]):
            break
        
        if columns.get_selected().get_value() > columns[mid].get_value():
            low = mid + 1
        else:
            high = mid - 1

    return columns