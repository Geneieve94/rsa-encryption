#!/usr/bin/python2
import random

def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e&1) == 1:
            # e&1 means that whether e is 1 or not
            result = (result * b) % m
        e >>= 1  # e = e/2
        b = (b*b) % m
    return result

def factorize(m):
    s=0
    d=0
    reminder=m%2
    while(reminder == 0):
        s=s+1
        m=m/2
        reminder = m%2
    d=m
    return s,d

def Miller_Rabin(n):
    s, d = factorize(n - 1)
    a = random.randint(1, n-1)
    # If a^q mod n= 1, n maybe is a prime number
    if fastExpMod(a, d, n) == 1:
        return "inconclusive"
    # If there exists j satisfy a ^ ((2 ^ j) * q) mod n == n-1, n maybe is a prime number
    for j in range(0, s):
        if fastExpMod(a, (2**j)*d, n) == n - 1:
            return "inconclusive"
    # a is not a prime number
    return "composite"

print Miller_Rabin(29)
