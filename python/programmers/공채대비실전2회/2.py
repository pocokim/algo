import math
def solution(l, v):    
    v.sort()

    dif = []
    for i in range(1,len(v)):
        dif.append(v[i] - v[i-1])
    
    longd = max(dif)
    
    # 배열이 비어있는 경우 
    try:
        longd = max(dif)
    except:
          # 런타임에러의 이유  : 효율성 만점인데 런타임에러면 오류가있어서 런타임에러
        longd = 0
    
    return max(math.ceil(longd/2),v[0],l-v[-1])
    
    
    # (v[i] - v[i-1] + 1)//2 을 사용하면 math모듈 쓸 필요없음.


    # 그리디를 사용하기 보다는, 가장 차이가 큰놈을 찾을수 있다는 생각이 들어서 그렇게 풀었는데 사실상 그게 그리디 
    # 이분탐색으로도 풀 수 있다. 길이를 점점 줄여나가면서 ans값을 적게 만드는 방법인데 아직은 이해가 잘 안간다.

def main():
    print(solution(8,[3]))

if __name__ == "__main__":
    main()
