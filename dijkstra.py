def dijkstra(g,start):

	X = [] #Vertex processed so far
	A = {} #Compute shortest distance
	B = {} #Compute shortest path
	X.append(start)
	A[start] = 0
	B[start] = start
	myDict = {}

	#Digkstra
	while len(X) < len(g):
		#Finding the neighbor with minimum distance
		for v in X:
			temp = {A[v]+g[v][neighbor]: [neighbor,v] for neighbor in g[v].keys() if neighbor not in X}
			if temp != {}:
				myDict[min(temp)] = temp[min(temp)]
	
		#Adding neighbor to Visited list (X)
		X.append(myDict[min(myDict)][0])
		#Assigning the minimum distance
		A[myDict[min(myDict)][0]] = min(myDict)
		#Assigning the minimum path
		B[myDict[min(myDict)][0]] = myDict[min(myDict)][1]
		myDict = {}
	
	return A,B
