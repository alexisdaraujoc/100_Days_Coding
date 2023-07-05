# Day 12: Matrix Pattern in Python

def create_matrix(rows, colums):
    matrix = []
    num = 1
    for a in range(rows):
        row = []
        for a in range(colums):
            row.append(num)
            num += 1 + a
        matrix.append(row)
    return matrix

rows = int(input('Enter the number of rows: '))
columns = int(input('Enter the number of columns: '))
matrix = create_matrix(rows, columns)
for ro in matrix:
    print(ro)
