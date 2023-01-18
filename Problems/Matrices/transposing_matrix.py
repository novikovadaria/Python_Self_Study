x = [ [1,7], 
      [5,4], 
      [7,8] ]

result = [[0,0,0],
          [0,0,0]]

# nested loop
for row in range(len(x)):
    for col in range(len(x[0])):
        result[col][row] =  x[row][col]


        # list comprehension
        # result = [[x[col][row] for col in range(len(x))] for row in range(len(x[0]))]

print(result)