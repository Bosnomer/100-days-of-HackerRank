# Exceptions

if __name__ == "__main__":
    no = int(input())
    for i in range(no):
        x, y = input().split() 
        try:
            print (int(x)//int(y))
        except ZeroDivisionError as e:
            print ("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print ("Error Code:", e)
