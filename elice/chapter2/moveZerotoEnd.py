
def moveZerosToEnd(nums):
    curr = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            # print('nums['+str(i)+']가 0값을가짐')
            # print(nums)
            nums[curr] = nums[i]
            # print(nums[curr])
            # print(nums)
            # if i != curr:
            nums[i] = 0
            # print(nums)
            # nums[i] = 0
            curr += 1 
    return nums
    
    # for i in range(len(nums)):
        
    #     if nums[i] == 0:
    #         print('if문 통과')
    #         nums.pop(i)
    #         # nums.pop(nums[i])
    #         # print(nums)
    #         nums.append(0)
    #         # print(nums)
    #     # else :
    #     #     print('if문을 통과하지 못함')
    #     # print('결과후의')
    #     # print(nums)
    # return nums


    # temp = []
    # for i in range(len(nums)):
    #     if nums[i] == 0:
    #         temp.append(i)
    #         print(temp)
    # for i in range(len(temp)):
    #     # nums.pop(temp[i])
    #     print(temp[i])
    # pop을 할때마다 nums의 길이가 달라져서 list out of range가 나오게 된다.


def main():
    print(moveZerosToEnd([0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0]))
    # print(moveZerosToEnd([0, 8, 0, 37]))


if __name__ == "__main__":
    main()
