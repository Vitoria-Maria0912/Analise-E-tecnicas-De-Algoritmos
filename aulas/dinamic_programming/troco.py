import sys, numpy

def troco_(moedas, troco):
    
    moedas = [0] + moedas
    qtdd_moedas = len(moedas)

    if(qtdd_moedas == 0 or troco == 0): resposta = [0]
    else:
        matriz = numpy.zeros((qtdd_moedas, troco+1), dtype=int)
        for col in range(1, troco+1):
            for lin in range(qtdd_moedas):
                valor_moeda = moedas[lin]
                valor_troco = col - valor_moeda
                if(valor_moeda == 1): matriz[lin] = range(0, troco+1)
                elif(valor_moeda == col): matriz[lin][col] = 1
                elif(valor_moeda > col): matriz[lin][col] = matriz[lin-1][col]
                else: matriz[lin][col] = min((matriz[lin][valor_troco] + 1), (matriz[lin-1][col]))
        resposta = matriz

    return resposta

moedas = list(map(int, sys.stdin.readline().split()))
troco = int(sys.stdin.readline())

# moedas, troco = [[1, 4, 6], 8]
print(troco_(moedas, troco))