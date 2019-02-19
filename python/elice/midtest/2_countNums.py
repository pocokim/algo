def solution(nums):
    #풀이 1 set 
    # return list(set(nums))

    #풀이 2 딕셔너리
    # dic = {}
    # for i in range(len(nums)):
    #     if nums[i] not in dic.values():
    #         dic[i] = nums[i]
    # return len(dic.values())    
    
    #풀이 3
    # nlogn 시간복잡도 sort후 조건문     
    #     temp =[nums[0]]
    #     nums.sort()
    #     for i in range(1,len(nums)):
    #         if nums[i] != nums[i-1]:
    #             temp.append(nums[i])
    #     return len(temp)
    

    # 풀이 4 브루트 포싱 
    # 시간복잡도 n^2
    # temp = []
    # for i in range(len(nums)):
    #     if nums[i] not in temp:
    #         temp.append(nums[i])
    # return len(temp)

    # DP로 해결할 수 있을것같음... 
    # temp = [nums[0]]
    # for i in range(1,len(nums)):
    #     if 

def main():
    print(solution([1, 3, 1, 2, 5, 3, 1, 4, 2, 3]))
    
if __name__ == "__main__" :
    main()
