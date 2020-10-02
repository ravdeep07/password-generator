#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:23:20 2020

@author: ravdeep-singh
"""

import string
import random

upper = string.ascii_uppercase
lower = string.ascii_lowercase
special = string.punctuation
number = string.digits
everything = upper + lower + special + number

def pwd_gen():
    x = str(input("Would you like a weak(W), medium(M) or a strong(S) password? "))
    
    if x == 'W':
        a1 = random.sample(lower, 4)
        b1 = random.sample(number, 3)
        a1.extend(b1)
        random.shuffle(a1)
        print('You Password is --->\t',end='')
        print("".join(a1))

    if x == 'M':
        a1 = random(lower, 4)
        b1 = random(number, 3)
        c1 = random(upper, 3)
        a1.extend(b1+c1)
        random.shuffle(a1)
        print('You Password is --->\t',end='')
        print("".join(a1))
        
    if x == 'S':
        a1 = random.sample(everything, 14)
        random.shuffle(a1)
        print('You Password is --->\t',end='')
        print("".join(a1))


pwd_gen()
