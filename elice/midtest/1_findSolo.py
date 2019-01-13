def solution(nums):
    for i in range(1,int(((len(nums)+1)/2))+1):
        if nums.count(i) !=2 :
            return i


def main():
    print(solution([1, 5, 3, 1, 2, 6, 4, 5, 2, 6, 3]))
    
if __name__ == "__main__" :
    main()
