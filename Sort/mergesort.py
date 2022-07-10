import copy
import pygame
from column import Column, GREY
from Columns import Columns


def algorithm(win, column_width, total_columns, columns):
    mergeSort(win, columns, 0, len(columns)-1)

    # visual for completed sorting
    for column in columns.get_columns():
        column.make_set()

    return columns

def mergeSort(win, columns, startIndex, endIndex):
    if endIndex <= startIndex:
        return

    mid = int(startIndex + (endIndex-startIndex)/2)
    mergeSort(win, columns, startIndex, mid)
    mergeSort(win, columns, mid+1, endIndex)
    merge(win, columns, startIndex, mid, endIndex)

def merge(win, columns, startIndex, mid, endIndex):
    copy_columns = copy.deepcopy(columns)
    k = startIndex
    i = startIndex
    j = mid+1

    # algorithm for merging
    while i <= mid and j <= endIndex:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if copy_columns[i].value > copy_columns[j].value:
            columns[k] = copy_columns[j]
            j += 1
        else:
            columns[k] = copy_columns[i]
            i += 1
        k += 1
    
    while i <= mid:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        columns[k] = copy_columns[i]
        i += 1
        k += 1

    while j <= endIndex:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        columns[k] = copy_columns[j]
        j += 1
        k += 1

    # Setting position of columns for drawing
    last_marked = None
    for i in range(startIndex, endIndex+1):
        if last_marked:
            last_marked.make_deselect()
        columns[i].change_pos(i)
        columns[i].make_swapped()
        last_marked = columns[i]
        columns.draw(win)

    if last_marked:
        last_marked.make_deselect()
    columns.draw(win)

    