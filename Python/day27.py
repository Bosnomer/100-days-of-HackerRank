# Symmetric Difference

if __name__=="__main__":
    M = [] 
    N = []
    n = int(input()) 
    M = map(int,input().split())
    
    n = int(input()) 
    N = map(int,input().split())

    result = (set(M).symmetric_difference(set(N)))
    result = sorted(result)
    
    for i in result:
        print(i)
