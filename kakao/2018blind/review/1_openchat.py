def solution(record):
    answer = []
    dic ={}
    for i in range(len(record)):
        if "Enter" in record[i] or "Change" in record[i]:
            status,id,nickname = record[i].split()
            dic[id] = nickname

    # for re in record: 레코드의 한줄한줄을 re로 받고, 
    #     if re[0] == 'E' or re[0] == 'C': 앞글자만 확인하여 구분하고 
    #         op, userid, nickname = re.split() : split한것을 변수에 명시적으로 표현하여 알아보기 쉽게 적었다.
    #         users[userid] = nickname
    
    
    # i로 받을 필요없이 , for re in record 로 나누고 re.split()를 사용하는게 더 파이썬 적인 풀이인듯하다.
    for i in range(len(record)):
        l = record[i].split()
        # who = record[i].split()[1] 로 미리 명시적으로 변수를 표현할 수 있다. 
        if "Enter" in record[i]:
            answer.append(dic[l[1]]+'님이 들어왔습니다.')
        if "Leave" in record[i]:
            answer.append(dic[l[1]]+'님이 나갔습니다.')
            
    return answer

def main():
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))

if __name__ == "__main__":
    main()