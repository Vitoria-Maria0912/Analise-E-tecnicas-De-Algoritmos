import sys

def mult(x): return x // 2 # a*2

def add(x): return (x - 1) // 10 # (10*a)+1

def valid(a, b): return (a >= 1 and b >= 1 and b <= 10**9 and a < b)

def rec(a, b, seq):
    if (b <= a) or ((b % 2 != 0) and (b % 10 != 1)): seq += f'{ b } '
    else:
        seq += f'{ b } '
        if ((b % 2) == 0): b = mult(b)
        elif ((b % 10) == 1): b = add(b)
        seq = rec(a, b, seq)
    return seq 

a, b = map(int, sys.stdin.readline().split())

if (not valid(a, b)): print("NO")
else: 
    seq = list(reversed(rec(a, b, "").split()))
    if int(seq[0]) != a : print("NO")
    else: 
        k = len(seq)
        print("YES")
        print(k)
        print(" ".join(seq))