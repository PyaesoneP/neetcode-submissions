class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom = 0
        top = len(matrix) - 1
        target_row = 0
        while bottom <= top:
            target_row = (top + bottom) // 2
            if matrix[target_row][-1] < target:
                bottom = target_row + 1
            elif matrix[target_row][0] > target:
                top = target_row - 1
            else:
                break
        
        l = 0
        r = len(matrix[target_row]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[target_row][m] == target:
                return True
            elif matrix[target_row][m] < target:
                l = m + 1
            elif matrix[target_row][m] > target:
                r = m - 1

        return False