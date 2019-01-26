def solution(arrA, arrB):
    answer = True
    for i in range(len(arrA)):

        # 리스트 쪼개는 법 
        # arrA = arrA[-1:]+arrA[0:len(arrA)-1]
        # -1 부터 ~ 라는 의미를 가진다. 
        arrA = arrA[:-1]+arrA[-1:]
        if arrA == arrB:
            answer = True
            return answer
        else :
            answer = False
            
    return answer

print(solution([4,3,1,4],[4,4,1,3]))