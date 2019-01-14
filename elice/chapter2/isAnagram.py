def isAnagram(str1, str2):

    # # 풀이 1 : 리스트 소팅
    #     str1List = list(str1)
    #     str2List = list(str2)
        
    #     str1List.sort()
    #     str2List.sort()
        
    #     return str1List == str2List
        
        dic1 = {}
        for ch in str1:
            dic1[ch] = int(dic1.get(ch,'0')) + 1 # 없으면 0을 있으면 갯수를 
    # 풀이3  : 딕셔너리 2개 비교 
    #     dic2 = {}
    #     for ch in str2:
    #         dic2[ch] = int(dic2.get(ch,'0')) +1 
        
    #     return dic1== dic2

    # 풀이 2 : 딕셔너리 1개 만들고 문자열과 딕셔너리 비교 
        for ch in str2:
            if ch in dic1:
                if dic1[ch] != 0:
                    dic1[ch] -=1
                    # print(dic1)
                elif dic1[ch] == 0: return False
            else : return False
        return True 



    # 풀이 4 안좋은풀이 
    # str1 =','.join(str1)
    # str1 = str1.split(',')
    
    # str2 = ','.join(str2)
    # str2 = str2.split(',')
    # print(str1)

    # for i in range(len(str1)):
    #     str1[i] = ord(str1[i])
    
    # for i in range(len(str2)):
    #     str2[i] = ord(str2[i])
    
    # str1.sort()
    # str2.sort()

    # if str1 == str2:
    #     return True
    # else : 
    #     return False
    
    # print(str1)
    # return ''

def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle')) # should return True
    print(isAnagram('cat', 'cap')) #should return False
    

if __name__ == "__main__":
    main()
