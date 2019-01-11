def wordPattern(pattern, strList):
    temp =[]
    pattern2 = []
    result = []

    for i in range(len(strList)):
        if strList[i] not in temp:
            temp.append(strList[i])

    for i in range(len(strList)):
        pattern2.append(temp.index(strList[i]))
    
    # print(pattern2)

    for i in range(len(pattern)):
        result.append(ord(pattern[i])-pattern2[i])

    return result.count(result[0]) == len(result)
 
    

    
        # if strList[i] in temp:
        #     pass
        # else : 
        #     temp.append(strList[i])


    # print(pattern)


             
    # return True

def main():

    print(wordPattern("aabb", ["elice", "elice", "alice", "alice"])) # should return True
    # wordPattern("xxbb", ["elice", "elice", "alice", "alice"]) # should return True
    print(wordPattern("abab", ["elice", "elice", "alice", "alice"])) # should return False
    # wordPattern("abab", ["elice", "elice", "alice", "alice"]) # should return False
    

if __name__ == "__main__":
    main()
