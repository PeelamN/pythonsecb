import csv
#filr=open('sample.csv','a')
with open ('sample.csv','w',newline='') as file:
    data=[
        [1,'chanadan'],
        [2,'nandan'],
        [3,'bandan'],

          ]
    record=csv.writer(file)
    record.writerow([4,'gajanan',45])
    record.writerows(data)