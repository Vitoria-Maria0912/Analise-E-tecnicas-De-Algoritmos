import sys

def create_str(n, s):
    asw = []
    for i in range(n):
        aux = s.copy()
        aux[i] = 1 - aux[i]
        asw.append("".join(map(str, aux)))
    return asw

t = int(sys.stdin.readline()) # quantidade de testes

for _ in range(t):
    n = int(sys.stdin.readline()) # comprimento da String
    s = list(map(int, sys.stdin.readline().removesuffix("\n"))) # String
    
    if len(s) == n: 
        created_str = create_str(n, s)
        count = "".join(created_str).count('1')
        print(count)
