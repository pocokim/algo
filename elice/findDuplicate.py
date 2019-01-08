
def findDuplicate(nums):
    # nums.sort()
    # for i in range(len(nums)-1):
    #     if nums[i]==nums[i+1]:
    #         return nums[i]

    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]

def main():
    print(findDuplicate([1, 5, 2, 4, 5, 6, 3]))

if __name__ == "__main__":
    main()