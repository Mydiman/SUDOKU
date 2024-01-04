"""
.py file for generate sudoku solution only
"""



def solution():
    from random import sample
    
    
    
    """
    generate random rows, columns and numbers
    e.g. when sth is [0, 1, 2], may return [2, 0, 1] (random)
    """
    def shuffle(sth) -> list:
        return sample(sth, len(sth))
    
    
    
    """
    finding the position of a number in:
        [[0, 1, 2, 3, 4, 5, 6, 7, 8],
        [3, 4, 5, 6, 7, 8, 0, 1, 2],
        [6, 7, 8, 0, 1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6, 7, 8, 0],
        [4, 5, 6, 7, 8, 0, 1, 2, 3],
        [7, 8, 0, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 0, 1],
        [5, 6, 7, 8, 0, 1, 2, 3, 4],
        [8, 0, 1, 2, 3, 4, 5, 6, 7]]
    """
    def position(row, column):
        rBox = row % 3
        return (3 * rBox + row // 3 + column) % 9
    
    
    
    rows = []
    for i in shuffle([0, 1, 2]):
        for j in shuffle([0, 1, 2]):
            rows.append(i * 3 + j)
    
    cols = []
    for i in shuffle([0, 1, 2]):
        for j in shuffle([0, 1, 2]):
            cols.append(i * 3 + j)
    
    nums = shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    board = []
    for r in rows:
        temp = []
        for c in cols:
            temp.append(nums[position(r,c)])
        board.append(temp)
    return board
