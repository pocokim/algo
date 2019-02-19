#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, N, s):
        
        totalP = sum(s) # 전체상품의 개수
        kunP = len(s) # 큰손고객이 한번에 소비하는 개수
        
        for i in range(0,N+1):
            
            
            # print(kunP * i + (kunP-1) * (N-i))
            # print(totalP)

            # 이걸로 한번에 걸러지는줄 몰랐음. 전체상품의 갯수가 손님의 수보다 작은경우 다른 조건문이 필요한줄알았음... 
            if kunP * i + (kunP-1) * (N-i) >= totalP : 
                return i

# (kunP-1) * (N-i) 를 안하고 if kunP * i + (kunP-1) * N-i >= totalP : 라고 해서 연산이 계속 틀리게 나왔었음... 괄호의 중요성.. 