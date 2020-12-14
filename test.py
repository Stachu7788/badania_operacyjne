class A:
    def __init__(self,num):
        self.a = num
        
    def get(self):
        return self.a
    
class B(A):
    def __init__(self,num,str_):
        super().__init__(num)
        self.b=str_
    
    def get(self):
        return self.a,self.b
        
        
ob_a = A(5)
print(ob_a.get())
print(type(ob_a))
ob_b = B(2,'string')
print(ob_b.get())
print(type(ob_b))
print(type(super(type(ob_b))))