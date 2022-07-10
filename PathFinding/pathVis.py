import pygame
import sys
import math
import time
from node import Node, draw, draw_grid, reconstruct_path
import astar, dijkstra, DFS, BFS


WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Algorithm")

ROW_NUMS = 50


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y,x = pos

    row = y // gap
    col = x // gap

    return row, col


def make_grid(rows, width):
    """make grid of nodes"""
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


def main(win, width, rows, args):
    if len(args) < 2:
        sys.exit("Usage: python pathVis.py [algorithm name]")
    if args[1] not in (set(sys.modules)&set(globals()) - {"pygame", "sys", "math", "node"}):
        sys.exit("Sorry this algorithm does not exist here")
    algor = args[1]

    startTime = time.time()

    ROWS = rows 
    grid = make_grid(ROWS, width)

    start = None
    end = None
    
    run = True 
    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                # if left mouse button is pressed
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_barrier()
            elif pygame.mouse.get_pressed()[2]:
                # right mouse button
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]

                if node.is_start():
                    start = None
                elif node.is_end():
                    end = None

                node.reset()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    # Use corresponding algorithm
                    module = sys.modules[algor]
                    try:
                        nodes_explored = module.algorithm(win, width, rows, grid, start, end)
                        endTime = time.time()
                        if nodes_explored and isinstance(nodes_explored, int):
                            print("Nodes explored: " + str(nodes_explored))
                        print("Time it took to find path (secs): " + str(endTime-startTime))
                    except:
                        sys.exit("Could not find algorithm")

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS,width)

    pygame.quit()


main(WIN, WIDTH, ROW_NUMS, sys.argv)