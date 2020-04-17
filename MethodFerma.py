#!/usr/bin/python
# -*- coding: UTF-8 -*-

import gmpy2
import time
from datetime import datetime
from gmpy2 import mpq, mpz, sqrt, ceil, isqrt
from sys import argv

def square(x,n):
    k = 1
    while k > 0:
        y = gmpy2.sqrt((mpq(x) + mpq(k))**2 - mpq(n))
        if gmpy2.is_integer(y):
           return y, k
        else:
           k+=1

def MethodFerma(n):
    x = isqrt(n) + 1
    y, k = square(x,n)
    a = mpz(x) + mpz(k) + mpz(y)
    b = mpz(x) + mpz(k) - mpz(y)
    return a, b, k

if __name__ == '__main__':
  if len (argv) == 2:
       if int(argv[1]) % 2 != 0:
           start = datetime.now()
           a, b, k = MethodFerma(mpz(argv[1]))
           end = datetime.now() - start
           print("\n[ Factor: a + b = ", mpz(a), "] \n")
           print("[ Factor: a - b = ", mpz(b), "] \n")
           print("[ Count: k = ", mpz(k), "] \n")
           print("Time: ", end)
       else:
           print("[Error] Your number is even")

  else:
       print("[Error] No input number")
