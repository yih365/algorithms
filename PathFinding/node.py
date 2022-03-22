import pygame

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


def reconstruct_path(came_from, current, win, width, rows, grid):
    """ Constructs final path """
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw(win, grid, rows, width)


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