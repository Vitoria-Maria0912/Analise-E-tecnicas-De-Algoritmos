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
    n = int(sys.stdin.readline().strip()) # comprimento da String
    s = sys.stdin.readline().strip() # String
    if len(s) == n: 
        created_str = create_str(n, list(map(int, s)))
        count = "".join(created_str).count('1')
        print(count)
