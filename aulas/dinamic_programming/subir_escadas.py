import sys

def subir_escadas(array):
    n = len(array)
    if(n == 0): resposta = [0]
    elif(n == 1): resposta = array[0]
    else:
        resposta[0] = array[0]
        resposta[1] = max(array[0], array[1])
        for i in range(2, n): 
            resposta.append(array[i] + array[i - 2])
    return resposta

input = list(map(int, sys.stdin.readline().strip()))

print(subir_escadas(input))