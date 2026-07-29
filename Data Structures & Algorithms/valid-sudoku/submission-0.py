from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for row in board:
            nums = [x for x in row if x != "."]
            if len(nums) != len(set(nums)):
                return False

        # Check columns
        for col in range(9):
            nums = []
            for row in range(9):
                if board[row][col] != ".":
                    nums.append(board[row][col])

            if len(nums) != len(set(nums)):
                return False

        # Check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                nums = []

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != ".":
                            nums.append(board[i][j])

                if len(nums) != len(set(nums)):
                    return False

        return True