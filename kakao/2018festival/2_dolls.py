import math 

N, K = map(int,input().split())
likes = list(map(int,input().split()))
temp = []
for cnt in range(K,N+1):
    for i in range(0,N-cnt+1):
        boon =[]

        temp = likes[i:i+cnt]
        if len(temp) != 0:
            mean = sum(temp)/len(temp)
        
    
        # sum 변수를 선언하면 typeError 
        s = 0
        for j in range(i,i+cnt):
            s += math.pow(likes[j]-mean,2)
        boon.append(math.sqrt(s/cnt))

print(min(boon))



