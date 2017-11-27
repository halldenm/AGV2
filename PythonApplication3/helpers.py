import networkx as nx
import matplotlib.pyplot as plt


# plots out the graph G with numbered nodes 
def plotGraph(graph):
	plt.plot() # Create a plot
	nx.draw(graph, with_labels=True, font_weight='bold',node_size=10)
	#nx.draw(G)  # Draws all nodes at correct position
	plt.show() # Need this to see a plot
	return





# creates a route for the selected agent in the time expanded graph. 
def throughTimeAndSpace(graph,originalGraph,start,end,timesteps):
	minsteps=len(nx.astar_path(originalGraph,str(start),str(end)))
	print nx.astar_path(originalGraph,str(start),str(end))
	print minsteps
	#minsteps=1
	start= str(start)+'.0'
	
	for i in range(minsteps-1,timesteps):
		
		timenr=1*i
		timestr='.'+str(timenr)
		print start
		print str(end)+timestr

		
		try: 
			res =  nx.astar_path(graph,str(start),str(end)+timestr)
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
		timenr=1*(i+1)
		timestr='.'+str(timenr)
		reservedTmp = reserved[i].split('.')
		reservedTmp = reservedTmp[0]+timestr
		if reservedTmp not in reserved:
			reserved.append(reservedTmp)
	return reserved

# returns a copy of the graph with the reserved nodes removed
def removeReserved(graph,reserved):
	#Gtmp= graph.copy(as_view=False)
	for i in range(0,len(reserved)):
		graph.remove_node(reserved[i])
	return graph
