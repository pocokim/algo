# count = 0

def convertTo1(num):
    # if num ==1:
    #     return count
    # else :
    #     global count
    #     count +=1 
    #     convertTo1(num-1)
    
        
#     elif num !=1 and num%2 !=0 and num%3 !=0 :
#         count +=1 
#         convertTo1(num-1)
#     elif num !=1 and num%2 ==0 and num%3 !=0:
#         count +=1
#         min(convertTo1(num/2),convertTo1(num-1))
#     elif num !=1 and num%2!=0 and num%3 ==0:
#         count +=1
#         min(convertTo1(num/3),convertTo1(num-1))
#     elif num !=1 and num%2==0 and num%3 ==0:
#         count +=1
#         min(convertTo1(num/2),convertTo1(num/3))
    

def main():
    print(convertTo1(2))

if __name__ == "__main__":
    main()
