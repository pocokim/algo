# 30분 

A = {}
B = {}

for i in range(101):
    if i in [1]:
        A[i] = 5000000
        # 범위 만들기 
    elif i in list(range(2,4)):
        A[i] = 3000000
    elif i in list(range(4,7)):
        A[i] = 2000000
    elif i in list(range(7,11)):
        A[i] = 500000
    elif i in list(range(11,16)):
        A[i] = 300000
    elif i in list(range(16,22)):
        A[i] = 100000
    else :
        A[i] = 0

for i in range(65):
    money = 5120000
    if i == 1:
        B[i] = money
    elif i in list(range(2,4)):
        B[i] = money/2
    elif i in list(range(4,8)):
        B[i] = money/4
    elif i in list(range(8,16)):
        B[i] = money/8
    elif i in list(range(16,32)):
        B[i] = money/16
    else : 
        B[i] = 0

T = int(input())
for i in range(T):
    a, b = input().split()
    a = int(a)
    b = int(b)

    print(int(A[a]+B[b]))


