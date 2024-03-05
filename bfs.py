#Name: Jack Chou
#Date: 11/12/2023
#Purpose: Create a BFS function

from collections import deque

def breadth_first_search(start, end):
    backpointers = {start: None}
    path = []
    q = deque([start])

    while len(q) != 0:
        current_vertex = q.popleft()

        for vertex in current_vertex.adj_vert_list:
            if vertex not in backpointers:
                backpointers[vertex] = current_vertex
                q.append(vertex)

        if current_vertex == end:
            f_vert = end
            path.append(end)
            while f_vert != start:
                f_vert = backpointers[f_vert]
                path.append(f_vert)

    return path









