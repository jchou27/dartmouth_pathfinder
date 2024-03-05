#Name: Jack Chou
#Date: 11/09/2023
#Purpose: create vertex class
from cs1lib import *

RAD = 9
STROKE_WIDTH = 4

class Vertex:
    def __init__(self, name, x, y, adj_vert_list):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adj_vert_list = adj_vert_list

    def __str__(self):
        adj_vertex_name = self.adj_vert_list[0].name
        for vertex in self.adj_vert_list:
            if vertex != self.adj_vert_list[0]:
                adj_vertex_name += "," + vertex.name

        return str(self.name) + "; " + "Location: " + str(self.x) + "," + str(self.y) + "; " + "Adjacent vertices: " + adj_vertex_name

    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, RAD)

    def draw_edge(self, vert_obj, r, g, b):
        enable_stroke()
        set_stroke_width(STROKE_WIDTH)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, vert_obj.x, vert_obj.y)

    def draw_all_edges(self, r, g, b):
        for vertex in self.adj_vert_list:
            self.draw_edge(vertex, r, g, b)

    def is_clicked(self, x, y):
        if (self.x - RAD) <= x <= (self.x + RAD) and (self.y - RAD) <= y <= (self.y + RAD):
            return True
        else:
            return False







