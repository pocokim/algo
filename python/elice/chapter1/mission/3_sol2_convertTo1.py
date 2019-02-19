dictionary = {
    1: 0
}

def convertTo1(num):
    if num in dictionary:
        return dictionary[num]
    # 메모이제이션을 하는 타이밍이 잘못된것인가? 
    # 4-2 피보나치문제를 풀때처럼 dic에 있는지 확인하고 있으면 가져오는 식을 추가했는데
    # 왜 메모이제이션이 안일어나는지 궁금하다. 
    # 복습할때 count를 인자로 받아서 재귀함수가 몇번 실행되는지 확인해보자.
    
    else :
        if num %3 == 0:
            output = min(1 + convertTo1(num/3), 1+ convertTo1(num-1))
            dictionary[num] = output
            return output
        
        elif num %2 == 0:
            output = min(1 + convertTo1(num/2), 1+ convertTo1(num-1))
            dictionary[num] = output
            return output  

        else :
            output = 1+ convertTo1(num-1)
            dictionary[num] = output
            return output

# # 재귀함수로 접근하게 된다면 10->9->8->7->6->5...와같은식으로 5에 1번, 10->5와같이 5에 2번 접근하게 됩니다.
# # 위의 예시는 굉장히 간단한 예시로 아주 큰 숫자를 가지고 테스트를 한다면 훨씬 많은 중복된 접근이 생길 것이고 이로 인해 시간초과가 나게 됩니다.
# # 크게 두가지 방법이 있습니다.
# # 1) 재귀함수 내에 num이 호출될때 저장해두고 사용하는 방법이 있습니다.
# # 예를들어 처음 convertTo1(5)가 호출될때는 코드대로 계산하고 새롭게 호출된다면 배열같은곳에 저장된 값을 그대로 리턴하는 방법이 있습니다.
# # 2) 아예 재귀함수가 아닌 방법으로 접근하는것도 방법이 될 수있습니다. 한번 다른방법도 고민해보시는 것이 좋을 것 같습니다.

def main():
    for i in range(1,150):
        print(convertTo1(i))


if __name__ == "__main__":
    main()
