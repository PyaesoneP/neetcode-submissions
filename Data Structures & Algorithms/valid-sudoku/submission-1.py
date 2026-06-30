from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid = defaultdict(set)
        column_dict = defaultdict(set)
        index_to_grid = {
            0 : '1',
            1 : '1',
            2 : '1',
            3 : '2',
            4 : '2',
            5 : '2',
            6 : '3',
            7 : '3',
            8 : '3'
        }
        for i, row in enumerate(board):
            seen = set()
            for j, column in enumerate(row):
                if column in seen:
                    return False
                elif column.isalnum():
                    seen.add(column)
                a=index_to_grid[i]
                b=index_to_grid[j]
                if column in grid[a+b]:
                    return False
                elif column.isalnum():
                    grid[a+b].add(column)
                if column in column_dict[j]:
                    return False
                elif column.isalnum():
                    column_dict[j].add(column)
                
        return True