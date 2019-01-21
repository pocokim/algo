#     def nextVal(self, num):
#         self.queue.put(num)
#         if self.queue.qsize() <= 3:
#             self.sum +=num
#         elif self.queue.qsize() >3:
#             print(self.queue.get())
#             self.sum -= self.queue.get()
#         print(self.sum)
#         # print(self.queue.qsize())
        
#         return self.sum/self.queue.qsize()

# 실수했던 점 
# self.sum에 num이 추가되는건 모든 경우에 다 적용되는 개념이다. 
# 본능적으로 짜는것이 아니라 머릿속에서 순서에 맞게 작성하여야한다.
# 프로그래밍적 본능에 맞게 코드를 작성해야한다.


    def nextVal(self, num):
        self.queue.put(num)
        self.sum +=num
        if self.queue.qsize() > self.size:
            # print(self.queue.get())
            self.sum -= self.queue.get()
        # print(self.sum)
        # print(self.queue.qsize())
        
        return self.sum/self.queue.qsize()