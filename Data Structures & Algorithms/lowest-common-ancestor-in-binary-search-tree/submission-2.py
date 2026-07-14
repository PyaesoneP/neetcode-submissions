# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Any
class Solution:
    def __init__(self):
        self.parents = set()
        self.common_ancestor = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent = None
        self.dfs(parent, root, p)
        self.dfs(parent, root, q)
        return self.common_ancestor
        

    def dfs(self, parent: TreeNode, node: TreeNode, target: TreeNode) -> None:
        if node in self.parents:
            self.common_ancestor = node
        if node not in self.parents:
            self.parents.add(node)

        if node.val == target.val:
            return
        elif target.val < node.val:
            return self.dfs(node, node.left, target)
        else:
            return self.dfs(node, node.right, target)