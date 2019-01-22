
# 28
# 지도 한 변의 길이
n = int(input())
temparr1 = list(input())
temparr2 = list(input())
del temparr1[0]
del temparr1[-1]
del temparr2[0]
del temparr2[-1]
temparr1 = ''.join(temparr1)
arr1 = temparr1.split(', ')
temparr2 = ''.join(temparr2)
arr2 = temparr2.split(', ')
##################################################################
answer = []
for i in range(n):
    temp = []
    a = bin(int(arr1[i]))
    a = a[2:].zfill(n) # 빈거를 채워주는 함수 
    b = bin(int(arr2[i]))
    b = b[2:].zfill(n)
    for j in range(n):    
        if (a[j] == '0') and (b[j] == '0'):
            temp.append(' ')
        else:
            temp.append('#')
    answer.append(''.join(temp))
print(answer)
