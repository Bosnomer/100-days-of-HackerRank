# Write a function

def is_leap(year):
    if year in range(1900,10**5+1):
        leap = False
        if (year%4==0):
            leap = True
            if (year%100==0 and year%400!=0):
                leap = False
        return leap
    
    else:
        print("Out of Constraint!")
        
year = int(input())
print(is_leap(year))
