# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -math.inf, math.inf)

    def dfs(self, node: TreeNode, lower_bound: int, upper_bound: int) -> bool:
        if node is None:
            return True
        if node.val <= lower_bound or node.val >= upper_bound:
            return False

        return self.dfs(node.left, lower_bound, node.val) and self.dfs(node.right, node.val, upper_bound)
        
        