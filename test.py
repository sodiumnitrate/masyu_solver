from board import *

white_pearls = [(1,3), (1,4), (3,1), (3,6), (4,1), (4,6),
                (6,0), (6,2), (6,5), (6,7), (8,0), (8,7)]
black_pearls = [(3,3),(3,4),(4,3),(4,4),(7,1),(7,3),(7,4),(7,6)]

masyu_board = Board(8, 10, 
                    white_pearls=white_pearls, black_pearls=black_pearls)

masyu_board.init_lines()

# manual input solution
masyu_board.lines[0][3] = lt.c_rd
masyu_board.lines[0][4] = lt.c_ld
masyu_board.lines[3][3] = lt.c_lu
masyu_board.lines[3][4] = lt.c_ru
masyu_board.lines[1][3] = lt.v
masyu_board.lines[2][3] = lt.v
masyu_board.lines[1][4] = lt.v
masyu_board.lines[2][4] = lt.v
masyu_board.lines[3][1] = lt.h
masyu_board.lines[3][2] = lt.h
masyu_board.lines[3][5] = lt.h
masyu_board.lines[3][6] = lt.h
masyu_board.lines[3][0] = lt.c_rd
masyu_board.lines[4][0] = lt.c_ru
masyu_board.lines[3][7] = lt.c_ld
masyu_board.lines[4][7] = lt.c_lu
masyu_board.lines[4][3] = lt.c_ld
masyu_board.lines[4][4] = lt.c_rd
masyu_board.lines[5][3] = lt.v
masyu_board.lines[5][4] = lt.v
masyu_board.lines[6][3] = lt.c_lu
masyu_board.lines[6][4] = lt.c_ru
masyu_board.lines[4][1] = lt.h
masyu_board.lines[4][2] = lt.h
masyu_board.lines[4][5] = lt.h
masyu_board.lines[4][6] = lt.h
masyu_board.lines[5][3] = lt.v
masyu_board.lines[5][4] = lt.v
masyu_board.lines[6][2] = lt.h
masyu_board.lines[6][5] = lt.h
masyu_board.lines[7][2] = lt.h
masyu_board.lines[7][5] = lt.h
masyu_board.lines[7][3] = lt.c_ld
masyu_board.lines[7][4] = lt.c_rd
masyu_board.lines[7][3] = lt.c_ld
masyu_board.lines[7][4] = lt.c_rd
masyu_board.lines[5][0] = lt.c_rd
masyu_board.lines[5][1] = lt.c_ld
masyu_board.lines[6][1] = lt.c_ru
masyu_board.lines[7][1] = lt.c_rd
masyu_board.lines[9][0] = lt.c_ru
masyu_board.lines[9][1] = lt.c_lu
masyu_board.lines[9][3] = lt.c_ru
masyu_board.lines[9][4] = lt.c_lu
masyu_board.lines[9][6] = lt.c_ru
masyu_board.lines[9][7] = lt.c_lu
masyu_board.lines[6][6] = lt.c_lu
masyu_board.lines[5][6] = lt.c_rd
masyu_board.lines[5][7] = lt.c_ld
masyu_board.lines[6][0] = lt.v
masyu_board.lines[7][0] = lt.v
masyu_board.lines[8][0] = lt.v
masyu_board.lines[8][1] = lt.v
masyu_board.lines[8][3] = lt.v
masyu_board.lines[8][4] = lt.v
masyu_board.lines[8][6] = lt.v
masyu_board.lines[6][7] = lt.v
masyu_board.lines[7][7] = lt.v
masyu_board.lines[8][7] = lt.v
masyu_board.lines[7][6] = lt.c_ld

masyu_board.print_board()

masyu_board.save_svg()