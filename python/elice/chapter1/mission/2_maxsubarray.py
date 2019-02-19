
def maxSubArray(nums):
    
    answer = [nums[0]]
    for i in range(1,len(nums)):
        answer.append(max(answer[i-1]+nums[i],nums[i]))
    return max(answer)

    # sum = (max(nums))
    # lefttemp = sum
    # leftsum = sum
    # righttemp = 0
    # rightsum = 0
    
    # for i in range(1,nums.index(max(nums))):
    #     lefttemp += nums[nums.index(max(nums))-i]
    #     if lefttemp >= leftsum:
    #         leftsum = lefttemp
    
    # print(nums.index(max(nums)))
    # print(len(nums)-1)
            
    # for i in range(nums.index(max(nums)),len(nums)-1):
    #     righttemp +=nums[i]
    #     if righttemp >= rightsum:
    #         rightsum = righttemp

    # print(leftsum)
    # print(rightsum)
    
    # if leftsum >= rightsum:
    #     return leftsum
    # else:
    #     return rightsum


    # maxSub = [nums[0]]
    # for i in range(1,len(nums)):
    #     maxSub.append(max(maxSub[i-1]+nums[i],nums[i]))
    # # print(maxSub)
    # return max(maxSub)


def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1])) # 30이 리턴되어야 합니다

if __name__ == "__main__":
    main()