# Row-wise sum
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

# main - row-wise sum
for r in range(rows):
    s = 0
    for c in range(cols):
        s += matrix[r][c]
    print("Row Sum:", s)



# column-wise sum
'''
for c in range(cols):
    s = 0
    for r in range(rows):
        s += matrix[r][c]
    print("Column Sum:", s)
'''