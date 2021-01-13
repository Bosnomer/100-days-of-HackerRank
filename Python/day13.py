# sWAP cASE

def swap_case(s):
    new = []
    for i in range(len(s)):
        if (s[i].isupper()):
            new.append(s[i].lower())
        else:
            new.append(s[i].upper())
    str1=""
    for ele in new:  
        str1 += ele 
    return (str1)
    return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
