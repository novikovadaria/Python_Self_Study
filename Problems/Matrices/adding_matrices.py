x = [ [1,7,3], 
      [4,5,6], 
      [7,8,9]]

y = [ [1,9,1], 
      [6,7,3], 
      [4,5,9]]

result = [  [0,0,0], 
            [0,0,0], 
            [0,0,0]]

for row in range(len(x)):
    for col in range(len(x[0])):
        result[col][row] = x[col][row] + y[col][row]
print(result)
