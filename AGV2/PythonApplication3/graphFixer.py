import networkx as nx
# takes a directed graph and returns a new graph,
#  that is exanded to indlude a time dimension and "self loops"

def addTimeDimension(graph,nodes,edges,timeSteps):
		addSelfLoops(graph,nodes,edges)
		addTimeNodes(graph,nodes,timeSteps)
		addTimeEdges(graph,edges,timeSteps)
		return graph
	
def addSelfLoops(graph,nodes,edges):
	for i in range(0,len(nodes)):
		new_edge=(nodes[i],nodes[i])
		edges.append(new_edge)
	return edges

def addTimeNodes(graph,nodes,timeSteps):
	for i in range(0,timeSteps):
		for j in range(0,len(nodes)):
			nodes[j]=nodes[j]+10
		graph.add_nodes_from(nodes)
	return nodes

def addTimeEdges(graph,edges,timeSteps):
	for i, line in enumerate(edges):
		 edges[i]=(edges[i][0]),edges[i][1]+10
	graph.add_edges_from(edges)
	for time in range(0,timeSteps):
		for i, line in enumerate(edges):
			edges[i]=(edges[i][0]+10),edges[i][1]+10
		graph.add_edges_from(edges)
	return edges

