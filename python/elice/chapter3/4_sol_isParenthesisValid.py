# 배운점 1번
# 역시 무한루프문이 아니라 인풋만큼 들어오는것이기에 while문을 사용하지 않고 해결할 수 있다.

# 배운점 2번 , 반복될것같은 if문은 딕셔너리를 사용하면 편하다.
# if문을 복잡하지 않게 만들기위해서 or 이 아니라 
# if st[i] == '(' or  st[i] ==  '[' or st[i] == '{' or st[i] == '<' :
# 대신 pOpens = ['(','[','{','<'] 라는 배열을 만들어서 처리 

# 3번
# i번째와 i-1번째가 {}로 이어져있는지를 판단하고 맞다면 지워주는 방식을 사용하고자 했는데  
# 이는 stack[-1]과 ch를 비교하면 됬다. 

# 4번 반복되는 if문은 딕셔너리를 사용하자. 
# if문에서 ch ='}' 일때 stack[-1]이 '{'인지, 즉 괄호가 짝이 맞는지 확인해주기 위해서 
#  stack[-1] == '{' and ch == '}' 과 같은 조건문을 여러개를 사용해주었는데 굳이 그럴필요없이
# 어떤 딕셔너리를 만들고 ch의 값에 따라 출력되게 하는것을 만들면 {' and ch == '}' 이 부분을 dic[ch]로 대체할 수 있다. 

#5번 
# 스택문제는 스택에 완전히 들어가면 true를 리턴할지 : 올바른 괄호가 들어가면 차곡차곡 쌓이게할지? / 괄호의 쌍이 맞으면 스택에서 빠지는것으로 할지 ? 고민이었는데 
# 스택의 유형은 스택에서 완전히 빠지면 true를 리턴하는 방식이 일반정인 방식인듯하다. 

def isParenthesisValid(st):
    pOpen = ['{','[','<','(']
    stack =[]
    dic ={'}':'{',')':'(','>':'<',']':'['}
    for ch in st:
        if ch in pOpen:
            stack.append(ch)
            # print(stack[-1])

        # 1. 스택이 비어있지 않고 2. 스택에 마지막에 들어온값이 왼쪽괄호이며 3.현재 ch와 짝이 맞아야한다. 

        # 파이썬에서 스택은 배열을 사용하기때문에 큐에서는 큐에 들어간 값을 저장할 수 없는데 비해, 스택은 stack[-1]로 마지막에 들어간 값을 찾을 수 있다.
        # 지금 ch이 아닌 그전의 ch를 어떻게 찾지? 때문에 처음에 ch[i-1]과 ch[i]번쨰를 찾으려고 다른 문자열변수를 만들기도 했었는데 stack[-1]을 하면 되는 문제였다.

        # if len(stack) != 0 and stack[-1] == '{' and ch == '}' :
        #     stack.pop()
        # if len(stack) != 0 and stack[-1] == '(' and ch== ')' :
        #     stack.pop()
        # if len(stack) != 0 and stack[-1] == '<' and ch == '>':
        #     stack.pop()
        # if len(stack) != 0 and stack[-1] == '[' and ch ==']':
        #     stack.pop()
        # print(stack)

        # 이렇게 작성하면 파이썬 key error가 나온다. dic[ch]에 없는값이 들어가면 안되기 떄문이다.
        # if len(stack) !=0 and dic[ch] == stack[-1]:
        #     stack.pop()
        # print(stack)

        # ch가 오른쪽괄호인 경우를 표현해주는 else문을 사용한다. 
        else :
            if len(stack) !=0 and dic[ch] == stack[-1]:
                stack.pop()


    # 삼항 연산자를 통해 작성해봄
    # return True if len(stack) == 0 else False
    return len(stack) == 0
    

def main():
    examples = ["({()})", "[]<>{}", ")(" "<]", "<(>)"]
    for example in examples:
        print(example, isParenthesisValid(example))

    
if __name__ == "__main__":
    main()