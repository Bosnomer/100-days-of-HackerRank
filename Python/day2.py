# Python If-Else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())

    if (n>=1 and n<=100):
        if(n%2!=0):
            print("Weird")
        
        if((n%2==0) and (n in range(2,6))):
            print("Not Weird")
        
        if((n%2==0) and (n in range(6,21))):
            print("Weird")

        if((n%2==0) and (n>20)):
            print("Not Weird")
    
    else:
        print("Out of Constraint!")
