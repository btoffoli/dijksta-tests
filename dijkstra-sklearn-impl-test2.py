from sklearn.utils.graph import single_source_shortest_path_length, graph_shortest_path
import numpy as np

graph =  np.array([
                    [0, 5, 10, 11],
                    [5, 0, 6,  8],
                    [10, 6, 0, 9],
                    [11, 8, 9, 0]
                ])

a = list(sorted(single_source_shortest_path_length(graph, 0).items()))
# b = list(sorted(single_source_shortest_path_length(graph, 2).items()))

# a1 = single_source_shortest_path_length(graph, 0)
a1 = graph_shortest_path(graph, False)


print(a)
print(a1)

