"""
    210CT - Programming, Algorithms and Data Structures.
    Question12.py
    Purpose: Implement TREE_SORT algorithm.
             
    Author : Rithin Chalumuri
    Version: 1.0 
    Date   : 02/12/16
    
"""


class BinTreeNode(object):
 
    def __init__(self, value):
        """
        Initialize the BinaryNode object.
        value is the value to be assigned this node.
        left stores the node object lesser than this node.
        right stores the node object higher than this node.
        """
        self.value=value
        self.left=None
        self.right=None
 
        
def tree_insert( tree, item):
    """
    Function to add a new BinTreeNode object with data into binary tree.
        
    Parameters:
        tree (BinTreeNode) ; the tree node in which you want to insert
        item (int); the data with which a new node object will be created
    """
    
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None): #If there is nothing on the left side
                tree.left=BinTreeNode(item)
            else: 
                tree_insert(tree.left,item)
        else:
            if(tree.right==None): #If there is nothing on the right side
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
                
    return tree


def in_order(tree):
    """
    Function to which performs inorder for a tree iteratively.
        
    Parameters:
        tree (BinTreeNode) ; the tree for which inorder is to be performed.
    
    Returns:
        sortedArr (list); list of all elements in ascending order.
    """
    
    sortedArr = []
    currentNode = tree
    stack = []
    loopRunning = True

    while loopRunning:

        if currentNode != None:
            stack.append(currentNode)
            currentNode = currentNode.left   #Keep going till the last left element of the tree

        else:
            if (len(stack) > 0): #If there are any pending nodes to visit
                currentNode = stack.pop()
                sortedArr.append(currentNode.value)
                currentNode = currentNode.right
                
            else:
                
                loopRunning = False

    return sortedArr


def treeSort(arr):
    """
    Function which sorts a sequence using tree sort algorithm.
    
    Parameters:
        arr(list); the sequence to be sorted.
        
    Returns:
        sortedArr (list); a sorted sequence in ascending order.
    """
    
    if not(isinstance(arr,list)): #If sequence of unsupported type is passed
        print("Error: Please enter a valid array and try again.")
        return
    
    tree = tree_insert(None,arr[0]) #First Element
    
    for i in range(1,len(arr)):
        tree_insert(tree,arr[i]) #Appened all elements into tree

    sortedArr = in_order(tree)

    return sortedArr

if __name__ == "__main__":
    
    arr = [1,55,2,54,1,3,687,32,57,1]
    sortedArr = (treeSort(arr))
    print(sortedArr)
