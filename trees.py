class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        print(val)
        self.inorder(root.left)

    def height_of_tree(self, root):
        if not root:
            return 0
        
        left_height = self.height_of_tree(root.left)
        right_height = self.height_of_tree(root.right)

        return 1+ max(left_height, right_height)
    
    def preorder(self, root):
        if not root:
            return
        
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    

    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)