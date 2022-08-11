str="This is a String"

#1program to calculate length of string
print("The length of the String is:",len(str))

#2program to calculate no. of char in string and char frequency
count=0
for i in str:
    count=count+1
print("The length of the String is:",count)
dict={}
x=0

for x in range(len(str)):
    s1=str[x]
    freq=1
    # b= x+1
    for b in range(len(str)):
        if str[x]==str[b]:
            freq=freq+1
        b += 1
    dict1={str[x]:freq}
    dict.update(dict1)

print(dict)

#3
string1="restart"
str=string1[0]
for i in range(len(string1)):
    if i==0:
        continue
    if string1[i]!="r":
        str=str+string1[i]
    else:
        str+="$"
print(str)





#4
String1 ='abc'
String2 = "String"
ing="ing"
ly="ly"
if String1.endswith("ing"):
    str1=String1+ly
else:
    str1=String1+ing
print(String1)
if String2.endswith("ing"):
    str2=String2+ly
else:
    str2=String2+ing
print(str1)
print(str2)

#5
list=["This","is","a","List","of","Words"]
longest=0
for i in list:
    Str=i
    if len(Str)>longest:
        longest=len(Str)
print("Length of the longest word in the list is:",longest)

#6
STRING=input("Enter the string")
print(STRING.upper())
print(STRING.lower())

#11
rev="Reverse"
temp=""
for i in range(len(rev)):
    temp=rev[i]+temp
print(temp)

#12
Character="Character"
n=5
str=""
for i in range(len(Character)):
    if i<n:
        str=str+Character[i].upper()
    else:
        str+=Character[i]
print(str)