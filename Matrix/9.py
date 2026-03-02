# Reverse matrix 90 degrees 
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []

for r in range(rows):
    row = []
    for c in range(cols):
        val = int(input(f"Enter value at [{r}][{c}]: "))
        row.append(val)
    matrix.append(row)

print("\nMatrix is:")

# main - clockwise rotate (transpose + reverse each row)
transpose = [[0 for r in range(rows)] for c in range(cols)]

for r in range(rows):
    for c in range(cols):
        transpose[c][r] = matrix[r][c]

for r in range(rows):
    transpose[r].reverse()

print(transpose)

# anti-clockwise rotate (transpose + reverse each column)
'''transpose = [[0 for r in range(rows)] for c in range(cols)]

for r in range(rows):
    for c in range(cols):
        transpose[c][r] = matrix[r][c]

transpose.reverse()

print(transpose)'''