import pygame
from column import Column
from Columns import Columns
import sys
import random
import time
import bubblesort, selectionsort, insertionsort
import quicksort, mergesort, cocktailsort


WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sort Algorithm")
COLUMNS = 50

def main(win, game_width, total_columns, args):
    if len(args) < 2:
        sys.exit("Usage: python sort.py [algorithm name]")
    if args[1] not in (set(sys.modules)&set(globals()) - {"pygame", "sys", "math", "column", "Columns"}):
        sys.exit("Sorry this algorithm does not exist here")
    algor = args[1]

    start = time.time()

    column_width = game_width//total_columns
    columns = Columns(total_columns, column_width, game_width)

    run = True
    while run:
        columns.draw(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    module = sys.modules[algor]
                    try:
                        columns = module.algorithm(win, column_width, total_columns, columns)
                        end = time.time()
                        print("Times swapped: " + str(columns.get_swapcount()))
                        print("Time it took to sort (secs): " + str(end-start))
                    except:
                        sys.exit("Could not complete algorithm")

                if event.key == pygame.K_c:
                    columns = Columns(total_columns, column_width, game_width)

    pygame.quit()


main(WIN, WIDTH, COLUMNS, sys.argv)
