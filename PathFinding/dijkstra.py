import pygame
from queue import PriorityQueue
from node import Node, draw, draw_grid, reconstruct_path


def algorithm(win, width, rows, grid, start, end):
    # PQ for getting next best node
    open_set = PriorityQueue()
    count = 0
    open_set.put((0, 0, start))
    open_set_hash = {start}

    came_from = {}

    # score for dijkstra algorithm
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    # while still available nodes to explore
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Get next node from PQ
        saved_g, _, current = open_set.get()
        open_set_hash.remove(current)
        # Visited using a different item in PQ with lower g score
        if g_score[current] < saved_g:
            continue

        # found target
        if current == end:
            reconstruct_path(came_from, end, win, width, rows, grid)
            end.make_end()
            return True

        # Iterate over neighbors
        for neighbor in current.neighbors:
            temp_g_score = g_score[current]+1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score

                count += 1
                open_set.put((g_score[neighbor], count, neighbor))
                open_set_hash.add(neighbor)
                neighbor.make_open()
        
        draw(win, grid, rows, width)

        # Mark node as checked
        if current != start:
            current.make_closed()

    # No valid path
    return False
    