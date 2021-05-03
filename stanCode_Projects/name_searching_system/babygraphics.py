"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 500
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE+((width - 2 * GRAPH_MARGIN_SIZE)/len(YEARS))*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # 外框
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # 12條直線
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH,i), 0, get_x_coordinate(CANVAS_WIDTH,i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH,i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor = tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    z = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK          # height座標(根據rank)的標準化
    for j in range(len(lookup_names)):
        n = j % len(COLORS)
        if lookup_names[j] in name_data:                            # 查詢區裡的名字有出現在dict裡
            for i in range(len(YEARS)):                             # 12年度
                year = str(YEARS[i])
                name = lookup_names[j]
                if year in name_data[name]:                         # 如果當年排名有出現在dict裡
                    rank = name_data[name][year]
                    x1 = get_x_coordinate(CANVAS_WIDTH, i)
                    y1 = GRAPH_MARGIN_SIZE+int(rank)*z
                    canvas.create_text(x1, y1, text=str(name)+' '+str(rank), anchor=tkinter.SW)
                    if i > 0:                                       # 畫線需要有前一年的座標
                        old_year = str(YEARS[i-1])
                        if old_year in name_data[name]:                                # 如果前一年排名有出現在dict裡
                            rank0 = name_data[name][old_year]
                            x0 = get_x_coordinate(CANVAS_WIDTH, i-1)
                            y0 = GRAPH_MARGIN_SIZE+int(rank0)*z
                            canvas.create_line(x0, y0, x1, y1, fill=COLORS[n], width=LINE_WIDTH)
                        else:
                            x0 = get_x_coordinate(CANVAS_WIDTH, i - 1)
                            y0 = GRAPH_MARGIN_SIZE + int(MAX_RANK) * z                  # 如果前一年排名不在1000內
                            canvas.create_line(x0, y0, x1, y1, fill=COLORS[n], width=LINE_WIDTH)
                if year not in name_data[name]:                      # 如果當年排名不在1000內
                    x1 = get_x_coordinate(CANVAS_WIDTH, i)
                    y1 = GRAPH_MARGIN_SIZE + int(MAX_RANK) * z
                    canvas.create_text(x1, y1, text=str(name) + ' *', anchor=tkinter.SW)
                    if i > 0:
                        old_year = str(YEARS[i-1])
                        if old_year in name_data[name]:
                            rank0 = name_data[name][old_year]
                            x0 = get_x_coordinate(CANVAS_WIDTH, i-1)
                            y0 = GRAPH_MARGIN_SIZE+int(rank0)*z
                            canvas.create_line(x0, y0, x1, y1, fill= COLORS[n], width= LINE_WIDTH)
                        else:
                            x0 = get_x_coordinate(CANVAS_WIDTH, i - 1)
                            y0 = GRAPH_MARGIN_SIZE + int(MAX_RANK) * z
                            canvas.create_line(x0, y0, x1, y1, fill= COLORS[n], width=LINE_WIDTH)



    # 
            #     if year != '2010':
            #         year2 = str(YEARS[i+1])
            #         rank1 = name_data[name][year]
            #         rank2 = name_data[name][year2]
            #         canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i),GRAPH_MARGIN_SIZE+int(rank1)*z, get_x_coordinate(CANVAS_WIDTH, i+1), GRAPH_MARGIN_SIZE+int(rank2)*z)
            #     # elif year not in year_lst:
            #     #     rank1 = MAX_RANK
            #     #     year2 = str(YEARS[i+1])
            # else:
            #     rank1 = MAX_RANK

    # z = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK
    # for name in lookup_names:
    #     name_rank_txt = {}
    #     if '1900' in name_data[name]:
    #         rank1 = name_data[name]['1900']
    #     else:
    #         rank1 = MAX_RANK
    #     for i in range(1, len(YEARS)):
    #         y = str(YEARS[i])
    #         if y in name_data[name]:
    #             rank2 = name_data[name][y]
    #         else:
    #             rank2 = MAX_RANK
    #         canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i - 1), GRAPH_MARGIN_SIZE + int(rank1) * z,
    #                            get_x_coordinate(CANVAS_WIDTH, i), GRAPH_MARGIN_SIZE + int(rank2) * z, width=LINE_WIDTH)
    #         rank1 = rank2
    #         name_rank_txt[name] = rank1
    #         canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX,
    #                            GRAPH_MARGIN_SIZE + int(name_rank_txt[name]) * z, text=str(name_rank_txt),
    #                            anchor=tkinter.NW)
    #     # for name, rank in name_rank_txt.items():
    #     #     name_rank_txt[name] = rank1
    #     # for j in range(len(YEARS)):
    #     #     canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX, GRAPH_MARGIN_SIZE + int(name_rank_txt[name]) * z, text=str(name_rank_txt), anchor=tkinter.NW)


    # if rank1 == MAX_RANK and rank2 == MAX_RANK:






    # z = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK
    # rank1 = ''

    # for j in range(len(lookup_names)):
    #     for name, year_lst in name_data.items():
    #
    #
    #
    #     for i in range(len(YEARS)):
    #         if str(YEARS[i]) != '2010':
    #             if lookup_names[j] in name and YEARS[i] in year_lst:
    #                 rank = name_data[name][str(YEARS[i])]
    #                 rank1 = rank
    #             else:
    #                 rank = MAX_RANK
    #                 rank1 = rank
    #     canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), GRAPH_MARGIN_SIZE + int(rank1) * z,get_x_coordinate(CANVAS_WIDTH, i + 1), GRAPH_MARGIN_SIZE + int(rank) * z)
















# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
