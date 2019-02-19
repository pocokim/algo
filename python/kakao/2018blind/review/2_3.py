def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    A = sorted(result, key=lambda x : result[x], reverse=True)
    print(A)
    # result(딕셔너리)를 소팅하는건데 result[x]값을 기준으로 소팅을 함. 출력되는건 정렬된 딕셔너리가 아니라 정렬된 리스트
    # 딕셔너리를 소팅하고, 소팅의 대상이 result의 키값이기 떄문에 

def main():
   print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
   print(solution(4, [2,1,2,1,1]))


if __name__ == "__main__":
    main()