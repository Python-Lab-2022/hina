import datetime
today=datetime.date.today()
startyear=today.year
endyear=int(input("Enter end year: "))
print("Leap years are:\n")
for year in range(startyear,endyear):
    if (year%400==0) and (year%100==0):
        print(year)
    elif (year%4==0) and (year%100!=0):
        print(year)
