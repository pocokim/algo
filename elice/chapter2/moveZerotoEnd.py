
def moveZerosToEnd(nums):
    # curr = 0
    # for i in range(len(nums)):
    #     if nums[i] != 0:
    #         # print('nums['+str(i)+']가 0값을가짐')
    #         # print(nums)
    #         nums[curr] = nums[i]
    #         # print(nums[curr])
    #         # print(nums)
    #         # if i != curr:
    #         nums[i] = 0
    #         # print(nums)
    #         # nums[i] = 0
    #         curr += 1 
    # return nums
    
    # for i in range(len(nums)):

    # for 문의 index가 바뀌기 때문에 while문을 통해 문제를 해결하려고 했으나 이 경우에도 오류가 생기는것을 알 수 있다. 

    # def moveZerosToEnd(nums):
    # for i in range(len(nums)):
    #     if nums[i] == 0:
    #         nums.pop(i)
    #         nums.append(0)

    # return nums

    # 따라서 이를 while문을 통해서 해결하려고 했다. 
    # 0이면 pop한 뒤에 append를 하고, 아니면 i를 증가시키는것으로 .. 
    # 그런데 이 경우 [0,0,1] 그리고 [0,0] 으로만 채워져있는경우를 해결하지 못한다. 
    # 따라서 pop과 append를 사용하기보다는 , curr을 이용하는것이 더 좋은 방법인것같다. 
    i = 0
    print(len(nums)-nums.count(0))
    while i < len(nums)-nums.count(0) :
        print(i)
        print(nums)
        if nums[i] == 0:
            # print('if문 통과')
            nums.pop(i)
            # nums.pop(nums[i])
            # print(nums)
            nums.append(0)
            print(nums)
            i = 0
            if i == len(nums)-nums.count(0) -1:
                break

            
        else:
            i += 1

        # else :
        #     print('if문을 통과하지 못함')

        # print('결과후의')
        # print(nums)
    return nums


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
    # print(moveZerosToEnd( [0, 0, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0] ))
    
    # print(moveZerosToEnd([0, 8, 0, 37]))
    # print(moveZerosToEnd([0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0]))

    print(moveZerosToEnd([0,0,1]))
    
if __name__ == "__main__":
    main()
