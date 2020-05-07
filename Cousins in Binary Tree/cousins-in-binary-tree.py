# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec_traverse(self, root: TreeNode, target, depth=0):
        result = (-1,-1)
        if(root):
            depth+=1
            if(root.left):
                if(root.left.val == target):
                    result = (root.val, depth)
                else:
                    result = self.rec_traverse(root.left, target, depth)
            if(root.right and result == (-1,-1)):
                if(root.right.val == target):
                    result = (root.val, depth)
                else:
                    result = self.rec_traverse(root.right, target, depth)
        return result

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if(not root):
            return false
        (left_parent, left_depth) = self.rec_traverse(root, x)
        print(left_parent, left_depth)
        (right_parent, right_depth) = self.rec_traverse(root, y)
        print(right_parent, right_depth)
        if(left_parent == right_parent):
            return False
        else:
            if(left_depth == right_depth):
                return True
            else:
                return False