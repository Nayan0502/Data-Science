#1
x=input("enter your first name")
y=input("enter your last name")

print(y+" "+x)

#2
x=input("enter comma separated numbers:")
list = x.split(",")
tuple= tuple(list)
print('list:',list)
print('tuple:',tuple)

#3
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[3])







#6
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

#7
my_list=[1, 5, 8, 3]
print(3 in my_list)
print(-1 in my_list)


#10
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

#17
import time

start = time.time()

for i in range(3):
    print("hello")

end = time.time()
print("the execution time is:" ,end-start)

#18
import os
print('Get current working directory : ', os.getcwd())

#20
x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter second number"))

a1=min(x,y,z)
a3=max(x,y,z)
a2=(x+y+z)-a1-a3

print(a1,a2,a3)

#24
import sys
a=sys.getsizeof(12)
print(a)





















































































































































































































































































































































