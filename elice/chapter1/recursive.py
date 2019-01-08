def fibo(num):
    if num ==1:
        return 1
        # fibo(1) = 1
    elif num == 2:
        return 1
        # fibo(2) = 1
    else:
        return fibo(num-1) + fibo(num-2)
        # fibo(n) = fibo(n-1)+fibo(n-2)
    
# def summeation(num):
#     # num += summeation(num-1)
#     # if num == 1:
#     #     return 1

#     if num == 1:
#         return 1
#     elif num >=2:
#         return summeation(num-1)+ num
    


#     # if num >=1:
#     #     return summeation(num-1)+ num

def fac(num):
    if num==1:
        return 1
    else : 
        return fac(num-1)*num

def binary(num):
    if num== 0:
        return '0'
    elif num ==1:
        return '1'
    else :
        return binary(int(num/2)) + str(num%2)

    # print(str(num%2))
    # print(num/2)

def power(x, n):
    if n ==0:
        return 1
    # elif n==1:
    #     return x
    else :
        return x * power(x,n-1) 

def gcd(a,b):
    if a< b:
        # a,b = b,a 

        # a = b
        # b = a

        # 이거 2개 왜 되는거지??

        # temp = a
        # a = b
        # b = a
    else : 
        if a%b ==0 :
            return b
        else:
            return gcd(b,a%b)
        


def main():
    # for i in range(1,10):
    #     print(fibo(i))

    # # print(summeation(10))

    # print(fac(6))

    # print(binary(13))

    # print(power(3,5))

    print(gcd(42,18))

if __name__ == "__main__":
    main()
