# Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    new_list = set(arr) 
    new_list.remove(max(new_list)) 
    print(max(new_list))
