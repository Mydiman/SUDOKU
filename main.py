from random import randint



def new_board():
  global print_board
  new_board_solution()
  while True:
    print_board = random_sub_board(randint(41, 45))
    all_possible(board)
    """
    solve sudoku with some basic skill
    if successful ---> end new_board
    else          ---> generate random board
    """
    while True:
      past_possible = possible
      """
      if the blank which only one possible ---> fill in
      
      example ---> 1 2 3 4 5 0 0 0 A
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 6
                   0 0 0 0 0 0 0 0 7
                   0 0 0 0 0 0 0 0 8
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   
                   A ---> 9
      """
      for i in range(9):
        for j in range(9):
          count = 0
          for k in range(1, 10):
            if k in possible [i][j]:
              count += 1
          if count == 1:
            for k in range(1, 10):
              if k in possible [i][j]:
                board [i][j] = k
                possible [i][j] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                for l in range(9):
                  possible [l][j][k - 1] = 0
                  possible [i][l][k - 1] = 0
                x_box = x_to_xbox(j)
                y_box = y_to_ybox(i)
                for l in range(y_box, y_box + 3):
                  for m in range(x_box, x_box + 3):
                    possible [l][m][k - 1] = 0
      """
      if blank is the only possible num in a row ---> fill in
      
      example ---> 1 2 3 4 5 6 7 A B
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 8
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   
                   A ---> 8 since B cannot be 8
      """
      for i in range(9):
        for j in range(1, 10):
          count = 0
          for k in range(9):
            if j in possible [i][k]:
              count += 1
          if count == 1:
            for k in range(9):
              if j in possible [i][k]:
                possible [i][k] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                board [i][k] = j
                for l in range(9):
                  possible [l][k][j - 1] = 0
                  possible [i][l][j - 1] = 0
                x_box = x_to_xbox(k)
                y_box = y_to_ybox(i)
                for l in range(y_box, y_box + 3):
                  for m in range(x_box, x_box + 3):
                    possible [l][m][j - 1] = 0
      """
      if blank is the only possible num in a column ---> fill in
      
      example ---> 1 0 0 0 0 0 0 0 0
                   2 0 0 0 0 0 0 0 0
                   3 0 0 0 0 0 0 0 0
                   4 0 0 0 0 0 0 0 0
                   5 0 0 0 0 0 0 0 0
                   6 0 0 0 0 0 0 0 0
                   7 0 0 0 0 0 0 0 0
                   A 0 0 0 0 0 0 0 0
                   B 0 0 8 0 0 0 0 0
                   
                   A ---> 8 since B cannot be 8
      """
      for i in range(9):
        for j in range(1, 10):
          count = 0
          for k in range(9):
            if j in possible [k][i]:
              count += 1
          if count == 1:
            for k in range(9):
              if j in possible [k][i]:
                possible [k][i] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                board [k][i] = j
                for l in range(9):
                  possible [l][i][j - 1] = 0
                  possible [k][l][j - 1] = 0
                x_box = x_to_xbox(i)
                y_box = y_to_ybox(k)
                for l in range(y_box, y_box + 3):
                  for m in range(x_box, x_box + 3):
                    possible [l][m][j - 1] = 0
      """
      if blank is the only possible num in a box ---> fill in
      
      example ---> 1 4 7 0 0 0 0 0 0
                   2 5 A 0 0 0 0 0 0
                   3 6 B 0 0 0 0 0 8
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   
                   A ---> 8 since B cannot be 8
      """
      for i in range(9):
        for j in range(1, 10):
          count = 0
          for k in range(9):
            if j in possible [k][i]:
              count += 1
          if count == 1:
            for k in range(9):
              if j in possible [k][i]:
                possible [k][i] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                board [k][i] = j
                for l in range(9):
                  possible [l][i][j - 1] = 0
                  possible [k][l][j - 1] = 0
                x_box = x_to_xbox(i)
                y_box = y_to_ybox(k)
                for l in range(y_box, y_box + 3):
                  for m in range(x_box, x_box + 3):
                    possible [l][m][j - 1] = 0
      """
      if there is two blank having the only same two possible in a column ---> delete possible of blank not having the same two possible in a row

      example ---> 1 0 0 0 0 0 0 0 0
                   2 0 0 0 0 0 0 0 0
                   3 0 0 0 0 0 0 0 0
                   4 0 0 0 0 0 0 0 0
                   5 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   A 0 0 0 0 0 0 0 0
                   B 0 0 6 7 0 0 0 0
                   C 0 0 0 0 0 6 7 0
                   
                  possible of A: 6 7 8 9
                              B: 8 9
                              C: 8 9
                  since B and C can only be 8 and 9 ---> so A cannot be 8 and 9
                                                         new possible of A: 6 7
      """
      for i in range(9):
        for j in range(1, 10):
          for k in range(1, 10):
            if k != j:
              count = 0
              temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
              temp [j - 1] = j
              temp [k - 1] = k
              for l in range(9):
                if possible [i][l] == temp:
                  count += 1
              if count == 2:
                for l in range(9):
                  if possible [i][l] != temp:
                    possible [i][l][j - 1] = 0
                    possible [i][l][k - 1] = 0
      """
      if there is two blank having the only same two possible in a column ---> delete possible of blank not having the same two possible in a column

      example ---> 1 2 3 4 5 0 A B C
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 6 0
                   0 0 0 0 0 0 0 7 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 6
                   0 0 0 0 0 0 0 0 7
                   0 0 0 0 0 0 0 0 0
                   
                  possible of A: 6 7 8 9
                              B: 8 9
                              C: 8 9
                  since B and C can only be 8 and 9 ---> so A cannot be 8 and 9
                                                         new possible of A: 6 7
      """
      for i in range(9):
        for j in range(1, 10):
          for k in range(1, 10):
            if k != j:
              count = 0
              temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
              temp [j - 1] = j
              temp [k - 1] = k
              for l in range(9):
                if possible [l][i] == temp:
                  count += 1
              if count == 2:
                for l in range(9):
                  if possible [l][i] != temp:
                    possible [l][i][j - 1] = 0
                    possible [l][i][k - 1] = 0
      """
      if there is two blank having the only same two possible in a box ---> delete possible of blank not having the same two possible in a box

      example ---> 1 2 3 0 0 0 0 0 0
                   4 5 A 0 0 0 0 0 0
                   B C 0 0 0 0 0 0 0
                   6 0 0 0 0 0 0 0 0
                   7 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 6 0 0 0 0 0 0 0
                   0 7 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   
                  possible of A: 6 7 8 9
                              B: 8 9
                              C: 8 9
                  since B and C can only be 8 and 9 ---> so A cannot be 8 and 9
                                                         new possible of A: 6 7
      """
      for i in range(9):
        for j in range(1, 10):
          for k in range(1, 10):
            if k != j:
              count = 0
              temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
              temp [j - 1] = j
              temp [k - 1] = k
              if i <= 2:
                y_box = 0
              elif i <= 5:
                y_box = 3
              else:
                y_box = 6
              if i == 0 or i == 3 or i == 6:
                x_box = 0
              elif i == 1 or i == 4 or i == 7:
                x_box = 3
              else:
                x_box = 6
              for l in range(y_box, y_box + 3):
                for m in range(x_box, x_box + 3):
                  if possible [l][m] == temp:
                    count += 1
              if count == 2:
                for l in range(y_box, y_box + 3):
                  for m in range(x_box, x_box + 3):
                    if possible [l][m] != temp:
                      possible [l][m][j - 1] = 0
                      possible [l][m][k - 1] = 0
      """
      if there is three blank having the only same two or three possible in a row ---> delete possible not having the only same two or three possible in a row

      example ---> 1 0 0 0 0 0 0 0 0
                   2 0 0 0 0 0 0 0 0
                   3 0 0 0 0 0 0 0 0
                   4 0 0 0 0 0 0 0 0
                   5 0 0 0 0 0 0 0 0
                   A 0 0 0 0 0 0 0 0
                   B 0 0 0 0 0 0 0 0
                   C 0 6 0 0 0 0 0 0
                   D 0 0 0 0 0 0 0 0
                   
                  possible of A: 6 7 8 9
                              B: 7 8 9
                              C: 7 8 9
                              D: 7 8 9

                  since B, C and D can only be 7, 8 and 9 ---> so A cannot be 7, 8 and 9
                                                               new possible of A: 6

      example ---> 1 0 0 0 0 0 0 0 0
                   2 0 0 0 0 0 0 0 0
                   3 0 0 0 0 0 0 0 0
                   4 0 0 0 0 0 0 0 0
                   5 0 0 0 0 0 0 0 0
                   A 0 0 0 0 0 0 0 0
                   B 0 0 0 0 0 0 0 0
                   C 0 6 0 0 0 0 0 0
                   D 0 0 7 0 0 0 0 0

                   possible of A: 6 7 8 9
                               B: 7 8 9
                               C: 7 8 9
                               D: 8 9

                  since B, C and D can only be 7, 8 and 9 ---> so A cannot be 7, 8 and 9
                                                               new possible of A: 6
      """
      for i in range(9):
        for j in range(1, 10):
          for k in range(1, 10):
            for l in range(1, 10):
              if j != k and j != l and k != l:
                count = 0
                temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp [j - 1] = j
                temp [k - 1] = k
                temp [l - 1] = l
                count1 = 0
                temp1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp1 [j - 1] = j
                temp1 [k - 1] = k
                count2 = 0
                temp2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp2 [j - 1] = j
                temp2 [l - 1] = l
                count3 = 0
                temp3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp3 [k - 1] = k
                temp3 [l - 1] = l
                for m in range(9):
                  if possible [i][m] == temp:
                    count += 1
                  elif possible [i][m] == temp1:
                    count1 += 1
                  elif possible [i][m] == temp2:
                    count2 += 1
                  elif possible [i][m] == temp3:
                    count3 += 1
                if count == 3:
                  for m in range(9):
                    if possible [i][m] != temp:
                      possible [i][m][j - 1] = 0
                      possible [i][m][k - 1] = 0
                      possible [i][m][l - 1] = 0
                elif count == 2:
                  if count1 == 1:
                    for m in range(9):
                      if possible [i][m] != temp and possible [i][m] != temp1:
                        possible [i][m][j - 1] = 0
                        possible [i][m][k - 1] = 0
                        possible [i][m][l - 1] = 0
                  elif count2 == 1:
                    for m in range(9):
                      if possible [i][m] != temp and possible [i][m] != temp2:
                        possible [i][m][j - 1] = 0
                        possible [i][m][k - 1] = 0
                        possible [i][m][l - 1] = 0
                  elif count3 == 1:
                    for m in range(9):
                      if possible [i][m] != temp and possible [i][m] != temp3:
                        possible [i][m][j - 1] = 0
                        possible [i][m][k - 1] = 0
                        possible [i][m][k - 1] = 0
      """
      if there is three blank having the only same two or three possible in a column ---> delete possible not having the only same two or three possible in a column

      example ---> 1 2 3 4 5 A B C D
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 6 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   
                  possible of A: 6 7 8 9
                              B: 7 8 9
                              C: 7 8 9
                              D: 7 8 9

                  since B, C and D can only be 7, 8 and 9 ---> so A cannot be 7, 8 and 9
                                                               new possible of A: 6

      example ---> 1 2 3 4 5 A B C D
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 6 0
                   0 0 0 0 0 0 0 0 7
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0

                   possible of A: 6 7 8 9
                               B: 7 8 9
                               C: 7 8 9
                               D: 8 9

                  since B, C and D can only be 7, 8 and 9 ---> so A cannot be 7, 8 and 9
                                                               new possible of A: 6
      """
      for i in range(9):
        for j in range(1, 10):
          for k in range(1, 10):
            for l in range(1, 10):
              if j != k and j != l and k != l:
                count = 0
                temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp [j - 1] = j
                temp [k - 1] = k
                temp [l - 1] = l
                count1 = 0
                temp1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp1 [j - 1] = j
                temp1 [k - 1] = k
                count2 = 0
                temp2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp2 [j - 1] = j
                temp2 [l - 1] = l
                count3 = 0
                temp3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp3 [k - 1] = k
                temp3 [l - 1] = l
                for m in range(9):
                  if possible [m][i] == temp:
                    count += 1
                  elif possible [m][i] == temp1:
                    count1 += 1
                  elif possible [m][i] == temp2:
                    count2 += 1
                  elif possible [m][i] == temp3:
                    count3 += 1
                if count == 3:
                  for m in range(9):
                    if possible [m][i] != temp:
                      possible [m][i][j - 1] = 0
                      possible [m][i][k - 1] = 0
                      possible [m][i][l - 1] = 0
                elif count == 2:
                  if count1 == 1:
                    for m in range(9):
                      if possible [m][i] != temp and possible [m][i] != temp1:
                        possible [m][i][j - 1] = 0
                        possible [m][i][k - 1] = 0
                        possible [m][i][l - 1] = 0
                  elif count2 == 1:
                    for m in range(9):
                      if possible [m][i] != temp and possible [m][i] != temp2:
                        possible [m][i][j - 1] = 0
                        possible [m][i][k - 1] = 0
                        possible [m][i][l - 1] = 0
                  elif count3 == 1:
                    for m in range(9):
                      if possible [m][i] != temp and possible [m][i] != temp3:
                        possible [m][i][j - 1] = 0
                        possible [m][i][k - 1] = 0
                        possible [m][i][k - 1] = 0
      """
      if there is three blank having the only same two or three possible in a column ---> delete possible not having the only same two or three possible in a column

      example ---> 1 2 3 0 0 0 0 0 0
                   A 4 5 0 0 0 0 0 0
                   B C D 6 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   
                  possible of A: 6 7 8 9
                              B: 7 8 9
                              C: 7 8 9
                              D: 7 8 9

                  since B, C and D can only be 7, 8 and 9 ---> so A cannot be 7, 8 and 9
                                                               new possible of A: 6

      example ---> 1 2 3 0 0 0 0 0 0
                   A 4 5 0 0 0 0 0 0
                   B C D 6 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0
                   0 0 0 0 0 0 0 0 0

                   possible of A: 6 7 8 9
                               B: 7 8 9
                               C: 7 8 9
                               D: 8 9

                  since B, C and D can only be 7, 8 and 9 ---> so A cannot be 7, 8 and 9
                                                               new possible of A: 6
      """
      for i in range(9):
        for j in range(1, 10):
          for k in range(1, 10):
            for l in range(1, 10):
              if j != k and j != l and k != l:
                count = 0
                temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp [j - 1] = j
                temp [k - 1] = k
                temp [l - 1] = l
                count1 = 0
                temp1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp1 [j - 1] = j
                temp1 [k - 1] = k
                count2 = 0
                temp2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp2 [j - 1] = j
                temp2 [l - 1] = l
                count3 = 0
                temp3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                temp3 [k - 1] = k
                temp3 [l - 1] = l
                if i <= 2:
                  y_box = 0
                elif i <= 5:
                  y_box = 3
                else:
                  y_box = 6
                if i == 0 or i == 3 or i == 6:
                  x_box = 0
                elif i == 1 or i == 4 or i == 7:
                  x_box = 3
                else:
                  x_box = 6
                for m in range(y_box, y_box + 3):
                  for n in range(x_box, x_box + 3):
                    if possible [m][n] == temp:
                      count += 1
                    elif possible [m][n] == temp1:
                      count1 += 1
                    elif possible [m][n] == temp2:
                      count2 += 1
                    elif possible [m][n] == temp3:
                      count3 += 1
                if count == 3:
                  for m in range(y_box, y_box + 3):
                    for n in range(x_box, x_box + 3):
                      if possible [m][n] != temp:
                        possible [m][n][j - 1] = 0
                        possible [m][n][k - 1] = 0
                        possible [m][n][l - 1] = 0
                elif count == 2:
                  if count1 == 1:
                    for m in range(y_box, y_box + 3):
                      for n in range(x_box, x_box + 3):
                        if possible [m][n] != temp and possible [m][n] != temp1:
                          possible [m][n][j - 1] = 0
                          possible [m][n][k - 1] = 0
                          possible [m][n][l - 1] = 0
                  elif count2 == 1:
                    for m in range(y_box, y_box + 3):
                      for n in range(x_box, x_box + 3):
                        if possible [m][n] != temp and possible [m][n] != temp2:
                          possible [m][n][j - 1] = 0
                          possible [m][n][k - 1] = 0
                          possible [m][n][l - 1] = 0
                  elif count3 == 1:
                    for m in range(y_box, y_box + 3):
                      for n in range(x_box, x_box + 3):
                        if possible [m][n] != temp and possible [m][n] != temp3:
                          possible [m][n][j - 1] = 0
                          possible [m][n][k - 1] = 0
                          possible [m][n][k - 1] = 0
      if board == solution:
        return print_board
      elif past_possible == possible:
        break



