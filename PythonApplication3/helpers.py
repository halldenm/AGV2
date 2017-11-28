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
	
	minsteps=len(nx.astar_path(originalGraph,str(start),str(end))) # used to find a shortcut
	# looks at the shortest path for the original graph then stores the length of this and uses this as starting point for the pathfinding in time domain
	print nx.astar_path(originalGraph,str(start),str(end)) # prints shortest path for original graph, used for debuggin
	print minsteps # prints number of steps, used for debuggin 
	print "lengt of path:"
	print nx.astar_path_length(originalGraph,str(start),str(end))
	#minsteps=1
	start= str(start)+'.0' # start node + time suffix
	
	for i in range(minsteps-1,timesteps): # loop thorugh the time expanded graph
		
		timenr=1*i 
		timestr='.'+str(timenr) # time suffix for each end node 
		print (start)   # prints start node 
		print str(end)+timestr  # prints end node 

		
		try: 
			res =  nx.astar_path(graph,str(start),str(end)+timestr) # looks if there is a solution in the current time step
			break # breaks if there a solution for this timestep
	   	except: # continues loop if there is no solution
			pass 
 	return res

# add the t+1 node to the reserved nodes
def reserveAndRemove(graph,reserved):# reserves the nodes and removes them form the graph
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
