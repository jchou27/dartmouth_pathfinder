#Name: Jack Chou
#Date: 11/9/2023
#Purpose: To import map image and draw on the map

from load_graph import *
from cs1lib import *
from bfs import *
from vertex import *

WINDOW_X = 1012
WINDOW_Y = 811

start = True
start_x = 0
start_y = 0
end_x = 0
end_y = 0
start_vert = None
end_vert = None
mpressed = False

vertex_dict = create_vertex_dict("dartmouth_graph.txt")


def load_map():
    global start

    if start:
        clear()

        img = load_image("dartmouth_map.png")
        draw_image(img,0 , 0)

        start = False


def my_mpress(mx, my):
    global mpressed, start_x, start_y
    start_x = mx
    start_y = my
    mpressed = True


def my_mmove(mx, my):
    global end_x, end_y
    end_x = mx
    end_y = my


def canvas():
    global start_vert, end_vert, start_x, start_y, end_y, end_x, mpressed

    load_map()

    for vertex in vertex_dict:
        vertex_dict[vertex].draw_all_edges(0, 0, 1)
        vertex_dict[vertex].draw_vertex(0, 0, 1)

    end_vert = None
    for key in vertex_dict:
        if mpressed and vertex_dict[key].is_clicked(start_x, start_y):
            start_vert = vertex_dict[key]
            start_vert.draw_vertex(1, 0, 0)

        if vertex_dict[key].is_clicked(end_x, end_y):
            vertex_dict[key].draw_vertex(1, 0, 0)
            end_vert = vertex_dict[key]


        if start_vert != None and end_vert != None:
            path = breadth_first_search(start_vert, end_vert)
            for val in path:
                val.draw_vertex(1, 0, 0)

            for i in range(len(path) - 1):
                path[i].draw_edge(path[i+1], 1, 0, 0)


start_graphics(canvas, height=WINDOW_Y, width=WINDOW_X, mouse_press=my_mpress, mouse_move=my_mmove)