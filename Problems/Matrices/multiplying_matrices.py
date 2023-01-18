x = [ [1,7,3], 
      [4,5,6], 
      [7,8,9]]

y = [ [1,9,1,4], 
      [6,7,3,7], 
      [4,5,9,9]]

result = [  [0,0,0,0], 
            [0,0,0,0], 
            [0,0,0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
print(result)