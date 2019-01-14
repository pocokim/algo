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
    dic = {}
    for ch in str1:
        dic[ch] = dic.get(ch,0) + 1

    for ch in str2:
        if ch not in dic:
            return ch

def main():
    print(findDifference("apple", "azlppe"))
    

if __name__ == "__main__":
    main()
