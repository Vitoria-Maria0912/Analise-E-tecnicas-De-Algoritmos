import sys
import itertools

t = int(sys.stdin.readline().strip())

if(t > 1 and t < 10**3):
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        nums = list(map(int, sys.stdin.readline().strip()))
