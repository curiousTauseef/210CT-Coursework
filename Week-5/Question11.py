class Node():

    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class doubleLinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,node,data):

        insertingNode = Node(data)

        if node != None: #If it is not the first element
            
            insertingNode.next = node.next
            node.next = insertingNode
            insertingNode.prev = node

            if insertingNode.next != None:
                insertingNode.next.prev = insertingNode

        if self.head == None: #If it is an empty list
            
            self.head = self.tail = insertingNode 
            
            insertingNode.prev = insertingNode.next = None 

        elif self.tail == node:
            
            self.tail = insertingNode
            

    def getNode(self,data):
        
        currentNode = self.head
        
        if currentNode != None:
                
            while currentNode.next != None:
                
                if (currentNode.value == data):
                    
                    return currentNode
            
                currentNode = currentNode.next
                
            if currentNode.value == data:
                
                    return currentNode
                
        return None
                
    
    def remove(self, data):

        deletingNode = self.getNode(data)

        if deletingNode == None:
            print(str(data) + " is not deleted because it does not exist in the list.")
            return

        if deletingNode.prev != None: #If deletingNode is not the first element in list
            
            deletingNode.prev.next = deletingNode.next
            
        else: #If deletingNode is  the lfirst element in list
            
            self.head = deletingNode.next

        if deletingNode.next != None: #If deletingNode is not the last element in list
            
            deletingNode.next.prev = deletingNode.prev
            
        else: #If deletingNode is  the last element in list
            self.tail = deletingNode.prev


    def display(self):
        values = []
        node = self.head
        while node != None:
            values.append(str(node.value))
            node = node.next
        print("List: ",",".join(values))



l = doubleLinkedList()
l.insert(None, 4)
l.insert(l.head,6)
l.insert(l.head,8)

l.insert(l.head,9)
l.insert(l.head,9)
l.remove(10)
l.display()
l.remove(9)
l.display()
