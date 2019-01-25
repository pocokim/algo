# 57분 

def solution(record):
    answer = []
    dic={}

    for message in record:
        mList = message.split(" ")
    
        
        if mList[0] == 'Enter':
            answer.append(mList[1]+"님이 들어왔습니다.")
            dic[mList[1]] = mList[2]
        if mList[0] == 'Leave':
            answer.append(mList[1]+"님이 나갔습니다")
        if mList[0] == 'Change':
            dic[mList[1]] = mList[2]
        
        print(answer)
        print(dic)


    # 아이디를 닉네임으로 바꿔주기    
    for i in range(len(answer)):
        for ch in dic:
            if ch in answer[i]:
                answer[i] = answer[i].replace(ch,dic[ch])
                
    print(answer)

# def solution(record):
#     answer = []
#     dic={}

#     for message in record:
#         mList = message.split(" ")
    
        
#         if mList[0] == 'Enter':
#             answer.append(mList[1]+'님이 들어왔습니다.')
#             dic[mList[1]] = mList[2]
#         if mList[0] == 'Leave':
#             answer.append(mList[1]+'님이 나갔습니다')
#         if mList[0] == 'Change':
#             dic[mList[1]] = mList[2]
        
#         print(answer)
#         print(dic)
        
#     for i in range(len(answer)):
#         if '들어왔습니다' in answer[i] :
#             for ch in dic:
#                     answer[i] = dic[ch]+'님이 들어왔습니다.'
#         if '나갔습니다' in answer[i] :
#             for ch in dic:
#                     answer[i] = dic[ch]+'님이 나갔습니다.'
    
#     return answer