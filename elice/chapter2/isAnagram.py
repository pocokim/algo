def isAnagram(str1, str2):
    # str1List = list(str1)
    # join , split 을 안쓰고도 list()로 문자열을 리스트로 만들 수 있음..
    


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
