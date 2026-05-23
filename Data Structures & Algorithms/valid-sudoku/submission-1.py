class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        column = len(board[1])
        # seen = set()

        # check every rows
        for row in board:
            nums = [n for n in row if n.isdigit()]
            if len(nums) != len(set(nums)): return False

        # check every column
        for c in range(column):
            nums = [board[r][c] for r in range(rows) if board[r][c].isdigit()]
            if len(nums) != len(set(nums)): return False

        # check every 3x3 box
        starting_points = [(0, 0), (0, 3), (0, 6),
                           (3, 0), (3, 3), (3, 6),
                           (6, 0), (6, 3), (6, 6)]

        for r, c in starting_points:
            nums = [board[i][j] for i in range(r, r+3) for j in range(c, c+3) if board[i][j].isdigit()]
            if len(nums) != len(set(nums)): return False

        return True