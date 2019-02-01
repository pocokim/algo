from random import sample

def finder(ip,quiz):
    st = 0
    ball = 0
    for i in range(len(ip)):
        if ip[i] == quiz[i]:
            st +=1
        elif ip[i] in quiz:
            ball +=1
    return [st,ball]

def printer(lst):
    if lst[0] == 0 and lst[1] == 0:
        print('낫씽') 
    elif lst[0] != 0 and lst[1] !=0:
        print('%s 스트라이크 %s볼'%(lst[0],lst[1]))
    elif lst[1] != 0 and lst[0] == 0:
        print('%s볼'%lst[1])
    elif lst[0] != 0 and lst[1] == 0:
        print('%s 스트라이크'%lst[0])

def main():    
    q = list(map(str,sample(range(1,10),3)))

    while True:
        ipt = input('숫자 입력 : ')
        printer(finder(ipt,q))
        if finder(ipt,q) == [3,0]:
            print('3개의 숫자를 모두 맞추셨습니다. 게임종료!')
            break

if __name__ == '__main__':
    main()


    