import operator
employees = {}
n=int(input("enter the number of elements:"))
for i in range(3):
    name = input("Enter employee's name: ")
    salary = input("Enter employee's salary: ")
    employees[name] = salary
print("Dictionary",employees)
a=sorted(employees.items(), key=operator.itemgetter(1))
print('Ascending order is',a)
d=dict(sorted(employees.items(), key=operator.itemgetter(1),reverse=True))
print('Descending order is',d)
