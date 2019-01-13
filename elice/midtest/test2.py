def solution(nums):
    temp = []
    for i in range(len(nums)):
        if nums[i] not in temp:
            temp.append(nums[i])
    return len(temp)

    # DP로 해결할 수 있을것같음... 
    # temp = [nums[0]]
    # for i in range(1,len(nums)):
    #     if 

def main():
    print(solution([1, 3, 1, 2, 5, 3, 1, 4, 2, 3]))
    
if __name__ == "__main__" :
    main()
