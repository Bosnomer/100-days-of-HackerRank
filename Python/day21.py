# String Formatting

def print_formatted(number):
    # your code goes here
    w = len(str(bin(number)).replace('0b',''))
    for i in range(1,number+1):
        #print(i)
        octal = oct(i)
        hexa = hex(i)
        binary = bin(i)

        #print(str(i).rjust(w, ' '), str(octal[2:]).rjust(w, ' '))
        print(str(i).rjust(w, ' '), str(octal[2:]).rjust(w, ' '), str(hexa[2:]).upper().rjust(w, ' '), str(binary[2:]).rjust(w, ' ' )) 

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
