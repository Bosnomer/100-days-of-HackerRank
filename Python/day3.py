# Arithmetic Operators

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    if ((a,b>=1) and (a,b<=10**10)):
        print(a+b)
        print(a-b)
        print(a*b)
    else:
        print("Out of Constraint!")
