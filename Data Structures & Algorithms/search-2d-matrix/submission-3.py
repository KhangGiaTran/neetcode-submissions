class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix) * len(matrix[0])
        left = 0
        right = length - 1

        while left <= right:
            mid = (left + right) // 2
            item_x = mid % len(matrix[0])
            item_y = mid // len(matrix[0])

            item = matrix[item_y][item_x]

            if target > item:
                left = mid + 1
            elif target < item:
                right = mid - 1
            else:
                return True
        return False