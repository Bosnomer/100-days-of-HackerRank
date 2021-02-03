# Set .union() Operation

if __name__ == "__main__":
    m = int(input())
    M = map(int,input().split())
    n = int(input())
    N = map(int,input().split())

    result = set(M).union(set(N))
    print(len(result))
