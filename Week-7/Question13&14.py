class Vertex(object):

    def __init__(self, value):
        self.value = value
        self.connections = []

    def value(self):
        return self.value

    def connect(self,connection):

        if connection in self.connections:
            pass
        else:
            self.connections.append(connection)
            self.connections = sorted(self.connections)
            

class Graph():

    def __init__(self,name):
        
        self.vertices = []
        self.name= name

    def addVertex(self,value):
        self.vertices.append(Vertex(value))

    def getVertex(self, value):
        return self.vertices[self.indexof(value)]

    def contains(self,value):
        for vertex in self.vertices:
            if vertex.value == value:
                return True
            
        return False
            
    def indexof(self, value):
        index = 0
        for vertex in self.vertices:
            if vertex.value == value:
                return index
            index += 1

    def addEdge(self,u,v):
        
        if not self.contains(u):
            self.addVertex(u)
            
        if not self.contains(v):
            self.addVertex(v)
        
        uIndex = self.indexof(u)
        vIndex = self.indexof(v)
        
        self.vertices[uIndex].connect(v)
        self.vertices[vIndex].connect(u)
        

    def printGraph(self):
        print("Vertex" + "|".center(3) + "Adjacency List")
        print("-"*7 + "|" + "-"*18)
        for vertex in self.vertices:
            print(str(vertex.value) + " "*5 + "|".center(3) + str(vertex.connections))
            
        return ""

    def printVertices(self):

        vertices = "Vertices in Graph '" + str(self.name) + "' : "

        for i in range(len(self.vertices)):
            vertices += str(self.vertices[i].value)
            if i != len(self.vertices)-1:
                vertices += ", "
                
        print( vertices)
        return ""

    def dfs(self, v):
        
        stack = []
        visited = []
        stack.append(self.getVertex(v))

        while not (len(stack)==0):
            
            currentVertex = stack.pop()
            if currentVertex.value not in visited:
                visited.append(currentVertex.value)

                for edge in currentVertex.connections[::-1]:
                    stack.append(self.getVertex(edge))
                    
        return visited
    

    def bfs(self, v):

        queue = []
        visited = []
        queue.append(self.getVertex(v))
        
        while not (len(queue)==0):
            currentVertex = queue.pop()
            if currentVertex.value not in visited:
                visited.append(currentVertex.value)
                for edge in currentVertex.connections:
                    queue.insert(0,self.getVertex(edge))
                    
        return visited
                    
    
    
def saveTraversal(graphname,arr,traversal):

    if traversal == "dfs":
        title = "Depth first search of graph '"+str(graphname) + "' :"
    else:
        title = "Breadth first search of graph '"+str(graphname) + "' :"

    file = open("Traversal Results.txt","w")

    resultsString = ""
    for i in range(len(arr)):
        resultsString += str(arr[i])
        if i != len(arr) - 1:
            resultsString += ", "

    file.write(title)
    file.write(resultsString)
    file.write("\n")
    file.close()
   
    
testg = Graph("Test Graph")
test2 = Graph("N")
testg.addEdge("A","B")
testg.addEdge("A","S")
testg.addEdge("S","C")
testg.addEdge("S","G")
testg.addEdge("G","F")
testg.addEdge("G","H")
testg.addEdge("H","E")
testg.addEdge("E","C")
testg.addEdge("F","C")
testg.addEdge("C","D")

print(testg.dfs("A"))
print(testg.bfs("A"))

testg.printGraph()
testg.printVertices()

test2.addEdge("A","B")
test2.addEdge("A","D")
test2.addEdge("A","G")
test2.addEdge("E","B")
test2.addEdge("E","G")
test2.addEdge("B","F")
test2.addEdge("F","D")
test2.addEdge("F","C")
test2.addEdge("C","H")

print(test2.dfs("A"))
print(test2.bfs("A"))
