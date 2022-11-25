list1=[]
list2 =[]
a=[]
n=int(input("Enter the number of colors in list1:"))
for i in range (0,n):
      list1.append(str(input()))
n1=int(input("Enter the number of colors in list2:"))
for i in range (0,n1):
      list2.append(str(input()))
for i in list1:
       if i not in list2:
           a.append(i)
print(a)
