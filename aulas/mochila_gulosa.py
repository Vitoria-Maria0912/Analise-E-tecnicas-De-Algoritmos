
def mochila_gulosa(pesos, valores, w):
    resposta = []
    peso = 0
    valor = 0 
    valor_real = 0
    i = 0
    while ((peso < w) and (i < len(valores))):
        if(peso + pesos[i] < w):
            peso += pesos[i]
            valor += valores[i]
            valor_real += valores[i]
            resposta.append(peso)
        else:
            aux = (w-peso)/pesos[i]
            valor += ((valores[i]/pesos[i]) * aux)
            peso = w
        i+=1

    return resposta, valor, valor_real

# Testes
itens = 3
weights = [50]
itens_pesos = [[10, 20, 30]]
itens_valores = [[60, 100, 120]]

for i, w, pesos, valores in zip(range(itens), weights, itens_pesos, itens_valores):
    resposta, valor, valor_real = mochila_gulosa(pesos, valores, w)
    print(f"Conjunto: { resposta } - Valor real: R$ { valor_real } - Valor máximo: R$ {valor:.2f}")