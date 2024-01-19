out=[]
for k in range(100,501):
    b=k
    d=0
    while b>0:
        c=b%10
        b=b//10
        b=d*10+c
    if  d==k:
          out+=[k] 
print(out) 
