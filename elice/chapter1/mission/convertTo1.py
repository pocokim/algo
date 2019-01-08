
def convertTo1(num):

    min_cnt = [ i-1 for i in range(num+1)]
    # 실제로 i는 1부터 시작하지만 배열은 0부터 시작하므로 index 조정을 위해서 일부로 0번쨰 index를 추가함. 

    for i in range(1,num+1):
        min_cnt[i] = min_cnt[i-1]+1
        if i%3 ==0:
            min_cnt[i] = min(min_cnt[i],min_cnt[int(i/3)]+1)
            # min_cnt[i] = min(min_cnt[i-1]+1,min_cnt[int(i/3)]+1)
        if i%2 ==0:
            # min_cnt[i] = min(min_cnt[i-1]+1,min_cnt[int(i/2)]+1)
            min_cnt[i] = min(min_cnt[i],min_cnt[int(i/2)]+1)
    return min_cnt[-1]



    # min_cnt = [i-1 for i in range(1,num+1)]
    
    # for i in range(1,num+1):
    #     if (i+1)%3 == 0:
    #         min_cnt[i] = min(1+min_cnt[i-1],1+min_cnt[int(i/3)])
          
    #     if (i+1)%2 == 0:
    #         min_cnt[i] = min(1+min_cnt[i-1],1+min_cnt[int(i/2)])
            
  

    # if num == 1:
    #     return 0
    # if num%3 == 0:
    #     return min(1 + convertTo1(num/3), 1+ convertTo1(num-1))
    # elif num %2 == 0:
    #     return min(1 + convertTo1(num/2), 1+ convertTo1(num-1))
    # else :
    #     return 1+ convertTo1(num-1)

# 재귀함수로 접근하게 된다면 10->9->8->7->6->5...와같은식으로 5에 1번, 10->5와같이 5에 2번 접근하게 됩니다.
# 위의 예시는 굉장히 간단한 예시로 아주 큰 숫자를 가지고 테스트를 한다면 훨씬 많은 중복된 접근이 생길 것이고 이로 인해 시간초과가 나게 됩니다.
# 크게 두가지 방법이 있습니다.
# 1) 재귀함수 내에 num이 호출될때 저장해두고 사용하는 방법이 있습니다.
# 예를들어 처음 convertTo1(5)가 호출될때는 코드대로 계산하고 새롭게 호출된다면 배열같은곳에 저장된 값을 그대로 리턴하는 방법이 있습니다.
# 2) 아예 재귀함수가 아닌 방법으로 접근하는것도 방법이 될 수있습니다. 한번 다른방법도 고민해보시는 것이 좋을 것 같습니다.
    
# 동적프로그래밍을 사용하기 위해서는 i번째를 저장하기위해서 배열을 만들고 for문을 돌려야할듯 



def main():
    print(convertTo1(10))
    # for i in range(1,14):
    #     print(convertTo1(i))   

    # a = int(input()) + 1

    # min_cnt = [ -1 for i in range(a)] 

    # for i in range(1,a):
    #     print(min_cnt)
    #     min_cnt[i] = min_cnt[i-1] + 1
    #     if i % 2 == 0:
    #         min_cnt[i] = min([min_cnt[i], min_cnt[int(i/2)]+1])
    #     if i % 3 == 0:
    #         min_cnt[i] = min([min_cnt[i], min_cnt[int(i/3)]+1])
    #     print(min_cnt)
        


    # print(min_cnt)     

if __name__ == "__main__":
    main()
