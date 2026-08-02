class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix[0])
        col_len = len(matrix)
        l, r  = 0, row_len * col_len - 1

        while l <= r:
            mid = (l + r) // 2
            x = mid % row_len
            y = mid // row_len

            if matrix[y][x] > target:
                r = mid - 1
            elif matrix[y][x] < target:
                l = mid + 1
            else:
                return True

        return False