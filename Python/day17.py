# Find a string

def count_substring(string, sub_string):
    count = 0
    lt = len(sub_string)
    for i in range(len(string)):
        if(sub_string == string[i:lt]):
            count += 1
        lt = lt + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
