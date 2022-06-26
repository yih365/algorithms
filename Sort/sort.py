import pygame
from column import Column, draw
import sys
import random
import time
import bubblesort, selectionsort, insertionsort
import quicksort, mergesort, cocktailsort


WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Search Algorithm")
COLUMNS = 50


def make_columns(columns_num, column_width, game_width):
    columns = []

    for i in range(columns_num):
        column = Column(i, column_width, random.randint(0, columns_num-1), game_width, columns_num)
        columns.append(column)

    return columns


def main(win, game_width, total_columns, args):
    if len(args) < 2:
        sys.exit("Usage: python search.py [algorithm name]")
    if args[1] not in (set(sys.modules)&set(globals()) - {"pygame", "sys", "math", "column"}):
        sys.exit("Sorry this algorithm does not exist here")
    algor = args[1]

    start = time.time()

    column_width = game_width//total_columns
    columns = make_columns(total_columns, column_width, game_width)

    run = True
    while run:
        draw(win, columns)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    module = sys.modules[algor]
                    try:
                        columns = module.algorithm(win, column_width, total_columns, columns)
                        end = time.time()
                        print("Time it took to sort (secs): " + str(end-start))
                    except:
                        sys.exit("Could not complete algorithm")

                if event.key == pygame.K_c:
                    columns = make_columns(total_columns, column_width, game_width)

    pygame.quit()


main(WIN, WIDTH, COLUMNS, sys.argv)

