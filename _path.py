rows=int(input('enter a no.of rows'))
temp=rows//2
out=''
for i in range(rows):
    for j in range(rows):
        if i==j or i==rows-j-1:
            out+=''
        else:
            out+='*'
    out+='\n'

print(out)