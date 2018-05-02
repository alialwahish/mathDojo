class MathDojo(object):
    def __init__(self):
        self.result=0
    def add(self,num1,num2=0,num3=0):
        if type(num1) is list:
            num1=self.ifList(num1)
        if type(num2) is list:
            num2=self.ifList(num2)
        if type(num3) is list:
            num3=self.ifList(num3)
        self.result+=num1+num2+num3
        return self
    def subtract(self,num1,num2=0,num3=0):
        if type(num1) is list:
            num1=self.ifList(num1)
        if type(num2) is list:
            num2=self.ifList(num2)
        if type(num3) is list:
            num3=self.ifList(num3)
        self.result-=num1+num2+num3
        return self
        
    def ifList(self,li):
        total=0
        for tot in li:
            total+=tot
        return total

    

md=MathDojo()
# print md.add(2).add(2,5).subtract(3,2).result
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result