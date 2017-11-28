import matplotlib.pyplot as plt
import networkx as nx
import random
import numpy
from Astar import a_star_search

G=nx.DiGraph() # Create a graph
gDict ={} # A dictionary of nodes is needed (hashmap)
edgeLabels = {} # A dictionary of edges (hashmap),
with open('layout.txt','r') as f: # Open the file
        for line in f: # For every line in the file
            gType = line.split()[0] # The type of the graph element
            typeId = line.split()[1] # The id of the graph element
            if gType == 'point': # Nodes
                x = int(line.split()[2]) # x-position in int
                y = int(line.split()[3]) # y-position in int
                gDict[typeId] = (x,y) # Add the node to the dictionary
                G.add_node(typeId,pos=(x,y)) # Add the node to te Graph
            elif gType == 'segment': # Edge
                fV = line.split()[2] # Gets the from Vertex
                tV = line.split()[3] # Gets the to Vertex
                weight = int(line.split()[4]) # Get the weight of the edge
                edgeLabels[(fV,tV)] = weight # Add it to the dictionary
                G.add_edge(fV,tV, weight=weight)  # Add the edge to the graph

nAgents = 2
windowSize = 4

# Astar
startIndices, goalIndices = [0, 2], [20, 22]
listStartNodes = [0 for x in range(nAgents)]
listGoalNodes = [0 for x in range(nAgents)]
for agent in range(0,nAgents):
    listStartNodes[agent], listGoalNodes[agent] = list(G.nodes)[startIndices[agent]], list(G.nodes)[goalIndices[agent]] 
print(list(G.nodes))
#print(list(G.nodes)[startIndex])
#reservationList = [[],[]]

# Creates a list containing 5 lists, each of 8 items, all set to 0
reservationList = [[0 for x in range(windowSize)] for y in range(nAgents)]
hej = 0
while hej != 10:
   
    for agent in range(0,nAgents):
        path, cost = a_star_search(G, listStartNodes[agent], listGoalNodes[agent], reservationList)
        print("path = ", path)
        print("cost = ", cost)

        # global reservation table
        if len(path) >= windowSize:
            reservationList[agent][0:windowSize] = list(path)[0:windowSize]
        else:
            reservationList[agent][0:(len(path))] = list(path)[0:(len(path))]

        listStartNodes[agent] = list(reservationList[agent])[len(reservationList[agent])-1]
        #print(reservationList)
        #print(start)
    hej = hej + 1

reservationList = []

listOfNodes = list(numpy.setdiff1d(list(G.nodes), path, assume_unique=True))
# Plotting
plt.plot() # Create a plot
#nx.draw(G, with_labels=True, font_weight='bold',node_size=10) # Some arguments that might be handy
#nx.draw(G, pos=gDict, node_size=10)  # Draws all nodes and edges at correct x-y-position
#nx.draw_networkx_nodes(G, path, node_color = 'g')
# THis draws the edges of the graph WITH the weights. This can be removed from the argument list
#edge_labels = nx.draw_networkx_edge_labels(G, pos=gDict, edge_labels=edgeLabels,label_pos=0.5,font_size=6)

nx.draw_networkx_nodes(G, pos=gDict, nodelist = listOfNodes, node_color = 'r', node_size = 10)
nx.draw_networkx_nodes(G, pos=gDict, nodelist = path, node_color = 'g', node_size = 10)
nx.draw_networkx_edges(G, pos=gDict)
#labels = {}
#labels[startIndex] ="s"
#labels[goalIndex] ="g"
#nx.draw_networkx_edge_labels(G, pos=gDict, labels, font_size=16)

plt.show() # Need this to see a plot on screen

# Create 10 orders in form of a list of node
orderList = [] # empty orderList
for x in range(0,10): # Number of orders
    rNode = random.choice(gDict.keys()) # get a random node from dictionary
    orderList.append(rNode) # Add the node to the order list
