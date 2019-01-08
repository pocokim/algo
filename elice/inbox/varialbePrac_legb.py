# # x= 10
# # y= 11
# def foo():
#     x = 20
#     def bar():
#         x= 50
#         a= 30
#         print(a,x,y)
#     bar()
#     x= 40
#     bar()
# foo()

def calc2():
    total2 = 0
    a= 10
    b= 20
    def add2():
        total2 =a+b
        return total2

    
    print(add2())
    print(total2)
    
calc2()
    


# def calc():
#     total = 0    # calc의 지역 변수
#     def add(a, b):
#         total = total + a + b    # add의 지역 변수 total을 사용하려고 해서 에러 발생
 
#     add(10, 20)
#     add(30, 40)
#     print(total)
 
# calc()