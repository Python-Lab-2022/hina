print("Output for a:\n")
list1= [11,21,102,-29]
for i in list1:
    if i>0:
        print(i)
print("Output for b:\n")
list2=[]
n=int(input("Enter the number of elements:"))
for i in range (0,n):
    list2.append(int(input()))
print(list2)
print("Squares are:")
for i in list2:
    print(i*i)
print("Output for c:\n")
string=("Geeks for Geeks")
vowels="AaEeIiOoUu"
final=[i for i in string if i in vowels]
print(len(final))
print(final)
print("Output for d:\n")
string2=['g','s','f','h']
for char in string2:
    print(char,'-',ord(char))
