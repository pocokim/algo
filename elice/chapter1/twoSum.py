
    # for i in range(len(nums)):
    #     for j in range(1,len(nums)-i):
    #         temp = nums[i]+nums[i+j]
    #         if target == temp:
    #             return nums[i],nums[i+j]


    # for i in nums:
    #     if target- i in nums:
    #         return i,target-i

# 배열안의 숫자를 하나씩 보기위해서 숫자를 하나씩 사용하기 
# fo i in nums 
def twoSum(nums, target):
    nums.sort()
    i,j = 0,len(nums)-1

    while i<j:
        sum = nums[i]+nums[j]
        if target == sum :
            return nums[i], nums[j]
        elif sum > target:
            j -= 1
        elif sum < target:
            i += 1
    return False
# 2019.1.10 오피스아워    
# 슬라이딩 윈도우 알고리즘과 약간 유사하다고 함


# if in문의 사용

def main():
    print(twoSum([2, 8, 19, 37, 4, 5], 12))

if __name__ == "__main__":
    main()

# http://buggymind.com/473  : nonetype object is not iterable 

#     main에서 twoSum함수를 print하라는 명령을 실행할때,
#     twoSum함수는 return을 해주는 함수인데 변수에 담지 않고, 그것을 바로 print할 수 있는지? 

