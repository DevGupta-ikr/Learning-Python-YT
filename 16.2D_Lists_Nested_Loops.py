# 2D List

number_grid = [
    [1,2,3],   # 4 rows 3 columns 2D list
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][2])
print(number_grid[1][1])
print(number_grid[2][2])


# Nested Loop

for row in number_grid:
    for col in row:
        print(col)