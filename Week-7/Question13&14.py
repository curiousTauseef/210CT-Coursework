"""
    210CT - Programming, Algorithms and Data Structures.
    Question13&14.py
    Purpose:  Implement unweighted graph data structure with depth first search
              and breadth first search traversals.
             
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 02/12/16
    
"""

class Vertex(object):

    def __init__(self, value):
        """
        Initialize the vertex object.
        value is the value to be assigned this vertex.
        connections is the list of all edges associated.
        """
        
        self.value = value
        
        self.connections = []

    def connect(self,connection):
        """ 
        Function to add an edge between this vertex and another vertex.
        Add connection to connections list of this vertex.
        
        Parameters:
            connection (string); the value of vertex which is to be connected
        """

        if connection in self.connections: # To avoid duplicate values
            pass
        
        else: # If its not a repeating value then add to connections
            
            self.connections.append(connection)
            
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

    def getVertex(self, value):
        """
        Function to return vertex object with value from list of vertices in graph.
        
        Parameters:
        value (any data type); the value to look for in graph vertices.
        
        Returns:
        Vertex Object with a value passed as argument.
        """
        
        return self.vertices[self.indexof(value)]

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

    def addEdge(self,u,v):
        """
        Function to add an edge with a weight between two vertrices.
        
        Parameters:
        u (any data type): the value of first vertex to connect
        v (any data type): the value of second vertex to connect
        """
        
        if not self.contains(u): #If the first vertex u doesnt exist in graph
            
            self.addVertex(u)
            
        if not self.contains(v): #If the second vertex v doesnt exist in graph
            
            self.addVertex(v)
        
        uIndex = self.indexof(u)
        vIndex = self.indexof(v)
        
        self.vertices[uIndex].connect(v) # Adding v to connections list of vertex u
        self.vertices[vIndex].connect(u) # Adding u to connections list of vertex v
        

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
            
        return ""

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
        

    def dfs(self, v):
        """
        Function to perform depth first search traversal.
        Results are saved into 'Traversal Results.txt'
        
        Parameters:
        v (any data type); the starting vertex to perform depth first search traversal.
        """

        if not(self.contains(v)): #Checking if v exists in graph
            print("DFS Error: Vertex '"+str(v)+"' does not exist in '"+str(self.name)+"' graph. Please try again.")
            return
            
        stack = []
        visited = []
        stack.append(self.getVertex(v)) #Adding starting vertex to stack

        while not (len(stack)==0):
            
            currentVertex = stack.pop()
            
            if currentVertex.value not in visited:
                
                visited.append(currentVertex.value)

                for edge in currentVertex.connections[::-1]: # Reversing connections lists to perform traversal in ascending order
                    
                    stack.append(self.getVertex(edge))
                    
        self.saveTraversal(visited,"bfs")
        
        print("DFS Traversal Results starting at vertex '"+str(v)+"' of graph '"+str(self.name)+"' are saved to 'Traversal Results.txt' file.")
    

    def bfs(self, v):
        """
        Function to perform breadth first search traversal.
        Results are saved into 'Traversal Results.txt'
        
        Parameters:
        v (any data type); the starting vertex to perform breadth first search traversal.
        """

        if not(self.contains(v)): #Checking if v exists in graph
            print("BFS Error: Vertex '"+str(v)+"' does not exist in '"+str(self.name)+"' graph. Please try again.")
            return

        queue = []
        visited = []
        queue.append(self.getVertex(v)) #Adding starting vertex to queue
        
        while not (len(queue)==0):
            
            currentVertex = queue.pop()
            
            if currentVertex.value not in visited:
                
                visited.append(currentVertex.value)
                
                for edge in currentVertex.connections:
                    
                    queue.insert(0,self.getVertex(edge))
                    
        self.saveTraversal(visited,"bfs") #Saving the results to 'Traversal Results.txt' file'
        
        print("BFS Traversal Results starting at vertex '"+str(v)+"' of graph '"+str(self.name)+"' are saved to 'Traversal Results.txt' file.")
    

    def saveTraversal(self,arr,traversal):
        """
        Function to write the traversal results into 'Traversal Results.txt' file
        
        Parameters:
        arr (list); the list which contains results of the traversal
        traversal (string); the type of traversal "bfs" or "dfs"
        """
        
        try: #Checking if the file exists
            file = open("Traversal Results.txt","r")
            file.close()
        except FileNotFoundError: #If it doesnt create a new file
            file = open("Traversal Results.txt","w")
            file.close

        if traversal == "dfs":
            title = "Depth first search starting at vertex '"+str(arr[0])+"' of graph '"+str(self.name) + "' :"
        else:
            title = "Breadth first search starting at vertex '"+str(arr[0])+"' of graph '"+str(self.name) + "' :"

        file = open("Traversal Results.txt","a")

        resultsString = ""
        
        for i in range(len(arr)):
            
            resultsString += str(arr[i]) #Add the value to results string
            
            if i != len(arr) - 1: # If it is last vertex the no need of comma
                resultsString += ", "

        file.write(title)
        file.write("\n")
        file.write(resultsString)
        file.write("\n \n")
        file.close()
        
                    

if __name__ == "__main__":
    
    graph1 = Graph("Graph 1")
    
    graph1.addEdge("A","B")
    graph2.addEdge("A","C")
    graph1.addEdge("A","D")
    graph1.addEdge("B","F")
    graph1.addEdge("C","E")
    graph1.addEdge("D","E")
    graph1.addEdge("D","G")
    graph1.addEdge("D","F")
    graph1.addEdge("G","H")
    graph1.addEdge("H","J")
    graph1.addEdge("I","H")
    graph1.addEdge("I","K")
    graph1.addEdge("F","I")
    
    graph1.dfs("Z")
    graph1.dfs("A")
    graph1.bfs("A")
    
    graph1.printGraph()
    graph1.printVertices()
               
    

