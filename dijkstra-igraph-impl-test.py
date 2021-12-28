import igraph as ig
from networkx.generators import directed



if __name__ == '__main__':

    g = ig.Graph(directed=True)

    a = g.add_vertex('a')
    b = g.add_vertex('b')
    c = g.add_vertex('c')
    d = g.add_vertex('d')
    e = g.add_vertex('e')
    f = g.add_vertex('f')

    g.add_edge('a', 'b', weigth=7)
    g.add_edge('a', 'c', weigth=9)
    g.add_edge('a', 'f', weigth=14)
    g.add_edge('b', 'c', weigth=10)
    g.add_edge('b', 'd', weigth=15)
    g.add_edge('c', 'd', weigth=11)
    g.add_edge('c', 'f', weigth=2)
    g.add_edge('d', 'e', weigth=6)
    g.add_edge('e', 'f', weigth=9)


    print(f'Graph data: {g}')
    # for v in g:
    #     print(type(v))
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print(f"{vid}, {wid}, {v.get_weight(w)}")

    #path = nx.dijkstra_path(g, 'a', 'e')

    
    # path = g.all_st_cuts(a, e)
    # print(path)
    # path = g.shortest_paths_dijkstra(source='a', target='e')
    path = g.get_shortest_paths('a', 'd')
    print(f'The shortest path a->d :{path}')

    path = g.get_shortest_paths('a', 'f')
    print(f'The shortest path a->f :{path}')

    path = g.get_shortest_paths('a', 'e')
    print(f'The shortest path a->e :{path}')
