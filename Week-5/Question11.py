"""
    210CT - Programming, Algorithms and Data Structures.
    Question11.py
    Purpose:  Implement the double linked list node delete function.
             
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 02/12/16
    
"""


class Node():

    def __init__(self,value):
        """
        Initialize the Node object.
        value is the value to be assigned this node.
        next stores the node object after this node.
        prev stores the node object before this node.
        """
        
        self.value = value
        self.next = None
        self.prev = None

class doubleLinkedList():
    
    def __init__(self):
        """
        Initialize the Double Linked List object.
        head stores the first node object in the list.
        tail stores the last node object in the list.
        """
        self.head = None
        self.tail = None

    def insert(self,node,data):
        """
        Function to add a new node object with data into linked list.
        
        Parameters:
        node (Node) ; the node you want to insert a new node after.
        data (any data type); the data with which a new node object will be created
        """
            
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

        elif self.tail == node: #If node is the last object
            
            self.tail = insertingNode
            

    def getNode(self,data):
        """
        Function which searchs linked list and returns a node object which contains 'data'
        
        Parameters:
        data (any data type); the data of a node looking for
        """
        
        currentNode = self.head
        
        if currentNode != None:
                
            while currentNode.next != None:
                
                if (currentNode.value == data):
                    
                    return currentNode
            
                currentNode = currentNode.next
                
            if currentNode.value == data: #In case, currentNode is or first element last element in list
                
                    return currentNode
                
        return None
                
    
    def remove(self, data):
        
        """
        Function which removes a node with 'data' in linked list.
        
        Parameters:
        data (any data type); the data of a node to be removed.
        """

        deletingNode = self.getNode(data)

        if deletingNode == None: # If node to delete does not exist
            print(str(data) + " is not deleted because it does not exist in the list.")
            return

        if deletingNode.prev != None: #If deletingNode is not the first element in list
            
            deletingNode.prev.next = deletingNode.next
            
        else: #If deletingNode is  the first element in list
            
            self.head = deletingNode.next

        if deletingNode.next != None: #If deletingNode is not the last element in list
            
            deletingNode.next.prev = deletingNode.prev
            
        else: #If deletingNode is  the last element in list
            self.tail = deletingNode.prev


    def display(self):
        """
        Function to print all the elements in linked list.
        """
        values = []
        node = self.head
        while node != None:
            values.append(str(node.value))
            node = node.next
        print("List: ",",".join(values))


if __name__ == "__main__":
    
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
