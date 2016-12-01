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

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)

def in_order(tree):
    inOrder = []        #Creating a Stack
    end = False
    while(not end):     #run while end is true
        if tree != None:    #tree is not empty
            inOrder.append(tree) #add tree into in order
            tree = tree.left    #tree equals to the left side of the tree

        else:
            if(len(inOrder) > 0 ):  #in order length is greater than zero
                tree = inOrder.pop() #tree equals empty list of in order
                print(tree.value)   #printing each tree value
                tree = tree.right   #go to the right side of the tree
            else:
                break               #break out of the loop
            
        

##def in_order(tree):
##    if(tree.left!=None):
##        in_order(tree.left)
##    print (tree.value)
##    if(tree.right!=None):
##        in_order(tree.right)

if __name__ == '__main__':
    
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
