class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m*n - 1

        while l <= r:
            mid = (l+r) // 2
            mid_row = mid // n
            mid_column = mid % n
            curr_mid = matrix[mid_row][mid_column]

            if curr_mid == target:
                return True
            elif curr_mid < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
