# 50분 

def solution(N, stages):

    # 2중 for문 
    n = [0 for i in range(N+2) ]
    for stage in stages:
        n[stage] += 0
        for i in range(1,stage):
            n[i] += 1
    
    print(n)
    
    live = n[1:len(n)-1]
    print(live)
    
    die = [len(stages)-live[0]]
    
    for i in range(1,N):
        die.append(live[i-1]-live[i])
        
    print(die)
    
    ans = []
    for i in range(N):
        ans.append(die[i]/(live[i]+die[i]))

    print(ans)
    
    answer = []
    
    for i in range(N):
        answer.append(ans.index(max(ans))+1)
        # print(answer)
        ans[ans.index(max(ans))] = -1
    
    return answer
#     for i in range(0,N-1):
#         member.append(member[i]-n[i+1])
        
#     print(member)
    
    
    
    answer = []
    return answer