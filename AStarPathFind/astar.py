import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0 )
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

ROW_NUMS = 50


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        """returns row and columns position of node"""
        return self.row, self.col

    def is_closed(self):
        """checks if node has been visited"""
        return self.color == RED 

    def is_open(self):
        """checks if node is in open set"""
        return self.color == GREEN

    def is_barrier(self):
        """checks if node is obstacle"""
        return self.color == BLACK

    def is_start(self):
        """checks if node is starting node"""
        return self.color == ORANGE

    def is_end(self):
        """checks if node is ending node"""
        return self.color == TURQUOISE

    def reset(self):
        """reset node"""
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows -1 and not grid[self.row+1][self.col].is_barrier():
            # Check down a row
            self.neighbors.append(grid[self.row+1][self.col])
        if self.row > 0 and not grid[self.row-1][self.col].is_barrier():
            # Check up a row
            self.neighbors.append(grid[self.row-1][self.col])
        if self.col < self.total_rows -1 and not grid[self.row][self.col+1].is_barrier():
            # Check right a column
            self.neighbors.append(grid[self.row][self.col+1])
        if self.col > 0 and not grid[self.row][self.col-1].is_barrier():
            # Check left a column
            self.neighbors.append(grid[self.row][self.col-1])

    def __lt__(self, other):
        """less than comparator"""
        return False


def h(p1, p2):
    """manhattan distance"""
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2) + abs(y1-y2)


def reconstruct_path(came_from, current, win, width, rows, grid):
    """ Constructs final path """
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw(win, grid, rows, width)


def algorithm(win, width, rows, grid, start, end):
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
        
        # Get next node from PQ
        current = open_set.get()[2]
        open_set_hash.remove(current)

        # Reached the end
        if current == end:
            reconstruct_path(came_from, end, win, width, rows, grid)
            end.make_end()
            return True

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

    # Did not find path
    return False


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


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
        pygame.draw.line(win, GREY, (i*gap, 0), (i*gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y,x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width, rows):
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

                    algorithm(win, width, rows, grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS,width)

    pygame.quit()


main(WIN, WIDTH, ROW_NUMS)