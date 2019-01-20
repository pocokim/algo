
def maximizeProfit(nums):

    maxP = [nums[0]]
    minP = [nums[0]]
    profit =[0]
    for i in range(1,len(nums)):
        if nums[i] > maxP[-1]:
            maxP.append(nums[i])
        if nums[i] < minP[-1]:
            minP.append(nums[i])
        if nums.index(maxP[-1]) >= nums.index(minP[-1]):
            profit.append(maxP[-1]-minP[-1])
        elif nums.index(maxP[-1]) < nums.index(minP[-1]) : 
            profit.append(profit[i-1])
        
    print(profit)

    return profit[-1]


    # max(profit)
    
    # if profit == None :
    #     return 0
    # else : return max(profit)
    # ValueError: max() arg is an empty sequence  말그대로 알규먼트에 빈값이 들어간다는뜻 .
    
    # return max(profit)

    # return max(maxP) - min(minP) 이건 말그대로 최대값에서 최소값을 뺀것
    
    # print(maxP)
    # print(minP)

    # print(nums.index(maxP[-1]))
    # print(nums.index(minP[-1]))
    # if nums.index(maxP[-1]) > nums.index(minP[-1]) : # 인덱스를 비교하여 성립하면 넣고 성립하지 않으면 넣지않는식으로 해결하는게 좋을까
        
    # else :

    # 단순히 maxP, minP 를 만드는게 아니라 이익을 최대화 하는 값을 dp로 만들어주어야할것같은데.. 아직까지 모르겠다. 

def main():
    print(maximizeProfit([1,2,3,4,5,6,7])) # 6
    print(maximizeProfit([7,6,5,4,3,2,1])) # 0
    print(maximizeProfit([1,2,3,4,3,2,1])) # 3
    print(maximizeProfit([2,8,19,37,4,5])) # 35
    print(maximizeProfit([3,2,1,4,7,5,6])) # 6
    print(maximizeProfit([4,8,19,2,5,37])) # 35


if __name__ == "__main__":
    main()