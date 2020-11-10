from itertools import chain

sudoku_field = [0, 4, 0,    3, 0, 0,    0, 2, 8,
                6, 3, 5,    7, 2, 0,    0, 0, 1,
                0, 0, 0,    4, 9, 0,    3, 0, 6,

                0, 5, 1,    2, 6, 0,    0, 8, 0,
                3, 0, 0,    0, 8, 0,    0, 1, 0,
                0, 9, 0,    0, 1, 4,    2, 6, 0,

                2, 0, 3,    0, 7, 9,    0, 0, 0,
                9, 0, 0,    0, 4, 5,    8, 3, 2,
                5, 6, 0,    0, 0, 2,    0, 7, 0]

columns = [sudoku_field[i::9] for i in range(9)]
rows = [sudoku_field[i:i+9] for i in range(0, 81, 9)]
squares = []

for i in range(0, 9, 3):
    for j in range(i, 81 + i, 27):
        square = [sudoku_field[k:k+3] for k in range(j, j + 21, 9)]
        squares.append(square)

for i in squares[:10]:
    squares.append(list(chain.from_iterable(i)))
    del squares[0]


# make options for numbers in columns (if there is a number in sudoku field then add empty list) ->

column_options = []
for column in columns:
    for element in column:
        option = []
        if element == 0:
            for i in range(1, 10):
                if i not in column:
                    option.append(i)
        column_options.append(option)

# make options for numbers in rows (if there is a number in sudoku field then add empty list) ->

rows_options = []
for row in rows:
    for element in row:
        option = []
        if element == 0:
            for i in range(1, 10):
                if i not in row:
                    option.append(i)
        rows_options.append(option)


# make options for numbers in squares (if there is a number in sudoku field then add empty list) ->

square_options = []
for square in squares:
    for element in square:
        option = []
        if element == 0:
            for i in range(1, 10):
                if i not in square:
                    option.append(i)
        square_options.append(option)


# combine options for one number and add them to all_options list

# for option in all_options:
#     for i in range(1, 10):
#         if option.count(i) > 1:
#             option.remove(i)
print()