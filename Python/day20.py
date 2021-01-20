# Text Wrap

import textwrap

def wrap(string, length):
    lst = (list(string[0+i:length+i] for i in range(0, len(string), length)))
    for i in lst:
        print (i)
    return ""

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
