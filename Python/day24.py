# Introduction to Sets

def average(array):
    array = set(array)
    n=len(array)
    s = list(array) 
    add = sum(array)
    return(add/n)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
