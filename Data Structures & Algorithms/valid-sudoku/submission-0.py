class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for row in range(9):
            check = [0] * 9

            for col in range(9):

                if board[row][col] == '.':
                    continue

                num = int(board[row][col]) - 1

                if check[num] > 0:
                    return False

                check[num] += 1

        # Check columns
        for col in range(9):
            check = [0] * 9

            for row in range(9):

                if board[row][col] == '.':
                    continue

                num = int(board[row][col]) - 1

                if check[num] > 0:
                    return False

                check[num] += 1

        # Check boxes
        for row in [0, 3, 6]:

            check1 = [0] * 9
            check2 = [0] * 9
            check3 = [0] * 9

            box = row

            while box < row + 3:

                for col in range(9):

                    # Left box
                    if col in [0, 1, 2]:

                        if board[box][col] == '.':
                            continue

                        num = int(board[box][col]) - 1

                        if check1[num] > 0:
                            return False

                        check1[num] += 1

                    # Middle box
                    elif col in [3, 4, 5]:

                        if board[box][col] == '.':
                            continue

                        num = int(board[box][col]) - 1

                        if check2[num] > 0:
                            return False

                        check2[num] += 1

                    # Right box
                    else:

                        if board[box][col] == '.':
                            continue

                        num = int(board[box][col]) - 1

                        if check3[num] > 0:
                            return False

                        check3[num] += 1

                box += 1

        # # Check 3x3 boxes
        # for startRow in [0, 3, 6]:
        #     for startCol in [0, 3, 6]:

        #         check = [0] * 9

        #         for row in range(startRow, startRow + 3):
        #             for col in range(startCol, startCol + 3):

        #                 if board[row][col] == '.':
        #                     continue

        #                 num = int(board[row][col]) - 1

        #                 if check[num] > 0:
        #                     return False

        #                 check[num] += 1
        

        return True