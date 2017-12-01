import matplotlib.pyplot as plt
import networkx as nx
import random

def graphNetworkFromFile(plot):

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



	if plot == True:
		# Plotting
		plt.plot() # Create a plot
		#nx.draw(G, with_labels=True, font_weight='bold',node_size=10) # Some arguments that might be handy
		nx.draw(G, pos=gDict,node_size=10)  # Draws all nodes and edges at correct x-y-position

		# THis draws the edges of the graph WITH the weights. This can be removed from the argument list
		#edge_labels = nx.draw_networkx_edge_labels(G, pos=gDict, edge_labels=edgeLabels,label_pos=0.5,font_size=6)

		plt.show() # Need this to see a plot on screen

	# Create 10 orders in form of a list of node
	orderList = [] # empty orderList
	for x in range(0,10): # Number of orders
		rNode = random.choice(gDict.keys()) # get a random node from dictionary
		orderList.append(rNode) # Add the node to the order list

	return G 