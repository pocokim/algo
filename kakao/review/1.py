def finder(num,arr1,arr2):
    temp = []
    for i in range(num):
        # 한번에 비트연산 가능 
        line = bin(arr1[i] | arr2[i])
        line = line[2:]

        # 문자열을 조작할때는 항상 조작후의 변수를 선언해주어야한다. 
        make0inline =line.zfill(num) 

        # 문자열의 값을 str[5] = 6 이렇게 바꾸지는 못함. make0inline 문자열은 바꿀 수 없음. 새로운 문자열 m1을 만들떄 1을 #으로 바꿔서 만든다는 뜻.
        m1 = make0inline.replace('1','#')
        m2 = m1.replace('0',' ') 


        temp.append(m2)
        
    
    
    return temp    



print(finder(5,[9, 20, 28, 18, 11],	[30, 1, 21, 17, 28]))  # ["#####","# # #", "### #", "# ##", "#####"]
print(finder(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])) # ["######", "### #", "## ##", " #### ", " #####", "### # "]