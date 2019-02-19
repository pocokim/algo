
def maximizeProfit(nums):

    maxP = [nums[0]] # nums[i]까지의 최대값을 저장하기 위한 배열
    minP = [nums[0]] # nums[i]까지의 최소값을 저장하기 위한 배열
    profit =[0] # i번째까지의 이익의 최대값을 저장하기 위한 배열 

    for i in range(1,len(nums)):
        if nums[i] > maxP[-1]: # nums[i]를 입력받았을때 입력받은값이 그전까지의 입력보다 크다면 maxP에 입력
            maxP.append(nums[i]) 
        if nums[i] < minP[-1]: # nums[i]를 입력받았을때 입력받은값이 그전까지의 입력보다 작다면 minP에 입력 
            minP.append(nums[i])
            # i번째까지의 최소를 찾기위함.

        if nums.index(maxP[-1]) >= nums.index(minP[-1]): # i번째의 최대이익은 i번째까지의 최대값에서 i번째까지의 최소값을 뺀 값임. 그러나 최대값이 나온위치는 항상 최소값의 위치보다 커야함.
            profit.append(maxP[-1]-minP[-1])
        elif nums.index(maxP[-1]) < nums.index(minP[-1]) : 
            profit.append(profit[i-1])
        

    return profit[-1]

    # 최대값과 최소값을 지정하지 않고 dp를 사용할 수 있나? 

    # profit = [0]
    # for i in range(1,len(nums)):
    #     if num[i] > num[i-1]:
    #         profit.append(num[i]-num[i-1]+profit[i-1])


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