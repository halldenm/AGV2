import networkx as nx
import matplotlib.pyplot as plt
from helpers import * 
from graphFixer import * 

# The code is in file is chaotic since it's mostly been used to 
# fin errors in the helper functions

# declare graph
G = nx.DiGraph()
nodes_of_graph = [1,2,3,4,5,6]
G.add_nodes_from(nodes_of_graph)
edges = [(1,2),(2,1),(3,2),(2,3),(4,3),(3,4),(5,4),(4,5),(6,5),(5,6),(1,6),(6,1),(6,2),(2,6),(5,3),(3,5)]
time= 10

# add the time 
G=addTimeDimension(G, nodes_of_graph,edges,time)

startA1= 1 
stopA1= 5

startA2= 4 
stopA2= 6 

startA3= 2 
stopA3= 4 

resA1 =  throughTimeAndSpace(G,startA1,stopA1,time)
print "path for A1 is:"
print resA1

#lägg till alla reserverade noder i t+1
resA1=reserveNodes(resA1)
# ta bort de reserverade noderna
Gtmp = removeReserved(G,resA1)

# find the path for A2 with reservations made for A1 
resA2 = throughTimeAndSpace(Gtmp,startA2,stopA2,time)
print "path for A2 is:"
print resA2

resA2 = reserveNodes(resA2)
Gtmp = removeReserved(Gtmp, resA2)

# find path for A3 
resA3 = throughTimeAndSpace(Gtmp,startA3,stopA3,time)
print "path for A3 is:"
print resA3

# ta bort de noder som är reserverade, 
# gör sedan a* med dem borttagna!	



