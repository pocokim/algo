def solution(board, nums):
    answer = 0
    bingo = [0 for i in range(len(board))]
    # print(bingo)
    
    
    # 2차원 리스트에 값이 포함되어있는지 확인하는법? 
    # 2차원 배열안에 있는지는 확인을 한번에 못하는듯하다.
    # 따라서 한줄의 배열을 받아와서 확인하는수 밖에 없는닷하다. 


    # <해설풀이>
    # 순서를 고려얀하고 빙고수만 받기떄문에 nums를 set으로 바꾸면된다.
    for num in nums:
        for i in range(len(board)):
            if num in board[i]:
                board[i][board[i].index(num)] = 0
                # print(board[i].index(num))
    
    print(board)
    
    
    # for num in board:
    #     print(num)
    
    # for num in nums:
    #     print(board.count([11,13,15,16]))
    # print(board.count(num)) 이 0이출력되는것을 보아 인자가 1차원 리스트여야함
    
# 이차원배열에 포함되어있는지를 nums를 돌면서 확인하는것이 아니라 board를 돌면서 확인해야하나? 
#     for num in nums:
#         if num in board:
            
    
    
    
    
    tempD1 = []
    tempD2 = []

    # 띄어서 각각 가로, 세로, 대각선을 생각했으면 더 안했갈릴듯 
    for i in range(len(board)):
        tempC=[]
        if board[i] == bingo:
            answer +=1
            # print('가로걸림')
        for j in range(len(board)):
            tempC.append(board[j][i])
        if tempC == bingo:
            answer +=1
            # print('세로걸림')

    # for i in range(len(board)):
    #     tempC = []
    #     for j in range(len(board)):
    #         tempC.append(board[j][i])
    #     # print(tempC)
    #     if tempC == bingo:
    #         answer +=1
    #         print('세로걸림')
            
            
            
        tempD1.append(board[i][i])
        tempD2.append(board[i][len(board)-i-1])
    
    # print(tempD1)
    # print(tempD2)
    if tempD1 == bingo:
        answer +=1
        # print('대각선1걸림')
    if tempD2 == bingo:
        answer +=1
        # print('대각선2걸림')
    
    
    return answer