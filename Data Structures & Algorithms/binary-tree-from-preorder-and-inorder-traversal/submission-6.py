# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preorder_index = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {}
        for i, val in enumerate(inorder):
            inorder_index_map[val] = i

        return self.buildSubTree(0, len(inorder) - 1, inorder_index_map, preorder, inorder)
        
    def buildSubTree(self, left: int, right: int, inorder_index_map: dict, preorder: List[int], inorder: List[int]) -> TreeNode:
        if left > right:
            return None

        node_val = preorder[self.preorder_index]
        inorder_index = inorder_index_map[node_val]
        node = TreeNode(node_val)

        self.preorder_index += 1

        node.left = self.buildSubTree(left, inorder_index - 1, inorder_index_map, preorder, inorder)
        node.right = self.buildSubTree(inorder_index + 1, right, inorder_index_map, preorder, inorder)

        return node
            
        