from fractions import gcd

# Make the graph unweighed
def weightToUnweight(graph):
	weights= getWeights(graph)
	gcdOfWeighed(weights)
	graph=splitEdges(graph,weights)
	#add the new edges to the grahp

# returns the weights of all edges rounded UP to nearest 1000ms
def getWeights(graph):
	weights=list()
	weightsTmp = list(graph.edges(data='weight'))
	for i, line in enumerate(weightsTmp):
		if weightsTmp[i][2]%1000 >500:
			weights.append(int( round(weightsTmp[i][2],-3)))
		elif (weightsTmp[i][2]%1000 <500):
			weights.append(int( round(weightsTmp[i][2]+500,-3)))

	return weights

# splits the edges into second slots and replaces the old edge with these.
def splitEdges(graph, weights):
	tmp = list(graph.edges())

	# loop over all edges 
	for i in range(0,len(tmp)):
		print tmp[i]
		# for edges longer than once second. created new edges and nodes inbetween. 
		if weights[i]>1000:

			#remove the old edge
			graph.remove_edge(*tmp[i])

			# add the first of the new edges 
			graph.add_edge(tmp[i][0],str(int(tmp[i][1])+1000000))
			print tmp[i][0]
			print str(int(tmp[i][1])+1000000)

			if weights[i] > 2000:
				for j in range(0,weights[i]/1000-1):
					graph.add_edge(tmp[j][0],str(int(tmp[j][1])+j*1000000))
					print j 
					print tmp[j][0]
					print str(int(tmp[j][1])+j*1000000)

			# add the of the new edges. 
			graph.add_edge(str(int(tmp[j][1])+j*1000000),tmp[i][0])
		# for edges shorter than one second just replace the edge with one that is 1 second
		elif weights[i]<=1000:
			graph.remove_edge(tmp[i][0],tmp[i][1])
			print tmp[i][0]
			print tmp[i][1]
			graph.add_edge(tmp[i][0],tmp[i][1], weight=1000)
			print tmp[i][0]
			print tmp[i][1]

	
	return graph

def gcdOfWeighed(weights):
	greatest=gcd(weights[0],weights[1])
	for i in range(1,len(weights)):
		greatest=gcd(weights[i],greatest)
	return greatest