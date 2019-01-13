def getParenthesisScore(st):
    def dq(i,j):
        ans = 0
        val = 0
        temp =[]
        for k in range(i,j):
            # print('i의 값'+str(i))
            val = (val +1 if st[k]=='(' else val -1) # 좌괄호와 우괄호에 점수 지정
            # temp.append(val)
            # print(temp)
            if val == 0: # 좌괄호와 우괄호의 쌍이맞을때 
                # print('k의값:'+str(k))
                if k - i ==1:
                    ans  += 1
                else : 
                    ans  += 2* dq(i+1,k) # 깊게 들어감
                    # 배운점2: dq의 범위가 dq(i+1,j)가 아니라 k임. 
                    # 어떻게 k로 할생각을 하냐면.. divide and conquer에 따라 깊게 들어간곳의 끝지점을 범위로 잡아야한다는 생각으로 해야함
                    #  j로 설정할 경우 .. 같은 계층에 있는 )(마저 연산해버림.

                i = k+1 # 배운점1: for문 range()안의 i값을 바꿀 수 있음.
                # print(ans)
        
        return ans

    return dq(0,len(st))



def main():
    # examples = ["()()(())", "(()(()))", "((()())())", "()", "((()))()"] # 4, 6, 10, 1, 5 점이 나와야 합니다.
    # for example in examples:
    #     print(example, getParenthesisScore(example))
    
    examples = ["((()())())"] # 4, 6, 10, 1, 5 점이 나와야 합니다.
    for example in examples:
        print(example, getParenthesisScore(example))
    
if __name__ == "__main__":
    main()