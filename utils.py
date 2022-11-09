import drawSvg as draw
from enum import Enum

# h: horizontal, v: vertical, c_rd: corner right down, 
# c_ld: corner left down, c_ru: corner right up, c_lu: corner left up
# h_r: horizontal half-line, right bit (h_l: left bit)
# v_u: vertical half-line, 
lt = Enum('lt', ['h','v','c_rd','c_ld','c_lu','c_ru','h_r','h_l','v_u','v_d','blank'])

def draw_grid(d, padding, grid_size, bx, by):
    im_x = bx * grid_size + padding * 2
    im_y = by * grid_size + padding * 2

    # draw horizontal lines
    for iy in range(by+1):
        x_start = padding
        x_end = im_x - padding
        y = padding + iy * grid_size

        if iy == 0 or iy == by:
            d.append(draw.Lines(x_start, y,
                                x_end, y,
                                stroke="black",
                                stroke_width=2))
        else:
            d.append(draw.Lines(x_start, y,
                                x_end, y,
                                stroke="gray",
                                stroke_width=1))

    # draw vertical lines
    for ix in range(bx+1):
        y_start = padding
        y_end = im_y - padding
        x = padding + ix * grid_size

        if ix == 0 or ix == bx:
            d.append(draw.Lines(x, y_start,
                                x, y_end,
                                stroke="black",
                                stroke_width=2))
        else:
            d.append(draw.Lines(x, y_start,
                                x, y_end,
                                stroke="gray",
                                stroke_width=1))

    return d

def shift_pearl_pos(pearl, bx, by, grid_size, padding):
    iy = by - pearl[0] - 1
    ix = pearl[1] 

    y = (iy + 0.5) * grid_size + padding
    x = (ix + 0.5) * grid_size + padding

    return x,y

def draw_pearls(d, bx, by, pearl_rad, white_pearls, black_pearls, padding, grid_size):
    # white pearls
    for pearl in white_pearls:
        x, y = shift_pearl_pos(pearl, bx, by, grid_size, padding) 
        d.append(draw.Circle(x, y, pearl_rad,
                            fill="white", stroke_width=2, stroke="black"))

    # black pearls
    for pearl in black_pearls:
        x, y = shift_pearl_pos(pearl, bx, by, grid_size, padding) 
        d.append(draw.Circle(x, y, pearl_rad,
                            fill="black", stroke_width=2, stroke="black"))

    return d

def check_pearl_edge(pearl,size):
    vertical_edge = False
    horizontal_edge = False
    if pearl[0] == 0 or pearl[0] == size[0] - 1:
        vertical_edge = True

    if pearl[1] == 0 or pearl[1] == size[1] - 1:
        horizontal_edge = True

    return vertical_edge, horizontal_edge
    

def draw_loop(d, bx, by, padding, grid_size, lines):
    for i in range(by):
        for j in range(bx):
            l = lines[i][j]

            x,y = shift_pearl_pos((i,j), bx, by, grid_size, padding)

            # vertical line
            if l == lt.v:
                y_start = y - grid_size * 0.5
                y_end = y + grid_size * 0.5
                d.append(draw.Lines(x, y_start,
                                    x, y_end,
                                    stroke_width=4,
                                    stroke="green"))

            # horizontal line
            elif l == lt.h:
                x_start = x - grid_size * 0.5
                x_end = x + grid_size * 0.5
                d.append(draw.Lines(x_start, y,
                                    x_end, y,
                                    stroke_width=4,
                                    stroke="green"))
            elif l == lt.blank:
                continue
            elif l == lt.h_r:
                x2 = x + grid_size * 0.5
                d.append(draw.Lines(x,y,
                                    x2,y,
                                    stroke_width=4,
                                    stroke="green"))
            elif l == lt.h_l:
                x2 = x - grid_size * 0.5
                d.append(draw.Lines(x,y,
                                    x2,y,
                                    stroke_width=4,
                                    stroke="green"))
            elif l == lt.v_u:
                y2 = y + grid_size * 0.5
                d.append(draw.Lines(x,y,
                                    x,y2,
                                    stroke_width=4,
                                    stroke="green"))

            elif l == lt.v_d:
                y2 = y - grid_size * 0.5
                d.append(draw.Lines(x,y,
                                    x,y2,
                                    stroke_width=4,
                                    stroke="green"))
            
            else: # corner
                # left-up
                if l == lt.c_lu:
                    x1_start = x - grid_size * 0.5
                    y2_end = y + grid_size * 0.5
                elif l == lt.c_ld:
                    x1_start = x - grid_size * 0.5
                    y2_end = y - grid_size * 0.5
                elif l == lt.c_ru:
                    x1_start = x + grid_size * 0.5
                    y2_end = y + grid_size * 0.5
                elif l == lt.c_rd:
                    x1_start = x + grid_size * 0.5
                    y2_end = y - grid_size * 0.5
                else:
                    print("error", l)

                d.append(draw.Lines(x1_start, y,
                                    x, y,
                                    stroke_width=4,
                                    stroke="green"))

                d.append(draw.Lines(x, y,
                                    x, y2_end,
                                    stroke_width=4,
                                    stroke="green"))
                
    return d