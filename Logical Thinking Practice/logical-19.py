# Adding Two Matrices

x = [[1, 2, 3],
     [4, 5, 6]]

y = [[7, 8, 9],
     [10, 11, 12]]

result = [[0, 0, 0],
          [0, 0, 0]]

# Matrix Addition
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

# Display Result
print("Addition of Two Matrices:")
for k in result:
    print(k)