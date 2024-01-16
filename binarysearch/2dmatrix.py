class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows * cols - 1

        while left <= right:
            midpoint = left + ((right - left) // 2)
            mid_row, mid_col = divmod(midpoint, cols)

            if matrix[mid_row][mid_col] > target:
                right = midpoint - 1
            elif matrix[mid_row][mid_col] < target:
                left = midpoint + 1
            else:
                return True
        return False

