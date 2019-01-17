# class Fib():
#     def __init__(self):
#         self.memo = {}

#     def fibonacci(self, num):
#         if num ==0:
#             self.memo[num] = 0
#         if num ==1 or num == 2: 
#             self.memo[num] = 1
#         elif num >=3 :
#             self.memo[num] = self.fibonacci(num-1) + self.fibonacci(num-2)
#         return self.memo[num]

        # 문제점1)
        #  self.memo[num] = fibonacci(num-1) + fibonacci(num-2)
        # NameError: name 'fibonacci' is not defined 라는 에러가 생긴다. 
        # 클래스에서 재귀를 사용하려면 fibonacci(num-1) 가 아니라 self.fibonacci(num-1)을 사용해야한다.

        # 문제점 2) 
        # 과연 이게 메모이제이션이 잘 된건가.. 싶긴하다. 잘되지 않았다. 먼저 5를 부르면 4와 3을 호출하는 식으로 , 저장은 하지만 메모이제이션은 안되는 그런 상태인것이다. 
        # 즉 메모이제이션을 위해서는 있으면 사용하라! 라는 코드가 있어야한다.
        # 그게 바로 아래의 코드 
        
        #    if num in self.memo:
        #         return  self.memo[num]


class Fib():
    def __init__(self):
        self.memo = {}

    def fibonacci(self, num):
        if num ==0:
            self.memo[num] = 0
        if num ==1 or num == 2: 
            self.memo[num] = 1
        elif num >=3 :
            if num in self.memo:
                return  self.memo[num]

            self.memo[num] = self.fibonacci(num-1) + self.fibonacci(num-2)
        return self.memo[num]


        
 
# def fibonacci(num):
#     if num == 0:
#         return 0
#     if num == 1 or num ==2 :
#         return 1
#     elif num >= 3:
#         return fibonacci(num-1) + fibonacci(num-2)
    
def main():
    a = Fib()
    print(a.fibonacci(10))

    # print(fibonacci(10)) # should return 55

if __name__ == "__main__":
    main()