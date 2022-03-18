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
        pass

    def __lt__(self, other):
        """less than comparator"""
        return False


def h(p1, p2):
    """manhattan distance"""
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2) + abs(y1-y2)


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
    started = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]:
                # if left mouse button is pressed
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]

                if not start:
                    start = node
                    start.make_start()
                elif not end:
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
                    node.reset()
                elif node.is_end():
                    end = None
                    node.reset()
                elif node.is_barrier():
                    node.reset()

    pygame.quit()


main(WIN, WIDTH, ROW_NUMS)