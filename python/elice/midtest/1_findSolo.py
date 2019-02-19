def solution(nums):
    #풀이 1
    nums.sort()
    for i in range(len(nums)):
        if (nums[i+2]-nums[i+1]==1 and nums[i+1]-nums[i]==1):
            return nums[i+1]
    #풀이 2
    # for i in range(1,int(((len(nums)+1)/2))+1):
    #     if nums.count(i) !=2 :
    #         return i


def main():
    print(solution([1, 5, 3, 1, 2, 6, 4, 5, 2, 6, 3]))
    
if __name__ == "__main__" :
    main()
