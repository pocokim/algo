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


# def wordPattern(pattern, strList):
#     temp =[]
#     pattern2 = []
#     result = []
    
#     temp2 =[]
#     newpattern =[]
    
#     for i in range(len(strList)):
#         if strList[i] not in temp:
#             temp.append(strList[i])
  
#     #위의 for문은 strList의 원소를 temp에 저장하였고
    
#     for i in range(len(strList)):
#         pattern2.append(temp.index(strList[i]))
        
#     # print(pattern2)
        
#     for i in range(len(pattern)):
#         if pattern[i] not in temp2:
#             temp2.append(pattern[i])
    
#     for i in range(len(pattern)):
#         newpattern.append(temp2.index(pattern[i]))
        
#     # print(newpattern)
    
#     return pattern2 == newpattern
        
    
#     # strList에서 for문을 돌면서 각 배열의 값이 temp의 어떤 위치에있는지 확인한 후에 
    
#     # print(pattern2)

# #     for i in range(len(pattern)):
# #         result.append(ord(pattern[i])-pattern2[i])

# #     return result.count(result[0]) == len(result)
    
    
    
#     # 패턴2의 모든 원소와 패턴1의 모든원소의 아스키코드값차이가 일치하는지를 확인하고 일치하면 return tru
    
#     # 그런데 이 경우에 aabb , aabbc 와 같은경우는 해결이 잘 되는데 ... 
#     # xxbb와 같은경우에는 통과하지를 못합니다. 
 
#     # 그렇군요.
#     # 혹시 pattern에도 strlist와 같은 처리를 한다면
#     # aabb -> [0, 0, 1, 1]
#     # xxbb -> [0, 0, 1, 1]
#     # 와 같은 결과가 나오지 않을까요?
    
#     #이것도 하나의 방법이 될 수 있을 것 같아요.

#     # 아 그러네요.. 네네 그렇게 해결할 수 있을것같아요.
#     # 그리고 제가 푼 방법말고, 원래 이 문제의 전형적인 해결방법을 조금 여쭤보고 싶네요. 
    
#     # 정확히 알려드리긴 힘들지만 힌트를 드리자면
#     # 2장의 3번째 수업에 있는 해쉬를 사용하는 방법이 있습니다.
#     # "aabb"와 같은 문자열에서 a나 b를 키로
#     # "elice"와 같은 문자를 값으로 사용해 저장하다가
#     # 패턴에 안맞는 부분이 생긴다면 False 패턴에 잘 맞아 떨어진다면 True를 리턴하는 방식입니다.
    
#     # 안그래도 dictionary를 사용해서 풀어보려고 했었는데... 역시 해쉬를 통해서 접근하는 방법을 사용하는군요
#     # 그런 방법으로 한번 더 고민해보도록하겠습니다.


        
        

        
# def main():
#     print(wordPattern("aabb", ["elice", "elice", "alice", "alice"])) # should return True
#     print(wordPattern("abab", ["elice", "elice", "alice", "alice"])) # should return False
    

# if __name__ == "__main__":
#     main()
