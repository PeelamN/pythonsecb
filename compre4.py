a={'a':'abc', 1:1234,'b':'bced',2:2345}
out={a[k]:k for k in a if type(k)==str
     }
print(out)