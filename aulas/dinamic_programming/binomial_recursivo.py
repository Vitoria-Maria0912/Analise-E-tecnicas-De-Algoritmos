import sys

def binomial_recursivo(n, k):
    if(k == 0 or (k == n)): resposta = 1
    elif(k > 0 and k < n):
        resposta = binomial_recursivo((n-1), (k-1)) + binomial_recursivo((n-1), k)
    else: resposta = 0
    return resposta

n = int(sys.stdin.readline()) 
k = int(sys.stdin.readline()) 

print(binomial_recursivo(n, k))