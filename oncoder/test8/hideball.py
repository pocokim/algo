
def ballFinder(nums):
    table=[1,0,0]
    # 1번째풀이
    for num in nums:
        toswap1 = int(num[0])-1 # 바꾸고자 하는 첫번쨰 컵
    #     toswap2 = int(num[2])-1 # 바꾸고자 하는 두번째 컵 


        # 컵의 교환 
        temp = table[toswap1]
        table[toswap1] = table[toswap2]
        table[toswap2] = temp

        # print(table)


    answer = table.index(1) # 공이 있는 위치반환 
        
        
    return answer+1

swaps = ["1-2","3-1"]
# swaps = ["1-2","3-2","1-2","2-1","2-1","3-2","1-3","3-1","1-2"]
# swaps =["2-3","1-3","2-3","2-1","3-1"]
print(ballFinder(swaps))

# 3번째 풀이 
# class Solution:
#     def solution(self, swaps):
#         table =['o','x','x']
#         for swap in swaps:
#             a = int(swap[0])
#             b = int(swap[2])
#             table[a-1],table[b-1]=table[b-1],table[a-1]
            
#         return int(table.index('o'))+1
