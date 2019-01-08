class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result 


a= FourCal()
print(type(a))
a.setdata(4,2)
# print(a.add())