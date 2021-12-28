from igraph.drawing import plot
import networkx as nx
from networkx.algorithms.shortest_paths import weighted
from networkx.generators import directed
import matplotlib.pyplot as plt
from networkx.utils.random_sequence import weighted_choice
from sklearn.utils.extmath import weighted_mode



if __name__ == '__main__':

    # g = nx.Graph(weighted=True, directed=True)
    g = nx.DiGraph(weighted=True, directed=True)
    # g = nx.petersen_graph()

    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_node('f')

    g.add_edge('a', 'b', weight=7)
    g.add_edge('a', 'c', weight=9)
    g.add_edge('a', 'f', weight=14)
    g.add_edge('b', 'c', weight=10)
    g.add_edge('b', 'd', weight=15)
    g.add_edge('c', 'd', weight=11)
    g.add_edge('c', 'f', weight=2)
    g.add_edge('d', 'e', weight=6)
    g.add_edge('e', 'f', weight=9)

    # print(f'Graph data: {g}')
    # for v in g:
    #     print(type(v))
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print(f"{vid}, {wid}, {v.get_weight(w)}")

    #path = nx.dijkstra_path(g, 'a', 'e')


    plt.subplot(121, title= "Grafo")
    # nx.draw_networkx_edges(G, weighted_mode)
    nx.draw_shell(g, with_labels=True, font_weight='bold', node_color='orange')
    pos=nx.shell_layout(g)    
    print(f"pos = {pos}")
    labels = nx.get_edge_attributes(g,'weight')
    print(f'labels: {labels}')
    nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
    
    
    
    
    path = nx.shortest_path(g, 'a', 'e')
    print(f'The shortest path a->e :{path}')    
    plt.subplot(222, title="Shortest Path a->e")    
    nx.draw_shell(g.subgraph(path), with_labels=True, font_weight='bold', node_color='orange')
    # nx.draw_shell(g, nlist=[1, 3], with_labels=True, font_weight='bold', node_color='orange')

    # path = nx.shortest_path(g, 'a', 'f')
    # print(f'The shortest path a->f :{path}')
    # plt.subplot(223)    
    # nx.draw_shell(g.subgraph(path), with_labels=True, font_weight='bold', node_color='orange')

    # path = nx.shortest_path(g, 'a', 'd')
    # print(f'The shortest path a->d :{path}')
    # plt.subplot(224, title="lala")    
    # nx.draw_shell(g.subgraph(path), with_labels=True, font_weight='bold', node_color='orange')
    
 
    
    # nx.draw_shell()

    plt.show()


