import re
data='''
vnjshgdhnn,ghs673heeap78he 23huj k hjwieqqiq378999230'
'''
pattern='[Aa][Pp] ?[0-3][1-9] ?[A-Za-z] ?[0-9]{4}'
data=re.findall(pattern,data)
print(data)