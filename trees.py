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

    
    def postorder(self, root):
        if not root:
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)
    
    def diameterOfBinaryTree(root):
        diameter = 0
        
        def height(node):
            nonlocal diameter
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        height(root)
        return diameter
    

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    def isBalanced(root):
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            
            right = check(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1     
            return 1 + max(left, right)
        
        return check(root) != -1

    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        remaining = targetSum - root.val

        return (self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining))

    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if not node:
                return
            
            path.append(node.val)

            if not node.left and node.right:
                if remaining == node.val:
                    result.append(path[:])
            else:
                dfs(node.left, remaining - node.val, path)    
                dfs(node.right, remaining - node.val, path)    
            
            path.pop()
        
        dfs(root, targetSum, [])
        return result







root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)