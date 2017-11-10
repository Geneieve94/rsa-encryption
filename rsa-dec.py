#!/usr/bin/python2
import sys
import random
def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e&1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b*b) % m
    return result

def decryption(C, d, N,n):
    pad=fastExpMod(int(C),d,n)
    print pad
    unpad=bin(pad)[2:][(N/2 - 2):]
    print unpad

    # RSA M = C^d mod n
    return int(unpad,2)

if   __name__ == "__main__":
    f_input = open(sys.argv[(sys.argv.index("-i") + 1)], 'r')
    input = f_input.read().strip()
    f_key = open(sys.argv[(sys.argv.index("-k") + 1)], 'r')
    key = f_key.read().split()
    out = str(decryption(input, int(key[2]), int(key[0]),int(key[1])))
    f_output = open(sys.argv[(sys.argv.index("-o") + 1)], 'w')
    output = f_output.write(out)
    f_input.close()
    f_key.close()
    f_output.close()