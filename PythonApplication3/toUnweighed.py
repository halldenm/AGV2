from fractions import gcd

# Make the graph unweighed
def weightToUnweight(graph):
	weights= getWeights(graph)
	gcdOfWeighed(weights)
	graph=splitEdges(graph,weights)
	#add the new edges to the grahp
	return graph

# returns the weights of all edges rounded UP to nearest 1000ms
def getWeights(graph):
	weights=list()
	weightsTmp = list(graph.edges(data='weight'))
	for i, line in enumerate(weightsTmp):
		if weightsTmp[i][2]%1000 == 0:
			weights.append(weightsTmp[i][2])
		elif weightsTmp[i][2]%1000 >500:
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
		newEdges = [] # temp variable for the new edges
		# for edges longer than once second. created new edges and nodes inbetween. 
		if weights[i]>1000:

			#remove the old edge
			graph.remove_edge(*tmp[i])

			# add the first of the new edges 
			#graph.add_edge(tmp[i][0],str(int(tmp[i][1])+1000000))

			newEdges.append((str(tmp[i][0]), str(int(tmp[i][1])+1000000)))
			print newEdges

			if weights[i] > 2000:
				
				for j in range(1,weights[i]/1000-1):
					
					newEdges.append((newEdges[j-1][1], str(int(newEdges[j-1][1])+1000000+int(tmp[i][1])*100000)))
					print str(int(newEdges[j-1][1])+1000000+int(tmp[i][1])*100000)
					print tmp[j-1][1]
					#,'weight=1000'))
 					print newEdges

				newEdges.append((newEdges[j][1], tmp[i][1]))#,'weight=1000'))
				print newEdges
				

			else: 
				newEdges.append((newEdges[i-1][1],str( tmp[i][1]))) #,'weight=1000'))
				print newEdges

			for k in range(0,len(newEdges)):
				graph.add_edge(*newEdges[k],weight=1000)

		else:
			graph.remove_edge(*tmp[i])
			graph.add_edge(*tmp[i],weight=1000)
		


			
			
			

		
		
	return graph

def gcdOfWeighed(weights):
	greatest=gcd(weights[0],weights[1])
	for i in range(1,len(weights)):
		greatest=gcd(weights[i],greatest)
	return greatest