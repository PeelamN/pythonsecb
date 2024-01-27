def factorial (self):
    out = 1
    if self.a>1:
        for val in range(1,self.a+1):
            out*=val 
        return out     