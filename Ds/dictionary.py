#2
my_dictionary ={0: 10, 1: 20}
print(my_dictionary)
my_dictionary.update({3:30})
print(my_dictionary)

#3
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic2.update(dic3)

dic1.update(dic2)
print(dic1)

#4

my_dictionary={1:10,2:20,3:30}

for i in my_dictionary.items():
    print(i)

#5

x=int(input("enter number x:"))
y={}

for d in range(x+1):
    
    if d==0:
        continue
    z={d:d*d}
    y.update(z)

print(y)

#6

my_dictionary={1:1,2:2,3:3,4:4}

my_dictionary.remove(1)