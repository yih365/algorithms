import pygame
from node import Node, draw, draw_grid, reconstruct_path


def algorithm(win, width, rows, grid, start, end):
    queue = [start]
    seen_node_set = {start}

    came_from = {}

    while len(queue) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = queue.pop(0)

        # Found goal node
        if current == end:
            reconstruct_path(came_from, end, win, width, rows, grid)
            end.make_end()
            return True

        # Update queue with neighbors
        for neighbor in current.neighbors:
            if neighbor not in seen_node_set:
                queue.append(neighbor)
                seen_node_set.add(neighbor)
                neighbor.make_open()
                came_from[neighbor] = current

        draw(win, grid, rows, width)

        # Mark node as checked
        if current != start:
            current.make_closed()

    # No available path
    return False