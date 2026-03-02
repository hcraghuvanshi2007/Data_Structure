# Matrix Traversal 
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

# main - row wise traversal 
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=" ")
    print()


# column wise traversal
'''
for c in range(cols):
    for r in range(rows):
        print(matrix[r][c], end=" ")
    print()
'''