def func(a,b,c=0,**kwargs):
    print(a,b,c,kwargs)
func(*[1,2],**{ 'c':1,'d':2})#a=1,b=2   