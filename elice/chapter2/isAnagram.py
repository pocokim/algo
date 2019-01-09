def isAnagram(str1, str2):
    str1 =','.join(str1)
    str1 = str1.split(',')
    
    str2 = ','.join(str2)
    str2 = str2.split(',')

    for i in range(len(str1)):
        str1[i] = ord(str1[i])
    
    for i in range(len(str2)):
        str2[i] = ord(str2[i])
    
    str1.sort()
    str2.sort()

    if str1 == str2:
        return True
    else : 
        return False
    
    # print(str1)
    # return ''

def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle')) # should return True
    print(isAnagram('cat', 'cap')) #should return False
    

if __name__ == "__main__":
    main()
