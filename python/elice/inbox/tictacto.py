# m,n = input().split()
# m, n = [int(x) for x in [m,n]]


matrix = [[" "]*3 for i in range(3) ]
dol = ['0','X']
turn = 0


def matrix_print() :
    for i in range(3):
        print("───┼───┼───┼───┤")
        print(str(i+1)+"  │ ", end="")
        for j in range(3):
            print(matrix[i][j]+" │ ", end="")
        print("")
    print("───┴───┴───┴───┘")

# print(matrix[0][0])
# print(matrix)
# print(matrix[m-1][n-1])
# print(matrix[m-1])

def matrix_fill():
    if x.isalpha() == False:
        print("You input wrong value. You must input a alphabet for X.")
    elif x != 'A' and x != 'B' and x != 'C':
        print("You input wrong value. Your input value for X must between A to C.")
    else:
        if y.isnumeric() == False:
            print("You input wrong value. You must input a numeric value for Y.")
        elif y != '1' and y != '2' and y != '3':
            print("You input wrong value. Your input value for Y must between 1 to 3.")
        else:
            matrix[int(ord(input_coor[0])-65)][int(input_coor[1])-1] = dol[turn]

for i in range(9):
    input_coor = input("Input coordinate for new marker : ")
    x = input_coor[0]
    y = input_coor[1]
    print("(" + input_coor[0] + ", " + input_coor[1] + ") is your input.")

    matrix_fill()
    matrix_print()

    turn = 1 - turn 

    

# if input_coor[0] == 'A' or 'B' or 'C' :
#     if input_coor[1] == '1' or '2' or '3':
#         matrix[int(ord(input_coor[0])-65)][int(input_coor[1])-1] = "0"
 


        
        

    
    

# print("  │A │B │C │")
# print("──┼──┼──┼──┤")
# print("1 │"+matrix[0][0]+" │"+matrix  │  │")
# print("──┼──┼──┼──┤")
# print("2 │  │  │  │")
# print("──┼──┼──┼──┤")
# print("3 │  │  │  │")
# print("──┴──┴──┴──┘")
