import random
import time
from graphs.my_graph import My_graph


def color_vertex(graph):
    #Si poteva non fare l'ultimo ma computazionalmente è la stessa cosa perchè fare un confronto è come fare un
    #assegnazione (entrambe O(1)) quindi abbiamo lasciato così
    for vertex in graph.vertices():
        if vertex.colored():
            continue
        for v in graph.not_colored_vertex(vertex):
            if graph.not_colored_degree(vertex) >= graph.not_colored_degree(v):
                vertex.color()
                break
            else:
                v.color()

t0=time.time()
for j in range(100):
    graph = My_graph()
    for i in range(100):
        graph.insert_vertex(i)

    for vertex in graph.vertices():
        for v in graph.vertices():
            if not(v == vertex or (graph.get_edge(vertex, v) is not None)): # if there isn't a self loop or an edge already exists
                if random.randint(0, 50) == 0:
                    graph.insert_edge(vertex, v)

    t1 = time.time_ns()
    color_vertex(graph)
    t2 = time.time_ns()
    colored = 0
    for v in graph.vertices():
        if v.colored():
            colored = colored + 1
    t = t2 - t1
    print("Execution time of graph {}:".format(j))
    print("Execution made in {0:.5f} ns".format(t))
    print("Colored nodes are: {}".format(colored))
tf=time.time()
print("Total Execution made in {0:.5f} ms".format(tf-t0))