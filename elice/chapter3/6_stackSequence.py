
# 1) 어떤식으로 코딩을 작성할것인가? 
# 1부터 n까지에 수에 대해 차례로 [push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.
# 처음에 감을 못잡았다. 스택에서 빠진순서대로 다시 넣으면 될것도 같은데, 뭔가 안될것같았기 떄문이다. 그래서 스택으로 사용해서 풀어야될것같으면서도 엄두를 못냈다. 
# https://www.acmicpc.net/problem/1874 백준문제와 유사하고, 백준 힌트를 보고 풀이법을 생각할 수 있었다. 
# 결국 nums를 받아서 , 원래 넣고 빼는것의 반대로 push,push,pop,pop이라면 / pop,pop,push,push를 해서 temp를 만들고 만들어진 배열이 1,2,3,4 순서의 역순이라면 true를 아니라면 false를 리턴하면됨.

# 2) 실제 코딩을 작성하는데의 애로사항 
# 12345678 순서로 temp를 채우려면 
# (7,8) (5,6) (1,2,3,4)
# 먼저들어가는거는 맨앞에 넣고, 이경우 [7,5,1] -> temp.insert(0,num)
# 그다음에 들어가는거는 같이들어가는수의 오른쪽에 추가되도록한다. -> 이걸어떻게 코딩해야할지 몰겠음.
# temp.insert()

# 반대로 

# 87654321 순서로 temp를 채운다면
# (7,8) (5,6) (1,2,3,4)
# 먼저들어가는것을 맨 뒤에 넣고 temp.insert(-1,num) 혹은 temp.append(num)
# 그 다음에 들어가는거는 같이 들어가는수의 왼쪽에 추가되도록한다. -> 이것도 역시... 어떻게 코딩해야할지..
# temp.index(먼저들어가는숫자),


# -> temp.append랑 , temp.insert랑 temp.index를 잘 활용하면 될듯  근데 어떻게 할지 머리가 안돌아가고..
# 추가는 그렇게 해준다고 쳐도. 

# 어떤 조건 if문하에 추가되는건지 생각해봐야할듯.
# 내 생각에는 1씩 차이나야하는것, 최대값을 고려하는것, 나머지 값을 고려하는것과 같은 3가지 조건이 들어가야함. 

# ====================================

# 해설을 본다음의 나의 생각: 나는 4, 3, 6, 8 을 그대로 이용해서 사용하려고 했는데, 4라는 숫자 자체를 push해서 풀기보다는 4까지 즉 1,2,3,4를 push하고 pop해서 빠진게 4이다. 라는 식으로 접근하는 문제였다. 
# 즉 count를 이용햐서 푸는 문제였던것이다. 




# def isStackSequence(nums):

#     # 1,2를 바탕으로 해본 삽질1
#     # stack =[]
#     # for num in nums:
#     #     if len(stack) ==0:
#     #         stack.append(num)
#     #         print(stack)
#     #     else: 
#     #         if num < stack[-1]:
#     #             stack.append(num)
#     #         else :
#     #             stack.pop()
#     #             print(stack)
#     #             stack.append(num)
#     #             print(stack)
#         # print(stack)

#     #  1,2를 바탕으로 해본 삽질2
#     # stack = [nums[0]]
#     # print(stack[-1])
#     # for i in range(1,len(nums)):
#     #     if nums[i] > stack[-1]:
#     #         stack.append(nums[i])
#     #     else :
#     #         stack.pop()
#     #     print(stack)

#     return True


def isStackSequence(nums):
    count = 1
    stack =[]
    for num in nums:
        while count <= num :
            stack.append(count)
            count +=1
            print(stack)
        
        # if num < count : 이렇게 짜면 빼고싶은값이 뺴지는게 아니라 , count보다 작은값은 다 빠지게 됨
        if num == stack[-1]:
            stack.pop()
            print(stack)
        else : return False
    
    if len(stack) == 0 : return True 
    # return True


def main():
    print(isStackSequence([2, 1, 4, 3])) # True가 리턴되어야 합니다
    print(isStackSequence([3, 1, 2, 4])) # False가 리턴되어야 합니다
    print(isStackSequence([4, 3, 6, 8, 7, 5, 2, 1])) # True 

    
if __name__ == "__main__":
    main()