# 다트게임

# 파싱을 문자열로 끊어서 할 필요가 없음. 글자별로 처리해도됨.
# 다시 풀어볼것... 

def dartResult(str1):
    answer = 0
    ans=[[0],[0],[0]]
    nums = []
    temp =[]


    # 숫자 인덱스찾기 
    for i in range(len(str1)):
        if str1[i].isdigit():
            temp.append(i)
    # print(temp)

    # 인덱스에 맞게 분리 
    nums.append(str1[temp[0]:temp[1]])
    nums.append(str1[temp[1]:temp[2]])
    nums.append(str1[temp[2]:])
    print(nums)

    for i in range(3):
        if nums[i][0] == '1' and nums[i][1] == '0':
            if nums[i][2] =='S':
                ans[i] = 10
            elif nums[i][2] =='D':
                ans[i] = 10*10
            elif  nums[i][2] =='T':
                ans[i] = 10*10*10         

        else : 
            if nums[i][1] =='S':
                ans[i] = int(nums[i][0])
            elif nums[i][1] =='D':
                ans[i] = int(nums[i][0]) * int(nums[i][0])
            elif  nums[i][1] =='T':
                ans[i] =int(nums[i][0]) * int(nums[i][0]) * int(nums[i][0])


    for i in range(3):
        if '#' in nums[i]:
            ans[i] *= -1
        if '*' in nums[i]:
            if i == 0:
                ans[0] *= 2
                # print(ans[0])
            if i ==1 or i ==2:
                # print(ans[0])
                ans[i] *= 2
                ans[i-1] *= 2
                # print(ans[1],ans[0])
             
        # if len(nums[i]) == 3:
        #     if nums[i][2] == '#':
        #         ans[i] *= -1
        #     if nums[i][2] == '*':
        #         if i == 0:
        #             ans[i] *= 2
        #         elif i ==1 or i ==2:
        #             ans[i] *= 2
        #             ans[i-1] *= 2
        

        # 개뻘짓. 출력하는 위치를 잘 찾아볼것!!!!!!!!!
        # 기존에 3번,4번,7번이 오류가났던 이유는 ans의 출력을 중간에 받았기 떄문 
    # print('종료후의 각각 ans값')

    # print(ans[0],ans[1],ans[2])    
    
                
    

    return ans[0]+ans[1]+ans[2]
    # return answer

print(dartResult('1S2D*3T'))
print()
print(dartResult('1D2S#10S'))
print()
print(dartResult('1S*2T*3S'))
print()

print(dartResult('1D#2S*3S'))
print()

print(dartResult('1D2S0T'))
print()

print(dartResult('1T2D3D#'))
print()

print(dartResult('1D2S3T*'))

