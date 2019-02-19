import numpy 

N, K = map(int,input().split())
likes = list(map(int,input().split()))
mean = []
for cnt in range(K,N+1):
    for i in range(0,N-cnt+1):
        mean.append(numpy.std(likes[i:i+cnt]))

print(min(mean))


