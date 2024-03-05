#Name: Jack Chou
#Date: 11/09/2023
#Purpose: To parse out dartmouth_graph txt file and insert the name, coordinates, and adj verticies into a dictionary

from vertex import *

def create_vertex_dict(input_file):
    vertex_dict = {}

    dartmouth = open(input_file, "r")

    for line in dartmouth:
        split_paras = line.split(";")

        name = split_paras[0].strip()

        cord = split_paras[2].strip().split(",")
        x = cord[0].strip()
        y = cord[1].strip()

        vertex_dict[name] = Vertex(name, x, y, [])

        # print(vertex_dict[name])

    dartmouth.close()

    dartmouth = open(input_file, "r")

    for line in dartmouth:
        split_paras = line.split(";")

        name = split_paras[0].strip()
        adj_vertex = split_paras[1].strip().split(",")
        # print(adj_vertex)
        for places in adj_vertex:
            adj = places.strip()
            vertex_dict[name].adj_vert_list.append(vertex_dict[adj])


    dartmouth.close()
    return vertex_dict


create_vertex_dict("dartmouth_graph.txt")




