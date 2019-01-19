a = [3, 7, 11, 15, 20, 26, 32, 38, 45, 52]
print(sum(a))

int' object is not callable 에러

sum이라는 변수를 선언하면 안됨...

#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, T, requiredTime):
        # print(T)
        # print(requiredTime)
        
        # a = 문제의 갯수
        # b = 벌점
        # return [a,sum(b)]
        
        requiredTime.sort()
        # print(requiredTime)

        temp =[]
        bulz = 0
        for i in range(len(requiredTime)):
            bulz += int(requiredTime[i])
            # print(sum)
            if bulz <= T:
                temp.append(bulz)
            # print(temp)
            # print(type(sum))
        
        if temp:
            # print(len(temp),sum(temp))
            return [len(temp),sum(temp)] <- 이렇게 리턴해도 되나? 순간 햇갈림 
        else :
            return [0,0]
        # print(len(temp))
        # print(sum(temp))
            
        # return [len(temp),sum(temp)]

        return 
        
            
        
        
        
