class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        rows = len(board)
        columns = len(board[1]) 

        for r in range(rows):
            for c in range(columns):
                num = board[r][c]
                if num.isdigit():
                    row_state = ("row", num, r)
                    column_state = ("column", num, c)
                    box_state = ("box", num, (r//3, c//3))
                    if row_state in seen or column_state in seen or box_state in seen:
                        return False
                    else:
                        seen.add(row_state)
                        seen.add(column_state)
                        seen.add(box_state)
        
        return True