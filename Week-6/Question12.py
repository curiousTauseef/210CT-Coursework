class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
        
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree


def in_order(tree):
    sortedArr = []
    currentNode = tree
    stack = []
    loopRunning = True

    while loopRunning:

        if currentNode != None:
            stack.append(currentNode)
            currentNode = currentNode.left

        else:
            if (len(stack) > 0):
                currentNode = stack.pop()
                sortedArr.append(currentNode.value)
                currentNode = currentNode.right
                
            else:
                
                loopRunning = False

    return sortedArr


def treeSort(arr):
    tree = tree_insert(None,arr[0])
    for i in range(1,len(arr)):
        tree_insert(tree,arr[i])

    sortedArr = in_order(tree)

    return sortedArr
