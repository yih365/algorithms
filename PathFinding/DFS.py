import pygame
from node import Node, draw, draw_grid, reconstruct_path


def algorithm(win, width, rows, grid, start, end):
    nodes_explored = 0
    stack = []
    stack.append(start)
    seen_node_set = {start}

    came_from = {}

    while len(stack) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        nodes_explored += 1

        current = stack.pop()

        # Found goal
        if current == end:
            reconstruct_path(came_from, end, win, width, rows, grid)
            end.make_end()
            break

        # Add valid neighbors to stack
        for neighbor in current.neighbors:
            if neighbor not in seen_node_set:
                stack.append(neighbor)
                seen_node_set.add(neighbor)
                came_from[neighbor] = current
                neighbor.make_open()

        draw(win, grid, rows, width)

        # Mark node as checked
        if current != start:
            current.make_closed()

    return nodes_explored
                