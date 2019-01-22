# 비밀지도 
# 1시간 걸림. 81프로 


# 문자열이 안바뀌는걸 몰라서 계속 문자열을 리스트로 만들어서 변경하여 처리함.
# makeNum 에서 문자열로 처리후 리스토로 변환 후 다시 문자열로
# finder에서 문자열로 연산후 다시 리스토로 변환 해서 값을 변경한 다음에 다시 문자열로 변경 

# 비트연산에 대해서 공부할것, 비트연산 할줄 몰라서 하나하나씩 처리하였음.

def finder(num,arr1,arr2):
    bmap =[]
    for i in range(num):
         
        temp =''
        bArr1 =makeNum(num,arr1[i])
        bArr2 = makeNum(num,arr2[i])
        print(bArr1,bArr2)

        for i in range(num):

            # 여기서의 비트 연산 
            temp += str(int(bArr1[i]) or int(bArr2[i]))
        # print(temp)

        a = list(temp)
        for i in range(len(a)):
            if a[i] == '1':
                a[i] = '#'
            elif a[i] =='0':
                a[i] =' '
        
        temp = "".join(a)
        # print(temp)
        bmap.append(temp)
    return bmap

        # 파이썬은 문자열의 값을 변경할 수 없다. 
        # for i in range(len(temp)):
        #     if temp[i] =='1':
        #         temp[i] ='#'
        #     elif temp[i] =='0':
        #         temp[i] =' '
        # print(temp)

        # bArr1 = bin(arr1[i])
        # bArr2 = bin(arr2[i])

        # print(bArr1,bArr2)

        # if len(bArr1)-2 == 4:
        #     bArr1 = bArr1[:2]+'0'+bArr1[2:]
        # if len(bArr1)-2 == 4:
        #     bArr2 = bArr2[:2]+'0'+bArr2[2:]

        # print(bArr1,bArr2)



def makeNum(num,arr):
    makeNum =''
    for i in range(num):
        makeNum += str(arr%2)  
        arr = arr//2
        
    M = list(makeNum)
    M.reverse()
    makeNum = "".join(M)
    return makeNum

# print(makeNum(5,9))
        

print(finder(5,[9, 20, 28, 18, 11],	[30, 1, 21, 17, 28]))  # ["#####","# # #", "### #", "# ##", "#####"]
print(finder(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])) # ["######", "### #", "## ##", " #### ", " #####", "### # "]