# String Validators

if __name__ == '__main__':
    s = input()
    check=[False, False, False, False, False]
    for i in range(len(s)):
        if(str(s[i]).isalnum()):
            check[0]=True
        if(str(s[i]).isalpha()):
            check[1]=True
        if(str(s[i]).isdigit()):
            check[2]=True
        if(str(s[i]).islower()):
            check[3]=True
        if(str(s[i]).isupper()):
            check[4]=True
    
    for i in check:
        print(i)
