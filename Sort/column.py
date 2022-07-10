import pygame

WHITE = (255, 255, 255)
BLUE = (0, 255, 0)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)


class Column:
    def __init__(self, position, width, value, game_width, total_columns):
        self.position = position
        self.width = width
        self.total_columns = total_columns
        self.value = value 
        self.color = WHITE
        self.pheight = value * (game_width//total_columns)
        self.x = self.position*width
        self.y = game_width-self.pheight

    def get_value(self):
        return self.value

    def get_pos(self):
        return self.x, self.y

    def make_swapped(self):
        self.color = BLUE

    def make_set(self):
        self.color = GREY

    def make_deselect(self):
        self.color = WHITE

    def change_pos(self, new_pos):
        self.position = new_pos
        self.x = self.position*self.width

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.pheight))

    def __lt__(self, other):
        return False
