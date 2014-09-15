# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 11:42:49 2014

@author: danielgladstone
"""

import networkx as nx
import csv
import os 

location = '/Users/danielgladstone/Google Drive/Genizah/Graphs/name-utf.gexf'

G = nx.read_gexf(location)
count = 0
for node in G.nodes():
        print node
        path = nx.shortest_path_length(G,node)
        print path
        count +=1
        print count

nx.shortest_path(G,'Joseph b. ', 'Sherira Gaon')