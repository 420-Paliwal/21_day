class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        print(self.val)
        self.inorder(root.left)