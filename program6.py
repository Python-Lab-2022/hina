list1=[]
list2=[]
n=int(input("Enter the number of elements in first list:"))
for i in range(0,n):
    list1.append(int(input()))
print("First list is:",list1)
num=int(input("Enter the number of elements in elements in second list:"))
for i in range(0,num):
    list2.append(int(input()))
print("Second list is:",list2)
len1=len(list1)
len2=len(list2)
print("Output of a")
if len1==len2:
    print("Two list are same length")
else:
    print("Two list are not same")
print("Output of b")
sum1=0
sum2=0
for i in list1:
    sum1=sum1+i
print("Sum of first list:",sum1)
for j in list2:
    sum2=sum2+j
print("Sum of second list:",sum2)
if sum1==sum2:
    print("Sum of two list are same")
else:
    print("Sum of two list are not same")
print("Output of c")
for x in list1:
    for y in list2:
        if x==y:
            print(x,"is the common element in these two list")
