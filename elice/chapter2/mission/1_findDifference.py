def findDifference(str1, str2):
    # 리스트 사용 
    # str1List = list(str1)
    # str2List = list(str2)
    # str1List.sort()
    # str2List.sort()

    # str1List.append('~')

    # for i in range(len(str2List)):
    #     if str2List[i] != str1List[i]:
    #         return str2List[i]

    # 풀이 2 딕셔너리 사용     
    # dic = {}
    # for ch in str1:
    #     dic[ch] = dic.get(ch,0) + 1

    # for ch in str2:
    #     if ch not in dic:
    #         return ch
    
    str1List = list(str1)
    str2List = list(str2)
    str1List.sort()
    str2List.sort()
    
    print(str1List)
    print(str2List)
    
#     print(str2List[1])
#     print(str2List[2])

# IndexError: list index out of range 배열 범위 문제가 계속 생김. 마지막 배열에 값을 넣어주어야할듯.. 
#   elif str1List[i] != str2List[i]: 애초에 값에 i가 들어가지않음. 

    
    for i in range(len(str2List)):
        if i == len(str1List) and str1List[i] == str2List[i]:
            return str2List[-1]

        elif str1List[i] != str2List[i]:
            # print(str2List[i])
            return str2List[i]
                
            

def main():
    print(findDifference("apple", "azlppe"))
    

if __name__ == "__main__":
    main()
