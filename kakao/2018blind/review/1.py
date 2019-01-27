def solution(record):
    answer = []
    dic ={}
    for i in range(len(record)):
        lst = record[i].split()
        if "Enter" in record[i] or "Change" in record[i]:
            dic[lst[1]] = lst[2]
    
    # print(dic)
    
    for i in range(len(record)):
        l = record[i].split()
        if "Enter" in record[i]:
            answer.append(dic[l[1]]+'님이 들어왔습니다.')
        if "Leave" in record[i]:
            answer.append(dic[l[1]]+'님이 나갔습니다.')
            
    return answer

def main():
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))

if __name__ == "__main__":
    main()