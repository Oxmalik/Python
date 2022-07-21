#!/bin/python3
#Muhammad Malik
#If/Else statements
#July 19, 2022

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    
    x = "Weird"
    y="Not Weird"
    
    if ((n%2)==1):
        print(x)
    elif (((n%2)==0)and (1<n<6)):
        print(y)
    elif (((n%2)==0)and (5<n<21)):
        print (x)
    elif (((n%2)==0)and (n>20)):
        print(y)
