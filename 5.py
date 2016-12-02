matrix = [[0,0,0],
         [0,0,0],
         [0,0,0]]

matrix1 = [[0,0,0],
          [0,0,0],
          [0,0,0]]

B = [[6,7,1],
    [3,8,4],
    [5,1,9]]

C = [[3,1,4],
    [7,2,3],
    [9,6,5]]

def addition(x, n, A):
    for y in range(len(x)):
        for z in range(len(x[0])):
            A[y][z] = x[y][z] + n[y][z]

def substraction(x, n, A):
    for y in range(len(x)):
        for z in range(len(x[0])):
            A[y][z] = x[y][z] - n[y][z]

def multiplication(x, n, A):
    for y in range(len(x)):
        for z in range(len(n[0])):
            for k in range(len(n)):
                A[y][z] += x[y][k] * n[k][z]


for i in matrix: 
    multiplication(B, C, matrix)
    print(i)

"""

pseudocode:

ADDITION(x, n, A)
    for y <-- lenght[x]
        for z <-- lenght[x[0]]:
            A[y][z] <-- x[y][z] + n[y][z]

SUBSTRACTION(x, n, A)
    for y <-- lenght[x]
        for z <-- lenght[x[0]]
            A[y][z] <-- x[y][z] - n[y][z]

MULTIPLICATION(x, n, A)
    for y <-- lenght[x]
        for z <-- lenght[n[0]]
            for k <-- lenght[n]
                A[y][z] <-- A[y][k] + ( x[y][k] * n[k][z] )


"""
