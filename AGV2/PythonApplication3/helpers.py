import networkx as nx
import matplotlib.pyplot as plt

def plotGraph(graph):
	plt.plot() # Create a plot
	nx.draw(graph, with_labels=True, font_weight='bold',node_size=10)
	#nx.draw(G)  # Draws all nodes at correct position
	plt.show() # Need this to see a plot
	return


def throughTimeAndSpace(graph,start,end,timesteps):
	for i in range(0,timesteps):
		try: 
			res =  nx.astar_path(graph,start,end+10*i)
			break 
	   	except: 
			pass
	return res

# add the t+1 node to the reserved nodes
def reserveAndRemove(graph,reserved):
	res=reserveNodes(reserved)
	graph=removeReserved(graph,res)
	return graph

# adds current node in t+1 to the list of reserved nodes
def reserveNodes(reserved):
	stop = len(reserved)
	for i in range(0,stop-1):
		reserved.append(reserved[i]+10)
	return reserved

# returns a copy of the graph with the reserved nodes removed
def removeReserved(graph,reserved):
	Gtmp= graph.copy(as_view=False)
	for i in range(0,len(reserved)):
		Gtmp.remove_node(reserved[i])
	return Gtmp
