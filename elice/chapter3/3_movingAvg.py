import queue

class MovingAvg(): # 클래스는 인자를 받을수도 있는듯 
    def __init__(self, size):
        self.size = size 
        self.queue = queue.Queue() # 큐를 연결시키기위해서 self.queue를 만듦
        # 변수를 연결시켜주기 위해서 다시 self.sum이라는 변수를 만듦. <- 처음풀때 이생각을 못함 
        self.sum = 0 

    def nextVal(self, num):
        # self.num = num
        # m = queue.Queue() # 선언을 여기서 하면 안됨. 함수가 불러질때마다 m이 사용됨.
        # m.put(num)
        # if m.qsize() == self.size:
        #     m.get()
        # print(m.get())
        
        
        self.queue.put(num)
        self.sum += num # 우선 다 더하고 

        if self.queue.qsize() == self.size+1:
            self.sum -= self.queue.get() # 큐에서 빠지는것들은 따로 뺌 
        
        # print(self.queue.qsize())

        return self.sum / self.queue.qsize()

        # 배운점 1) queue와 sum을 함수에서 계속 이용하기 위해서 __init__에서  self.queue와 self.sum을 사용함.
        # 배운점 2)nextVal에는 queue와, sum이라는 자료구조가 있다! queue를 사용하면서 sum에 동시에 사용할 수 있다! 


        
        
        


def queueExample():
    q = queue.Queue()
    # q.put(1)
    # q.put(2)
    # print(q.qsize())
    # print(q.get())
    # print(q.qsize())
    # print(q.get())
    
    
def main():
    queueExample()
    

    nums = [2,8,19,37,4,5]
    ma = MovingAvg(3)
    print(ma)
    results = []
    for num in nums:
        avg = ma.nextVal(num)
        results.append(avg)
    print(results) # [2.0, 5.0, 9.666666666666666, 21.333333333333332, 20.0, 15.333333333333334]
if __name__ == "__main__":
    main()