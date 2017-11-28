from fractions import gcd

# Make the graph unweighed
def weightToUnweight(graph):
	weights= getWeights(graph)
	gcdOfWeighed(weights)
	#extrakt min weight
	#split all edges 
	splitEdges(graph)
	#add the new edges to the grahp

def getWeights(graph):
	weights=list()
	weightsTmp = list(graph.edges(data='weight'))
	for i, line in enumerate(weightsTmp):
		weights.append(weightsTmp[i][2])
	return weights

def gcdOfWeighed(weights):
	greatest=gcd(weights[0],weights[1])
	for i in range(1,len(weights)):
		greatest=gcd(weights[i],greatest)
	return greatest