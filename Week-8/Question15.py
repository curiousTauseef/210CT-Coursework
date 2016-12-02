"""
    210CT - Programming, Algorithms and Data Structures.
    Question15.py
    Purpose:  Implement Dijkstra’s algorithm for a weighted graph data structure.
             
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 02/12/16
    
"""

import queue

class Vertex(object):

    def __init__(self, value):
        """
        Initialize the vertex object.
        value is the value to be assigned this vertex.
        connections is the list of all edges associated.
        """
        
        self.value = value
        self.connections = []

    def connect(self,connection,weight):
        """ 
        Function to add a weighted edge between this vertex and another vertex.
        Add a list [connection,weight] to connections list of this vertex.
        
        Parameters:
            connection (string); the value of vertex which is to be connected
            weight (int); the value of the weight for this edge
        """
        
        if connection in self.connections: # To avoid duplicate values
            pass 
        
        else: # If its not a repeating value then add to connections
            
            self.connections.append([connection,weight])
            self.connections = sorted(self.connections)

class Graph():

    def __init__(self,name):
        """
        Initialize the Graph object.
        name is the name of the graph.
        vertices is the list of all vertex objects in this graph.
        """
        
        self.vertices = []
        self.name= name

    def addVertex(self,value):
        """
        Function to add a new vertex object with value into list of vertices in graph.
        
        Parameters:
        value (any data type); the value with which a vertex object will be created
        """
        
        self.vertices.append(Vertex(value)) 

    def contains(self,value):
        """ 
        Function to check if a particular vertex is in the graph.
        
        Parameters:
        value (any data type); the value to look for in the graph.
        
        Returns:
        A boolean; True if a vertex with 'value' exists, else false.
        """
        
        for vertex in self.vertices:
            
            if vertex.value == value:
                
                return True
            
        return False
            
    def indexof(self, value):
        """
        Function to return the index of a particular value in list of 
        vertex objects in the graph.
        
        Parameters:
        value (any data type); the value for which you want the index.
        """
        
        index = 0
        
        for vertex in self.vertices:
            
            if vertex.value == value:
                
                return index
            
            index += 1
            

    def addEdge(self,u,v,weight=0):
        """
        Function to add an edge with a weight between two vertrices.
        
        Parameters:
        u (any data type): the value of first vertex to connect
        v (any data type): the value of second vertex to connect
        weight (int): the weight of the edge. By default it is 0.
        """
        
        if not(isinstance(weight,int): #Checking if entered weight is an int
               print("Error: The weight of an edge has to be an integer. Please try again.")
               return
        
        if not self.contains(u): #If the first vertex u doesnt exist in graph
            self.addVertex(u)
            
        if not self.contains(v): #If second vertex v doesnt exist in graph
            self.addVertex(v)
        
        uIndex = self.indexof(u)
        vIndex = self.indexof(v)
        
        self.vertices[uIndex].connect(v,weight) # Adding v to connections list of vertex u
        self.vertices[vIndex].connect(u,weight) # Adding u to connections list of vertex v


    def printGraph(self):
        """
        Function to print the vertices and its weights edges.
        Each edge is a list with two values; [vertex value, weight]
        Adjacency list of each vertex is is a list of edges associated with it.
        """
        print("Vertex" + "|".center(3) + "Adjacency List")
        print("-"*7 + "|" + "-"*18)
               
        for vertex in self.vertices:
            
            print(str(vertex.value) + " "*5 + "|".center(3) + str(vertex.connections))
            
               
    def printVertices(self):
        

        vertices = "Vertices in Graph '" + str(self.name) + "' : "

        for i in range(len(self.vertices)):
            vertices += str(self.vertices[i].value)
            if i != len(self.vertices)-1:
                vertices += ", "
                
        print(vertices)


    def djikstra(self, startNode):

        distances = {}
        previous = {}
        q = queue.PriorityQueue()
        start_weight = float("inf")

        #Initialization

        for vertex in self.vertices:
            weight = start_weight
            if vertex.value == startNode:
                weight = 0
            distances[vertex.value] = weight
            previous[vertex.value] = None

        q.put((0,startNode))

        while not (q.empty()):

            currentVertex = q.get()
            currentVertex_data = currentVertex[1]
            currentVertexIndex = self.indexof(currentVertex_data)

            #relaxation step

            for edge in self.vertices[currentVertexIndex].connections:
                currentVertexDistance = distances[currentVertex_data] + edge[1]

                if currentVertexDistance < distances[edge[0]]:
                    distances[edge[0]] = currentVertexDistance
                    previous[edge[0]] = currentVertex_data
                    q.put((distances[edge[0]],edge[0]))

        return distances, previous


    def shortest_path(self, start, end):

        if not(self.contains(start)):
            print("Error: Vertex '"+str(start)+"' does not exist in the graph '"+str(self.name)+"'. Please try again")
            return
        elif not(self.contains(end)):
            print("Error: Vertex '"+str(end)+"' does not exist in the graph '"+str(self.name)+"'. Please try again")
            return

        distances, previous = self.djikstra(start)
        
        shortestPath = []
        final = end

        while final is not None:
            shortestPath.insert(0,final)
            final = previous[final]

        return shortestPath, distances[end]
           
    
 
testg = Graph("random")

testg.addEdge("a","b",2)
testg.addEdge("a","c",8)
testg.addEdge("b","c",1)
testg.addEdge("c","e",3)
testg.addEdge("a","d",5)
testg.addEdge("d","e",4)


path1, distances1 = testg.shortest_path("a","e")
print(path1,distances1)

test2 = Graph("lol")
test2.addEdge(1,2,3)
test2.addEdge(1,4,2)
test2.addEdge(1,3,4)
test2.addEdge(2,5,2)
test2.addEdge(2,3,4)
test2.addEdge(3,5,6)
test2.addEdge(5,4,1)
test2.addEdge(5,6,2)
test2.addEdge(4,6,4)
test2.printGraph()
test2.printVertices()

path2, distance2 = test2.shortest_path(1,6)
print(path2,distance2)
