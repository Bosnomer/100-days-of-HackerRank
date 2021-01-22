# Capitalize!

def solve(s):
    s = list(s)
    s[0] = s[0].upper()
    for i in range(len(s)):
        if s[i] == " ":
            s[i+1] = s[i+1].upper()
    str1 = ""    
    s = str1.join(s)
    return(s)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
