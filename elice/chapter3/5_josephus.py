import queue

# 큐의장점 
# 배열은 인덱스가 계속 바뀌지 않지만 
# 큐를 사용하면 뽑았다가 다시 넣는경우 인덱스가 계속 바뀌는것을 고려할 수 있음.

def josephus(num, target):
    q = queue.Queue()
    temp = []
    
    for i in range(1,num+1):
        q.put(i)
    



    # 처음에 while문 생각하지 못하고 짬 근데 한번만 도네?
    # for i in range(1,target+1):
    #     value = q.get()
    #     if i != target:
    #         q.put(value)
    #     if i == target:
    #         return value

    # 그래서 while문으로 작성해봄.
    while q.qsize() !=0 :
        # print(q.qsize())
        for i in range(1,target+1):
            value = q.get() 
            if i != target:
                q.put(value) 
            if i == target:
                temp.append(value)
                

            
    return temp
    
    # def josephus(num, target):
    # q = queue.Queue()
    # temp = []
    # for i in range(1,num+1):
    #     q.put(i)
    
    # for i in range(num):
    #     for j in range(target-1):
    #         a= q.get()
    #         q.put(a)
    #     temp.append(q.get())
        
        
    


def main():
    print(josephus(7, 3)) #[3, 6, 2, 7, 5, 1, 4]이 반환되어야 합니다

if __name__ == "__main__":
    main()
