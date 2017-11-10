#!/usr/bin/python2
import sys
import random
import math
def fastExpMod(b, e, m):
    """
    e = e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n)

    b^e = b^(e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n))
        = b^(e0*(2^0)) * b^(e1*(2^1)) * b^(e2*(2^2)) * ... * b^(en*(2^n))

    b^e mod m = ((b^(e0*(2^0)) mod m) * (b^(e1*(2^1)) mod m) * (b^(e2*(2^2)) mod m) * ... * (b^(en*(2^n)) mod m) mod m
    """
    result = 1
    while e != 0:
        if (e&1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b*b) % m
    return result

#M=message, e=private key, N=bit size of each block, n=p*q
def encryption(M, e, N,n):
    lr=random.getrandbits(N/2 -2)
    strM=bin(int(M))[2:]
    while len(strM) < N/2:
        strM = "0"*(N/2 - len(strM)) + strM

    strR=bin(lr)[2:]
    while len(strR)!= N/2 - 2:
        lr=random.getrandbits(N/2-2)
        strR=bin(lr)[2:]

    padM=int(strR+strM,2)
    # RSA C = M^e mod n
    return fastExpMod(padM, e, n)

if   __name__ == "__main__":

    f_input=open(sys.argv[(sys.argv.index("-i")+1)],'r')
    input=f_input.read().strip()
    f_key=open(sys.argv[(sys.argv.index("-k")+1)],'r')
    key=f_key.read().split()
    out = encryption(input, int(key[2]), int(key[0]),int(key[1]))
    out=str(out)
    f_output=open(sys.argv[(sys.argv.index("-o")+1)],'w')
    output = f_output.write(out)
    f_output.close()
    f_input.close()
    f_key.close()




