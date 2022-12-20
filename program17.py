d1={}
d2={}
d3={}
n=int(input("Enter the number of elements in d1:"))
for i in range(n):
    name=input("Enter the name:")
    age=input("Enter age:")
    d1[name]=age
print("Dictionary1:",d1)
n1=int(input("Enter the number of elements in d2:"))
for i in range(n1):
    name1=input("Enter the name:")
    age1=input("Enter age:")
    d2[name1]=age1
print("Dictionary2:",d2)
d3=d1.copy()
d3.update(d2)
print("Merge two dictionaries:\n")
print(d3)
