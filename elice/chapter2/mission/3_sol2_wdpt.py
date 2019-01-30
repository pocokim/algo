    
# 선욱 2차 풀이 업데이트 
def wordPattern(pattern, strList):
    dic ={}
    for i in range(len(pattern)):
        if pattern[i] not in dic:
            dic[pattern[i]] = strList[i]
        else :
            if dic[pattern[i]] != strList[i]:
                return False
    
    return True 

def main():
    print(wordPattern("aabb", ["elice", "elice", "alice", "alice"])) # should return True
    print(wordPattern("abab", ["elice", "elice", "alice", "alice"])) # should return False
    

if __name__ == "__main__":
    main()
