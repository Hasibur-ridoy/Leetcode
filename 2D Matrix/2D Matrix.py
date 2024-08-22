from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # ROW is the number of rows in the matrix and COLS is the number of columns in the matrix
        ROW, COLS = len(matrix), len(matrix[0])
        # setting up pointer in the matrix for finding the correct row
        top, bot = 0, ROW - 1

        while top <= bot:

            #finding the correct row that contains the target value
            row = top + ((bot - top) // 2)

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        # if the top crosses the bot pointer it means there was no correct row found
        if not (top <= bot):
            return False

        # 2nd binary search O(log n)

        row = top + ((bot - top) // 2)
        l,r = 0, COLS - 1

        while l <= r:
            m = l + ((r-l) // 2)

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
