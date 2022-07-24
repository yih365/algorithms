from column import Column, BLACK
import pygame
import random

class Columns:
    def __init__(self, columns_num, column_width, game_width):
        self.swap_count = 0
        self.columns = []
        self.columns_num = columns_num

        for i in range(columns_num):
            column = Column(i, column_width, random.randint(0, columns_num-1), game_width, columns_num)
            self.columns.append(column)

    def get_swapcount(self):
        return self.swap_count

    def get_columns(self):
        return self.columns

    def __getitem__(self, index):
        return self.columns[index]

    def __setitem__(self, index, value):
        self.columns[index] = value
        self.swap_count += 1

    def draw(self, win):
        win.fill(BLACK)

        for column in self.columns:
            column.draw(win)

        pygame.display.update()
    
    def swap(self, index1, index2):
        self.columns[index1].change_pos(index2)
        self.columns[index2].change_pos(index1)
        self.columns[index1], self.columns[index2] = self.columns[index2], self.columns[index1]
        self.columns[index1].make_swapped()
        self.columns[index2].make_swapped()
        self.swap_count += 1
        
    def print_columns(self):
        """print columns for debugging"""
        for column in self.columns:
            print(column.get_value(), end='')
        print()

    def select_random(self):
        index = random.randint(0, self.columns_num-1)
        self.columns[index].select()
        self.selected = self.columns[index]
    
    def check(self, column):
        column.make_swapped()
        self.swap_count += 1
        if self.selected.equals(column):
            column.make_set()
            return True
        return False
    
    def get_selected(self):
        return self.selected

    def __len__(self):
        return len(self.columns)
