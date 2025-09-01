import sys

def fib(n):
    if(n == 0): resposta = []
    resposta = [0, 1]
    for i in range(2, n): resposta.append(resposta[i - 1] + resposta[i - 2])
    return resposta

input = int(sys.stdin.readline()) 

print(fib(input))