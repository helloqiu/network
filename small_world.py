# -*- coding: utf-8 -*-

import networkx
import matplotlib.pyplot as plt
import random
import json

l = dict()
c = dict()


def work(n, k, p):
    G = networkx.Graph()
    G.add_nodes_from(range(0, n))
    for i in range(0, n):
        for j in range(1, k + 1):
            G.add_edges_from([(i, (i - j) % n), (i, (i + j) % n)], can_rewire=True)

    # plt.figure(3, figsize=(100, 100), dpi=480)
    # networkx.draw_circular(G, with_labels=False)
    # plt.savefig('origin.png')

    for i in range(0, n):
        nodes = G.neighbors(i)
        for node in nodes:
            if G[i][node]['can_rewire'] and p > random.random():
                G.remove_edge(i, node)
                new = random.randint(0, n - 1)
                temp_neighbors = G.neighbors(i)
                while new in temp_neighbors:
                    new = random.randint(0, n - 1)
                G.add_edge(i, new, can_rewire=False)

    plt.figure(3, figsize=(24, 24), dpi=480)
    networkx.draw_circular(G, with_labels=False)
    plt.savefig('final-%f.png' % p)
    print('p=%f:' % p)
    l[p - 0.0000001] = networkx.average_shortest_path_length(G)
    c[p - 0.0000001] = networkx.average_clustering(G)
    # print('characteristic path: %f' % networkx.average_shortest_path_length(G))
    # print('clustering coefficient: %f' % networkx.average_clustering(G))


if __name__ == '__main__':
    n = int(raw_input('Please input n:'))
    k = int(raw_input('Please input k:'))
    # p = float(raw_input('Please input p:'))
    start = 0.0000001
    distance = 0.01
    for i in range(0, 100):
        p = start + distance
        work(n, k, p)
    with open('l_result.json', 'w') as f:
        f.write(json.dumps(l))
    with open('c_result.json', 'w') as f:
        f.write(json.dumps(c))
