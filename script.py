import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab


break_flag = True
matrix = []
with open('weight_adj.txt') as f:
    while break_flag:
        row = [] 
        while True:
            c = f.read(1)
            if c == '':
                break_flag = False
                break
            elif c == '\n':
                break
            elif c == ' ':
                continue
            else:
                row.append(c)
        matrix.append(row)

weighted_edges = [] 
row = 0
col = 0
while row < len(matrix):
    while col < len(matrix[row]):
        if matrix[row][col] != '0':           
            weighted_edges.append(tuple([row,col, matrix[row][col]]))
        col += 1
    row += 1
    col = row


G=nx.karate_club_graph()
#pos = nx.spring_layout(G)
G.add_weighted_edges_from(weighted_edges)
edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])

#pos=nx.shell_layout(G)
pos=nx.spring_layout(G)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw(G,pos,with_labels=True)

plt.show()
