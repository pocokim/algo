def hanoi(height) :
    result = []
    
    def move(begin, end, height):
        temp = 6- begin - end # temp를 처리하는방법 어떻게 나머지를 뺴야하는지 고민하고있었음.
       
        # if height == 1:
        #     result.append(begin,end)
        
        if height == 0:
            return 
            # pass를 써도됨.
            
        else :
            move(begin,temp,height-1)
            result.append((begin,end))
            move(temp,end,height-1)
        return result

    move(1,3,height)
    return result

#처음에 횟수를 새는문제인줄 알고 count를 선언해서 더해주려고 했음.
# count를 함수의 변수로 넣지 않는이상 재귀함수에서 count를 사용할 수 없다.
    
            
def main():
    print(hanoi(3))

if __name__ == "__main__":
    main()
