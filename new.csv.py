import csv
#filr=open('sample.csv','a')
with open ('sample.csv','w',newline='') as csvfile:
    fieldnames=['id','name','age']
    record=csv.DictWriter(csvfile,fieldnames)
    record.writeheader()
    data=[
        {'id':1,'name':'Raj','age':18},
        {'id':2,'name':'Rama','age':16},
        {'id':3,'name':'naveen','age':20},
            ]
    record.writerows(data)

with open('new.csv','r',newline='') as file:
    records=csv.DictReader(file)
    for i in records:
        print(i)
        