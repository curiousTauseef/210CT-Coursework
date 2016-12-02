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
        
        Returns:
        index (int); the index of the value looking for in vertices list
        None; if a vertex with the value doesnt exist in the graph.
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
        
        if not(isinstance(weight,int)): #Checking if entered weight is an int
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
        """
        Function to print a list of all vertices in graph
        seperated by a comma.
        """
        
        vertices = "Vertices in Graph '" + str(self.name) + "' : "

        for i in range(len(self.vertices)):
            
            vertices += str(self.vertices[i].value) #Add the value to vertices string
            
            if i != len(self.vertices)-1: # If it is last vertex the no need of comma
                
                vertices += ", "
                
        print(vertices)


    def djikstra(self, startVertex):
        """
        Function to perform djikstra's algorithm on graph.
        Getting the shortest distances from a vertex to all other vertices.
        
        Parameters:
        startVertex (any data type); The starting vertex from which the shortest distances
                                   to all other vertices is to be calculated.
        
        Returns:
        distances (dictionary); the keys are the names of all vertices and its value is
                                the shortest distance from starting vertex to them.
        previous (dictionary); the key are the names of all vertices and its values is the
                               name of the previous vertex required to get to them.
        """
        
        distances = {}
        previous = {}
        Queue = queue.PriorityQueue()
        infinity = float("inf")

        #Initialization, setting starting vertex to 0 and the rest to infinity

        for vertex in self.vertices:
            
            weight = infinity
            
            if vertex.value == startVertex:
                
                weight = 0
                
            distances[vertex.value] = weight
            
            previous[vertex.value] = None

        Queue.put((0,startVertex)) # Adding the starting vertex with priority number 0 in tuple to queue

        while not (Queue.empty()):

            currentVertex = Queue.get() # Getting element with least weight
            
            currentVertex_data = currentVertex[1] #second item in tuple is the value of vertex
            
            currentVertexIndex = self.indexof(currentVertex_data)

            #relaxation step

            for edge in self.vertices[currentVertexIndex].connections: 
                
                #edge[0] is the value of the vertex connected to
                #edge[1] is the weight of the edge
                
                currentVertexDistance = distances[currentVertex_data] + edge[1] #tentative weight

                if currentVertexDistance < distances[edge[0]]:
                    
                    distances[edge[0]] = currentVertexDistance #Update the distance to get the vertex
                    
                    previous[edge[0]] = currentVertex_data #Save current vertex as last visited vertex
                    
                    Queue.put((distances[edge[0]],edge[0])) 

        return distances, previous


    def shortest_path(self, start, end):
        """
        Function which uses djikstra algorithm to return the shortest path
        and distance from two vertices in graph.
        
        Parameters:
        start (any data type); the starting vertex
        end (any data type); the destination vertex
        
        Returns;
        shortestPath(list); the list of the shortest path from start to end vertices
        distance(int); the shortest distance to get till there.
        """
        
        #Checking if the start and end vertices exist in graph
        
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
           
    
 
if __name__ == "__main__":
    
    graph1 = Graph("Graph 1")
    
    graph1.addEdge("A","B",3)
    graph1.addEdge("A","C",11)
    graph1.addEdge("A","D",5)
    graph1.addEdge("B","F",2)
    graph1.addEdge("C","E",1)
    graph1.addEdge("D","E",5)
    graph1.addEdge("D","G",6)
    graph1.addEdge("D","F",4)
    graph1.addEdge("G","H",6)
    graph1.addEdge("H","J",8)
    graph1.addEdge("I","H",9)
    graph1.addEdge("I","K",12)
    graph1.addEdge("F","I",3)
    
    path, distance = graph1.shortest_path("A","K")
    
    print(path,distance)
    
    
    
