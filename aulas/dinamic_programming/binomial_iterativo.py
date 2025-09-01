import sys, numpy

def binomial_iterativo(n, k):
    matriz = numpy.zeros((k+1, n+1), dtype=int)
    for col in range(n+1):
        for lin in range(k+1):
            if(lin == 0 or col == lin): matriz[lin, col] = 1 
            elif(lin > 0 and col > lin): matriz[lin, col] = matriz[(lin-1), (col-1)] + matriz[lin, (col-1)]
    return matriz

n = int(sys.stdin.readline()) 
k = int(sys.stdin.readline()) 

print(binomial_iterativo(n, k))