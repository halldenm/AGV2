import networkx as nx
# takes a directed graph and returns a new graph,
#  that is exanded to indlude a time dimension and "self loops"

# expands the graph in a second dimensions for time, note that the graph is directed so that it is only possible to go forward in time 
def addTimeDimension(graph,nodes,edges,timeSteps):
		addTimeSuffixes(graph,nodes,edges)
		addSelfLoops(graph,nodes,edges)
		addTimeNodes(graph,nodes,timeSteps)
		addTimeEdges(graph,edges,timeSteps)
		
		return graph


# adds self loops to the inputted graph, this is to allow for waiting in a node 
def addSelfLoops(graph,nodes,edges):
	for i in range(0,len(nodes)):
		new_edge=(nodes[i],nodes[i])
		edges.append(new_edge)
	return edges

# adds nodes for next timestep 
def addTimeNodes(graph,nodes,timeSteps):
	
	for i in range(1,timeSteps):
		time=1*i
		timestr=str(time)
		for j in range(0,len(nodes)):

			new_node= nodes[j].split('.')
			nodes[j]=new_node[0]+'.'+timestr
		graph.add_nodes_from(nodes)
	return graph

# adds edges forward in time. also changes the edges of the graph in order to make it directed forward in time 
def addTimeEdges(graph,edges,timeSteps):
	#remove the original edges
	graph.remove_edges_from(edges)

	# here starts the string manipulation which is a bit messy
	timestr='.1'
	for i, line in enumerate(edges):

		new_edge= edges[i][1].split('.')
		new_edge= new_edge[0]+timestr
		new_edge=edges[i][0],new_edge
		edges[i]=new_edge
	graph.add_edges_from(edges)

	for time in range(1,timeSteps):
		timenr=1*time
		timestr=str(timenr)
		if time !=0:
			timestrNxt=str(timenr+1)
		for i, line in enumerate(edges):
			new_edge= edges[i][0].split('.') # split each part of the edge and add the time step
			new_edgeNxt =edges[i][1].split('.')

			new_edge= new_edge[0]+'.'+timestr
			new_edgeNxt = new_edgeNxt[0]+'.'+timestrNxt

			# add each part of the new edge together
			#new_edge=new_edge,new_edgeNxt

			edges[i]=new_edge,new_edgeNxt


			
		graph.add_edges_from(edges)
	return edges

# adds time siffixes
def addTimeSuffixes(graph,nodes,edges):
	graph = addNodeTimeSuffix(nodes,graph)
	graph = addEdgeTimeSuffix(edges,graph)
	return graph

#adds the time suffix to inputed nodes 
def addNodeTimeSuffix(nodes,graph):
	graph.remove_nodes_from(nodes)
	timestr='.0'
	for i in range(0,len(nodes)):
		nodes[i]+=timestr
	graph.add_nodes_from(nodes)
	return graph

#adds the time suffix to inputed edges
def addEdgeTimeSuffix(edges,graph):
	graph.remove_edges_from(edges)
	timestr='.0'
	for i in range(0,len(edges)):
		
		edges[i]=(edges[i][0]+timestr),edges[i][1]+timestr
		
	graph.add_edges_from(edges)
	return graph
	
