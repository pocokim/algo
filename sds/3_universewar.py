testcase = input()
N,M,B = input().split()

matrix = [[0]*2 for i in range(int(M)) ]

for i in range(int(M)):
    matrix[i][0] , matrix[i][1] = input().split()

print(matrix)