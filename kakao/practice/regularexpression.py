data = """
park 800905-1049118
kim  700905-1059119
""" 
# 1. 여러줄 문자열은 큰따옴표3개를 붙여쓴다. 

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        # print(line)
        # print(word)
        word_result.append(word)
        # print(word_result) 

# 스페이스는 리스트에 들어가지만 여러줄문자열의 첫번째는 들어가지 않는다? 들어가는데 개행되서 그렇다. word_result가 바뀌기 떄문이다.

        # print(" ".join(word_result))
    result.append(" ".join(word_result))
    # print(result)
print("\n".join(result))

newData = data.split("\n") 
# print(newData)
# 2. 여러줄 문자열에서는 처음의 빈 줄도 데이터로 들어간다. 

# for line in data.split('\n'): # 이라고 하면 data.split('\n') 에서 이미 리스트를 만들어버린다. 

# for line in data.split('\n'):
#     for word in line.split(" "):
#         # 공백을 기준으로 라인의 문자들을 저장한다. 
#         if len(word) == 14:
#             print(word[:6].isdigit()) #  isdigit()은 문자열이 숫자로 구성되어있는지를 나타내는 함수 

#3. join은 문자열을 삽입해주는 함수이지만 문자열이 아니라 리스트와 튜플에서도 사용가능하다.
#4. join은 문자열을 리턴한다. 즉 리스트를 문자열로 바꿀 수 있다. 

