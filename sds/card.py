testcase = int(input())

for j in range(1,testcase+1):
    len = int(input())
    bag= input().split()


    word = bag[0]



    for i in range(1,len):
        word1 = word+bag[i]
        word2 = bag[i]+word

        if ord(word[0]) > ord(bag[i]):
            word = word1
        elif ord(word[0]) <ord(bag[i]):
            word = word2 
        else :
            word = word2
        
        
    print("#"+str(j)+" "+word)    