import urllib.request
def new_board_solution():
  global solution
  webUrl = urllib.request.urlopen('https://www.sudokuweb.org/')
  solution = []
  for i in range(95):
    data = str(webUrl.readline())
  for i in range(9):
    temp = []
    data = str(webUrl.readline())
    data = str(webUrl.readline())
    for j in range(9):
      data = str(webUrl.readline())
      data = str(webUrl.readline())
      temp.append(int(data [37]))
    solution.append(temp)



"""
x_box = 0, 3, 6
"""
def x_to_xbox(x):
  while x != 0 and x != 3 and x != 6:
    x -= 1
  return x



"""
y_box = 0, 3, 6
"""
def y_to_ybox(y):
  while y != 0 and y != 3 and y != 6:
    y -= 1
  return y



def random_sub_board(count):
  global board
  board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
  print_board_will_change_with_board_so_i_use_this_name = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]
  for i in range(count):
    while True:
      x_rand = randint(0, 8)
      y_rand = randint(0, 8)
      if board [y_rand][x_rand] == 0:
        board [y_rand][x_rand] = solution [y_rand][x_rand]
        print_board_will_change_with_board_so_i_use_this_name [y_rand][x_rand] = solution [y_rand][x_rand]
        break
  return print_board_will_change_with_board_so_i_use_this_name


  
def all_possible(poss_board):
  global possible
  possible = []
  for i in range(9):
    temp = []
    for j in range(9):
      if poss_board [i][j] != 0:
        temp.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
      else:
        temp1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for k in range(9):
          if poss_board [k][j] != 0:
            temp1 [poss_board [k][j] - 1] = 0
          if board [i][k] != 0:
            temp1 [poss_board [i][k] - 1] = 0
        if j <= 2:
          x_box = 0
        elif j <= 5:
          x_box = 3
        else:
          x_box = 6
        if i <= 2:
          y_box = 0
        elif i <= 5:
          y_box = 3
        else:
          y_box = 6
        for k in range(x_box, x_box + 3):
          for l in range(y_box, y_box + 3):
            if poss_board [l][k] != 0:
              temp1 [poss_board [l][k] - 1] = 0
        temp.append(temp1)
    possible.append(temp)  



new_board()
for i in range(9):
  print(print_board [i])
