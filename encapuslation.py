class cname:
    a=10
    b=20
    def __init__(self,c,d):  
       self._c = c
       self._d = d
    def display(self):
         print(self.c,self.d)
class sub(cname):
    pass
obj=sub(5,6)            
