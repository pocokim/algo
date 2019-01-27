def solution(record):
    answer = []
    namespace = {}
    # 반복되서 써지는것은 printer에 넣어서 정리 
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        # if re[0] == 'E' or re[0] == 'C':
        # if를 여러개 사용할때는 찾고자하는 대상을 배열로 생성 
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
    
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

# 굳이 프린터라는 딕셔너리를 생성해서 쓰는 테크닉을 사용할 필요까지는 없지만 printer[r.split(' ')[0]]
# 간단하게 출력할 수 있음.