# Python program to remove all half nodes
'''
output
Inorder traversal of given tree
7 1 6 11 2 5 4 9 
Inorder traversal of the modified tree
1 6 11 2 4
'''


class Node:
    # Constructor for creating a new node
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print root.data,
        printInorder(root.right)



def removeHalfNodes(root):
    if root is None:
        return None
    #Recur to left tree
    root.left=removeHalfNodes(root.left)
    #Recur right tree
    root.right=removeHalfNodes(root.right)

    # if both left and right child is None , its not a half node
    if root.left is None and root.right is None:
        return root

    #If current nodes is a half node with left child None then it's right child is returned and   
    # replaces it in the given tree
    if root.left is None:
        new_root=root.right
        temp=root
        root=None
        del(temp)
        return new_root

    #If current nodes is a half node with right child None then it's left child is returned and   
    # replaces it in the given tree
    if root.right is None:
        new_root=root.left
        temp=root
        root=None
        del(temp)
        return new_root
    
    return root
#Main program
root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)
 
print "Inorder traversal of given tree"
printInorder(root)
 
newRoot = removeHalfNodes(root)
 
print "\nInorder traversal of the modified tree"
printInorder(newRoot)
    
    
