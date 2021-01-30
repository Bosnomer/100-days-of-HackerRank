# Set .add()

if __name__ == "__main__":  
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    arr = set(arr)
    print(len(arr))
