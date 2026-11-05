# Transpose of Two Matrices

x= [[1,4],
    [2,5],
    [3,6]
    ]

result = [[0,0,0],
          [0,0,0]]

# import numpy as np
# c=np.transpose(x)
# print(c)

for i in range (len(x)):
    for j in range (len(x[0])):
        result[j][i]=x[i][j]

for k in result:
    print(k)