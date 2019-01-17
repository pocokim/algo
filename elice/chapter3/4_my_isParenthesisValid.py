def isParenthesisValid(st):

    temp =''
    stack =[]

    for i in range(len(st)):
        print('연산전')
        print(temp)
        print(stack)
        temp +=st[i]
        if st[i] == '(' or  st[i] ==  '[' or st[i] == '{' or st[i] == '<' :
            stack.append(st[i])
        if temp[i-1] == '(' and temp[i] ==')' :
            temp[i-1]='' #그래서 그냥 빈 문자열을 넣으려고 했는데 ... TypeError: 'str' object does not support item assignment라고 뜸. 
            temp[i]=''
            # temp = temp.replace('(',' ') 이렇게 하면 i-1번째의 값만 바뀌는것이 아니라 '('가 다 바뀜 
            # temp = temp.replace(')',' ')
            stack.pop()
        elif temp[i-1] =='{' and temp[i] =='}':
            temp[i-1]=''
            temp[i]=''
            # temp = temp.replace('{','')
            # temp = temp.replace('}','')
            stack.pop()
        elif temp[i-1] =='<' and temp[i] =='>':
            temp[i-1]=''
            temp[i]=''
        elif temp[i-1] =='[' and temp[i] =='] ':
            temp[i-1]=''
            temp[i]=''
            # temp = temp.replace('<','')
            # temp = temp.replace('>','')
            stack.pop() 
        print('연산후')
        print(temp)
        print(stack)

    if len(stack) == 0:
        return True
    else:
        return False
    # for 문을 사용해야할지 while문을 사용해야할지 햇갈린다.
    # 보통 for문은 정해진 길이가 있을떄, while문은 탈출을 하고싶을떄 사용하는것같음. 이경우 

    # for문을 사용할떄 , 그리고 string in st라는 방식으로 조건문을 사용할때 i번째 인덱스에서 i-1번째의 값을 string으로는 비교하기 어려운듯하다.  만일 가능하다면 stack.pop으로 전의 값에 영향을 줄 수는 있을듯
    # for string in st:
    #     if string == '(' or  string ==  '[' or string == '{' or string == '<' :
    #         stack.append(string)
    #     if len(stack) != 0 and (string ==')' or string ==']' or string =='}' or string =='>'):
    #         stack.pop()
    #     print(stack)

    
             
    # 문제점 1) <) 도 다른괄호가 아닌 같은괄호로 처리해버림.

    # 마지막에 stack에 배열이 남아있다면 false고 아니라면 true를 리턴하는 식으로 짜면 될것같음. 만일 이런식으로 짠다면.. 
    # 근데 애초에 스택의길이로 반환하는게 아니라, 스택에 안들어가면 return false로 접근할 수 있을것같음. 


    
def main():
    examples = ["({()})", "[]<>{}", ")(" , "<]", "<(>)"]
    for example in examples:
        print(example, isParenthesisValid(example))

    # ans = 'i loveyou'
    # ans = ans.replace('i','I')
    # print(ans)
    
if __name__ == "__main__":
    main()