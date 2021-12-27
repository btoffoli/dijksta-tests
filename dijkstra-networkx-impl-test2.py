import networkx as nx



if __name__ == '__main__':

    g = nx.Graph()

    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_node('f')

    g.add_edge('a', 'b', weigth=7)
    g.add_edge('a', 'c', weigth=9)
    g.add_edge('a', 'f', weigth=14)
    g.add_edge('b', 'c', weigth=10)
    g.add_edge('b', 'd', weigth=15)
    g.add_edge('c', 'd', weigth=11)
    g.add_edge('c', 'f', weigth=2)
    g.add_edge('d', 'e', weigth=6)
    g.add_edge('e', 'f', weigth=9)

    print('Graph data:')
    # for v in g:
    #     print(type(v))
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print(f"{vid}, {wid}, {v.get_weight(w)}")

    path = nx.dijkstra_path(g, 'a', 'e')

    
    # nx.shortest_path('a', 'e')
    print(f'The shortest path :{path[::-1]}')
