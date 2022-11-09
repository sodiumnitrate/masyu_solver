import drawSvg as draw
import sys
from utils import *

class Board:
    def __init__(self, size_x=None, size_y=None, 
                 white_pearls=None, black_pearls=None, lines=None):
        self.size = (size_x, size_y)
        self.white_pearls = white_pearls
        self.black_pearls = black_pearls
        self.lines = lines

    def init_lines(self):
        lines = []
        for i in range(self.size[1]):
            row = []
            for j in range(self.size[0]):
                row.append(lt.blank)
            lines.append(row)
        self.lines = lines

    def print_board(self):
        if self.size[0] is None or self.white_pearls is None or self.black_pearls is None:
            print("Error: board uninitialized")
            return
        board_string = """"""
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                if (i,j) in self.white_pearls:
                    board_string += 'w'
                elif (i,j) in self.black_pearls:
                    board_string += 'b'
                else:
                    board_string += '.'
            board_string += '\n'
        print(board_string)

    def save_svg(self,padding=50,grid_size=40,pearl_rad=15,fname="board.svg"):
        if self.size[0] is None or self.white_pearls is None or self.black_pearls is None:
            print("Error: board uninitialized")
            return
        im_x = self.size[0] * grid_size + padding * 2
        im_y = self.size[1] * grid_size + padding * 2

        d = draw.Drawing(im_x, im_y, origin=(0,0))
        d = draw_grid(d,padding, grid_size,self.size[0],self.size[1])
        d = draw_pearls(d, self.size[0], self.size[1], pearl_rad,
                        self.white_pearls, self.black_pearls,
                        padding, grid_size)

        d = draw_loop(d, self.size[0], self.size[1], padding,
                      grid_size, self.lines)

        d.saveSvg(fname)

    def first_pass(self):
        self.init_lines()
        
        # white pearls near edge
        for pearl in self.white_pearls:
            vertical_edge, horizontal_edge = check_pearl_edge(pearl,self.size)    
            if vertical_edge and horizontal_edge:
                sys.exit("Invalid board: there is a white pearl at the corner")