# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        value_list = []
        self.inOrderTraversal(root, value_list, k)
        return value_list[-1]

    def inOrderTraversal(self, node: TreeNode, value_list: List, k: int) -> None:
        if node is None or len(value_list) == k:
            return
        self.inOrderTraversal(node.left, value_list, k)
        if len(value_list) < k:
            value_list.append(node.val)
        self.inOrderTraversal(node.right, value_list, k)
        