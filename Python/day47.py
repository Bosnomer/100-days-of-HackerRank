# Detect Floating Point Number

n = int(input())
for i in range(n):
    try:
        check=input()
        check=float(check)
        if (check==0):
            print("False")
        else:
            print("True")
    except:
        print("False")
