data = [
    [83, 67, 79],
    [52, 95, 75],
    [59, 58, 100],
    [57, 65, 50]
]
row_name = ['a', 'b', 'c', 'd']
col_name = ['e', 'f', 'g']

for i, row in enumerate(data):
    for j, col in enumerate(row):
        print(f"from {row_name[i]} to {col_name[j]} is {col}")
