class Solution:
    # 2번째 풀이 
    def solution(self, swaps):
        table =['o','x','x']
        for swap in swaps:
            a = int(swap[0])
            b = int(swap[2])
            table[a-1],table[b-1]=table[b-1],table[a-1]
            
        return int(table.index('o'))+1

    def soltion(self,nums):
    # 3번쨰 풀이
        table=[0,1,0,0] # 테이블 초기화 1,2,3 순서를 맞추기 위한 0번째 위치 생성 


        for i in range(len(nums)):
            a = nums[i].split('-') # 입력받은 문자열리스트 분해 

            table[int(a[0])],table[int(a[1])] = table[int(a[1])] , table[int(a[0])]
            # swap 

        return table.index(1)  #반환 

    #키포인트 : [0]번째 index 추가생성, 입력받은 문자열 split으로 분해