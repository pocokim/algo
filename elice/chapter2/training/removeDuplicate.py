
def removeDuplicate(nums):
    temp = []
    for i in range(0,len(nums)-1):
        if nums[i]==nums[i+1]:
            temp.append(nums[i])
    for i in range(0,len(temp)):
        nums.remove(temp[i])
            # print(nums.index(nums[i]))
            # temp.append(nums.index(nums[i]))
    return nums
    # print(index)
    # return []

def main():
    print(removeDuplicate([1, 1, 2, 2, 2, 2, 5, 7, 7, 8])) # [1, 2, 5, 7, 8]을 리턴해야 합니다

if __name__ == "__main__":
    main()