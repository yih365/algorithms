import pygame
import math
from queue import PriorityQueue
from node import Node, draw, draw_grid, reconstruct_path


def h(p1, p2):
    """manhattan distance"""
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2) + abs(y1-y2)


def algorithm(win, width, rows, grid, start, end):
    nodes_explored = 0
    count = 0

    # PQ for getting next best node
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    # Set for checking if something is in pq
    open_set_hash = {start}

    # Keep track of path
    came_from = {}

    # f and g scores table
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = g_score[start] + h(start.get_pos(), end.get_pos())

    # while still available nodes to explore
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        nodes_explored += 1       

        # Get next node from PQ
        current = open_set.get()[2]
        open_set_hash.remove(current)

        # Reached the end
        if current == end:
            reconstruct_path(came_from, end, win, width, rows, grid)
            end.make_end()
            break

        # Update neighbor scores
        for neighbor in current.neighbors:
            temp_g_score = g_score[current]+1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw(win, grid, rows, width)

        # Mark node as checked
        if current != start:
            current.make_closed()

    return nodes_explored