# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 19:25:52 2014

@author: danielgladstone
"""

import networkx as nx
import os 

destination = '/Users/danielgladstone/Google Drive/MTH 492/Weighted Graphs/striaghtn.gexf'

G = nx.DiGraph()

e = [('Manuel','Charles'),('Manuel','Donna'),('Manuel','Stuart'),('Charles','Carol'),('Carol','Jim'),('Charles','Harold'),('Charles','Wynn'),('Donna','K'),('Donna','N'),('Donna','S'),('Donna','T'),('Stuart','B'),('Stuart','F'),('Stuart','Sh')]

r = [('Nancy','Manuel'),('Nancy','Stuart'),('Nancy','Donna'),('Nancy','Tanya'),('Fred','Bob'),('Nancy','Charles'),('Nancy','Kathy'),('Stuart','Charles'),('Charles', 'Stuart'),('Stuart','Fred'),('Stuart','Bob'),('Stuart','Sharon'),('Sharon','Bob'),('Charles','Wynn'),('Charles','Carol'),('Charles','Harold'),('Donna','Susan'),('Donna','Kathy'),('Donna','Tanya'),('Manuel','Donna'),('Manuel','Charles'),('Manuel','Stuart')]

n = [(1,2),(2,3),(3,4),(4,5)]

a = [(u'a',u'b'),(u'b',u'c'),(u'c',u'd'),(u'd',u'e')]

def add_node(name, weight = None):
    if not G.has_node(name):
        G.add_node(name)
        G.node[name]['latitude'] = 0
        
def add_edge_G(n1, n2):
    if not G.has_edge(n1,n2):
        G.add_edge(n1,n2)
        G.edge[n1][n2]['weight'] = None


for thing in a:
    add_node(thing[0])
    add_node(thing[1])
    add_edge_G(thing[1],thing[0])
#
for node in G.nodes():
    dic = nx.shortest_path(G,node) #list of all end targets
    for end_target in dic.keys():
        path = nx.shortest_path(G,node,end_target) #list of all nodes between each end target and start node
#        print 'nnode = ' + str(node)
        print '    '
        print '------'
        print 'node = ' + str(node)
        print 'end_target = ' + str(end_target)
        print 'path =' + str(path)
        for path_node in path:
            if G.has_edge(node, path_node) == True:
                print '++++'
                print 'path_node = ' + str(path_node)
                if G.edge[node][path_node]['weight'] == None:
                    G.edge[node][path_node]['weight'] = 2.0
                else:
                    G.edge[node][path_node]['weight'] += 1.0 /int(G.edge[node][path_node]['weight'])
                print 'weight = ' + str(G.edge[node][path_node]['weight'])



if os.path.isfile(destination) == True:
    os.remove(destination)
    

nx.write_gexf(G,destination)