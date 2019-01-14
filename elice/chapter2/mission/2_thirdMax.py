
def thirdMax(nums):

    # 풀이 1
    # nums.remove(max(nums))
    # nums.remove(max(nums))
    # return max(nums)
    
    #풀이 2
    ans = [ nums[0],nums[1],nums[2]]
    ans[2],ans[0],ans[1] = max(ans) , min(ans) , sum(ans) - max(ans) - min(ans)
    
    for i in range(3,len(nums)):
        if nums[i] > ans[2]:
            ans[2],ans[1],ans[0] = nums[i],ans[2],ans[1]
        elif  nums[i] < ans[2] and nums[i] > ans[1] :
            ans[1],ans[0] = nums[i],ans[1]
        elif nums[i] < ans[1] and nums[i] >ans[0] :
            ans[0] = nums[i]

    return ans[0]
    

    # temp =[nums[0],nums[1],nums[2]]
    # for i in range(3,len(nums)):
    #     a = max(nums[i],max(temp))
    #     if a in temp:
    #         pass
    #     else : 
    #         temp.append(a)
    #         temp.remove(min(temp))
        
    #     print(temp)
    # return min(temp)




    # nums.sort()
    # return nums[-3]
    # 90점 짜리 풀이라고 한다... 

def main():
    print(thirdMax([2, 19, 8, 37, 4, 5, 12, 50, 1, 34, 23])) # should return 34

if __name__ == "__main__":
    main()


# 3번쨰로 큰 숫자를 찾는건데.. nlogn의 시간복잡도 여서 그런지 90점이 나오더라구요.
#         더 빠르게 해결하기 위해서 제 생각에는 웬지.. 1장의 
        
#         def twoSum(nums, target):
#             nums.sort()
#             i,j = 0,len(nums)-1

#             while i<j:
#                 sum = nums[i]+nums[j]
#                 if target == sum :
#                     return nums[i], nums[j]
#                 elif sum > target:
#                     j -= 1
#                 elif sum < target:
#                     i += 1
#             return False
            
#         이런 함수처럼 하나의 배열에서 i와 j라는 인덱스를 변경하면서 3번째로 큰 값을 찾아야할것같은데... 이 아이디어가 맞나요?
#         저는 단순히 sorting을 하고 3번째로 큰 값을 찾으면 된다고 생각했는데.. sort보다 낮은 시간복잡도로 찾으려니 어떻게 해결해야할지 사실 
#         감이 잘 안잡히네요 

#         #
#      음음.... 일단 문제를 만드는 과정에서 의도한 풀이중에는 i,j를 이용한 것은 없었습니다. 한번 고민해보셔서 해당 방법으로 푸시는것도 하나의 방법이 되겠지만 다른 방법으로 알려드리겠습니다.
        
#         # 첫번째 방법은 제일 큰수, 2번째로 큰수, 3번째로 큰수를 저장해 나가는 방식입니다.
        
#         [2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23] 를 예시로 들면
        
#         [2]
#         [2, 8]
#         [2, 8, 19]
#         [8, 19, 37]
#         [8, 19, 37]
#         [8, 19, 37]
#         [12, 19, 37]
#         이런 식으로 진행해 마지막에
#         [34, 37, 50]
#         이 되어 34가 답이 되는 것이죠.
        
#         두번째 방법은 배열에서 최대값을 찾는것은 O(n)이고 삭제하는것도 O(n)이므로
#         제일 큰값을 찾아 배열에서 제거하고, 다시 제일 큰값을 찾아 배열에서 제거한 뒤
#         제일 큰 값을 찾으면 3번재로 큰 값이 됩니다.
        
#         어느쪽이든 O(n)의 방법이니 한번 쉬워보이는 쪽으로 푸시면 될 것 같습니다.
#         이해 되셨나요?
        
  
        