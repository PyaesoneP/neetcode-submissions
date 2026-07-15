# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            current_sum = node.val + max(self.maxSum(node.left), 0) + max(self.maxSum(node.right), 0)
            max_sum = max(max_sum, current_sum)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return max_sum

    def maxSum(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return max(node.val + max(self.maxSum(node.left), self.maxSum(node.right)), 0)
        