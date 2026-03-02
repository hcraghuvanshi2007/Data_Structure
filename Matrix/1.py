rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

matrix = []

for r in range(rows):
    row = []
    for c in range(cols):
        val = int(input("Enter value: "))
        row.append(val)
    matrix.append(row)

print(matrix)