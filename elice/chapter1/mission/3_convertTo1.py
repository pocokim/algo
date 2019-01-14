
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

# 2019.1.10
#     두번 다 수행하지만 첫번째 if문에서 min_cnt[int(i/3)]+1가 들어가게 되더라도 두번째 if문에서 min_cnt[i]를 사용하기 때문에 누락되지 않고 사용하게 됩니다.
    
#     동준님께서 설명해주신 이 멘트의 의미를 잘 모르겠습니다. ㅠㅠ 제 생각에는...
#     파이썬에서는 swap을 a,b = b,a 이렇게 하더라구요. 
#     # 넵 기억합니다!
    
#     # 음.... 예를 들어 설명해 드리도록 
# 하겠습니다.
#     #min_cnt[i-1]+1 이 7, min_cnt[int(i/3)]+1이 5, min_cnt[int(i/2)]+1 이 10 이라고 가정해 보겠습니다.
    
#         if i%3 ==0:
#             min_cnt[i] = min(min_cnt[i-1]+1,min_cnt[int(i/3)]+1)
#             # 이 부분을 지나고 나면 min_cnt[i]은 5가 됩니다. 이해되시나요? 넵
#         if i%2 ==0:
#             min_cnt[i] = min(min_cnt[i-1]+1,min_cnt[int(i/2)]+1)
#             # 하지만 이 부분을 지나고 나면 min_cnt[i] = min(7, 10)과 다름없는지라
#             # 진짜 최소값인 5가 사라지고 min_cnt[i]은 7이 됩니다.
            
            
            
#             # 크... 그러네요..... 근데 제가 궁금한게 
#         #넵 그러합니다 ㅋㅋ
#         # min_cnt[i-1]+1 대신 min_cnt[i]을 적으면 진짜 최소값이 사라지지 않겠지요
        
        
        
#         def convertTo1(num):

#     min_cnt = [ i-1 for i in range(num+1)]

#     for i in range(1,num+1):
#         min_cnt[i] = min_cnt[i-1]+1
#         if i%3 ==0:
#             min_cnt[i] = min(min_cnt[i],min_cnt[int(i/3)]+1)
#         if i%2 ==0:
#             min_cnt[i] = min(min_cnt[i],min_cnt[int(i/2)]+1)

#     return min_cnt[-1]
        
#         #여기서 min_cnt[i] = min(min_cnt[i],min_cnt[int(i/3)]+1)
#         왼쪽에도 min_cnt[i]가 들어가고 오른쪽에도 min_cnt[i]가 들어가잖아요.
        
        
#         # 그 부분은 설명드리자면, min(min_cnt[i],min_cnt[int(i/3)]+1)이 먼저 해당 변수의 값으로 바뀌어 계산되는 것과 비슷하게 동작합니다.
        
#         #예를 들어 min_cnt[i]이 10이라면
#         #min_cnt[i] = min(min_cnt[i],min_cnt[int(i/3)]+1)
#         #은 min_cnt[i] = min(10,min_cnt[int(i/3)]+1) 처럼 계산되기에 min_cnt[i]값이 바뀐다고 오른쪽의 min_cnt[i] 이 영향을 받지는 않습니다.
        
        
        
#         # 충분한 답변이 되셨나요?
        
        
        
#         네 그러면. 제가 파이썬 공부하면서 좀 신기했던게.. 원래 c언어에서는 swap할때
#         temp = a
#         a = b
#         b = a이렇게 하던데 파이썬은 a= b , b= a이렇게 하더라구요. 
#         오른쪽의 변수는 값을 가르킨다고 생각하면 될까요? 
        
#          min(min_cnt[i],min_cnt[int(i/3)]+1)이 먼저 해당 변수의 값으로 바뀌어 계산되는 것과 비슷하게 동작합니다.
#          라고 말씀하셨던것처럼... 그리고 이 부분에 대해서는 제가 공부해도 괜찮을것같아서.. (동준님 시간뺐는것도 죄송하고)
#          혹시 구글링할만한 키워드를 알려주신다면 제가 공부해보겠습니다!
#          # 네 맞습니다. 
        
#         a= b , b= a는 혹시 a, b = b, a를 말씀하신건가요?
#         혹시 그렇다면 위의 설명드린 것과 같은 맥락입니다.
#         a가 10, b가 5일때
#         a, b = b, a -> a,b = 5, 10 처럼 동작하게 되는 것이죠.
        
#         이부분에 대해 공부할만한 키워드가..... 음 정확히 어떻게 검색해야 할지는 모르겠습니다만
        
#         엘리스의 도레미 파이썬이나 파이썬 기초I과 같은 과목이 도움이 되지 않을까 합니다.
#         한번 파이썬의 대입 연산자에 대해 검색해 보시는것도 어떨가 하네요.

  
    
#     if num == 1:
#         return 0
#     if num%3 == 0:
#         return min(1 + convertTo1(num/3), 1+ convertTo1(num-1))
#     elif num %2 == 0:
#         return min(1 + convertTo1(num/2), 1+ convertTo1(num-1))
#     else :
#         return 1+ convertTo1(num-1)

# # 재귀함수로 접근하게 된다면 10->9->8->7->6->5...와같은식으로 5에 1번, 10->5와같이 5에 2번 접근하게 됩니다.
# # 위의 예시는 굉장히 간단한 예시로 아주 큰 숫자를 가지고 테스트를 한다면 훨씬 많은 중복된 접근이 생길 것이고 이로 인해 시간초과가 나게 됩니다.
# # 크게 두가지 방법이 있습니다.
# # 1) 재귀함수 내에 num이 호출될때 저장해두고 사용하는 방법이 있습니다.
# # 예를들어 처음 convertTo1(5)가 호출될때는 코드대로 계산하고 새롭게 호출된다면 배열같은곳에 저장된 값을 그대로 리턴하는 방법이 있습니다.
# # 2) 아예 재귀함수가 아닌 방법으로 접근하는것도 방법이 될 수있습니다. 한번 다른방법도 고민해보시는 것이 좋을 것 같습니다.
    
# 동적프로그래밍을 사용하기 위해서는 i번째를 저장하기위해서 배열을 만들고 for문을 돌려야할듯 



def main():
    # print(convertTo1(10))
    for i in range(1,150):
        print(convertTo1(i))   


        


    # print(min_cnt)     

if __name__ == "__main__":
    main()
