#2
from array import*
arr=array("i",[1 ,2 ,3 ,4 ,5])
len(arr)
for i in arr[:]:
    print(i)

#3
from array import*
str=array("i",[1,2,1,1,4,5])
count=0
for i in str:
    if i==1:
        count=count+1
print("No. of occurances of 1 is", count)

#4
from array import*
Arr=array("i",[2,1,4,5,7,1])
se=1
c=0
for i in Arr:
    if Arr==se:
        Arr.remove(i)
        break
    c = c + 1
for i in Arr:
    print(i)
print(Arr)



