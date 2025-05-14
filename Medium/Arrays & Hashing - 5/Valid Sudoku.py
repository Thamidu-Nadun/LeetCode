from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def box(col_list):
            col_dic = dict()
            for i in col_list:
                if i=='.':
                    continue
                if i in col_dic:
                    col_dic[i]+=1
                    return False
                else:
                    col_dic[i] = 1
            return True
 
        def boxValid(board):
            main_list = []

            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    new_list = []
                    for i in range(3):
                        for j in range(3):
                            new_list.append(board[box_row + i][box_col + j])
                    main_list.append(new_list)

            for i in main_list:
                if box(i)==False:
                    return False
            return True
    
        def validCol(board):
            for i in board:
                if col(i)==False:
                    return False
            return True
    
        def col(col_list):
            col_dic = dict()
            for i in col_list:
                if i=='.':
                    continue
                if i in col_dic:
                    col_dic[i]+=1
                    return False
                else:
                    col_dic[i] = 1
            return True

        def row(row_list):
            row_dic = dict()
            for i in row_list:
                if i=='.':
                    continue
                if i in row_dic:
                    row_dic[i]+=1
                    return False
                else:
                    row_dic[i] = 1
            return True
        def validRow(board):
            for i in board:
                if row(i)==False:
                    return False
            return True

        _col = 0
        row_len = 9
        col_list = []
        for _row in range(9):
            l = []
            for i in range(row_len):
                l.append(board[i][_col])
            col_list.append(list(l))
            _col+=1

        if boxValid(board)==False:
            return False
        elif validCol(col_list)==False:
            return False
        elif validRow(board)==False:
            return False
        else:
            return True
        