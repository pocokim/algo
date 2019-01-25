def solution(str1, str2):
    map11 =[]
    map22 =[]

    map1= []
    map2 =[]
    for i in range(len(str1)-1):
        map11.append(str1[i:i+2])

    for m in map11:
        if m.isalpha() == True:
            map1.append(m.lower())

    for i in range(len(str2)-1):
        map22.append(str2[i:i+2])
    for m in map22:
        if m.isalpha() ==True:
            map2.append(m.lower())

    print(map1)
    print(map2)

    dic1={}
    dic2={}

    for m in map1:
        dic1[m] = dic1.get(m,0)+1

    for m in map2:
        dic2[m] = dic2.get(m,0)+1

    print(dic1)
    print(dic2)

    # 합집합 
    dic3 = {}
    for ch in dic1:
        if ch in dic2:
            dic3[ch] = max(dic1[ch],dic2[ch]) 
        else :
            dic3[ch] = dic1[ch]

    for ch in dic2:
        if ch not in dic1:
            dic3[ch] = dic2[ch]
    print(dic3)

    # 교집합 
    dic4 = {}
    for ch in dic1:
        if ch in dic2:
            dic4[ch] = min(dic1[ch],dic2[ch])

    print(dic4)

    len3 = sum(dic3.values())
    len4 = sum(dic4.values())

    # print(len3,len4)
    if len3 == 0 and len4 == 0:
        return 65536

    return int(65536*(len4/len3))