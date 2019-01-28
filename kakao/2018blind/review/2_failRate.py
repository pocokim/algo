import operator

def solution(N, stages):
    answer = []
    
    die = []
    for i in range(1,N+1):
        die.append(stages.count(i))
    
    live = [len(stages)]
    for j in range(1,N):
        live.append(live[j-1]-die[j-1])
    # 너무 list out of range 못맞추는듯.

    
    # index를 찾는데 시간복잡도가 n만큼 걸리므로 여기서 시간복잡도가 오래걸린다.
    # answer = []
    # for i in range(N):
    #     answer.append(ans.index(max(ans))+1)
    #     ans[ans.index(max(ans))] = -1
    
    # return answer

    # 시간복잡도를 낮추기 위해 딕셔너리를 만들었고 딕셔너리를 정렬하였음. 
    ans = {}
    for i in range(N):
        if live[i] != 0:
            ans[i+1] = die[i]/live[i] 
        else : 
            ans[i+1] = 0
    
    A = sorted(ans.items(),key=operator.itemgetter(1),reverse=True)
    print(A)

    for dic in A:
        answer.append(dic[0])
    return answer
    
    # for i in range(N):
    #     answer.append(A[i][0])
    # return answer
    

def main():
#    print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
   print(solution(4, [2,1,2,1,1]))


if __name__ == "__main__":
    main()