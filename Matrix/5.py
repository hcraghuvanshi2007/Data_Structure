# Print upper triangular part of a matrix
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

# main
for r in range(rows):
    for c in range(r+1, cols):
        print(matrix[r][c], end=" ")
    print()