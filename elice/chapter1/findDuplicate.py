
def findDuplicate(nums):
    # nums.sort()
    # for i in range(len(nums)-1):
    #     if nums[i]==nums[i+1]:
    #         return nums[i]

    # 승태 풀이 (이중포문 써서 단순비교)
    # for i in range(len(nums) - 1):
    # for j in range(i+1, len(nums)):
    #     if nums[i] == nums[j]:
    #         return nums[j]

    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]

def main():
    print(findDuplicate([1, 5, 2, 4, 5, 6, 3]))

if __name__ == "__main__":
    main()