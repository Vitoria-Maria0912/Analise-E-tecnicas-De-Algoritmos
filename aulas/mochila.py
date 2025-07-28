def mochila(X, itens_pesos, itens_valores, valor, maiorValor, pesoMax, i):
    if(i == len(itens_pesos)):
        maiorValor = max(valor, maiorValor)
        print(f"Valor { maiorValor } R$ - Peso: { 16 - pesoMax } - Itens: { X }")
    else:
        if(itens_pesos[i] <= pesoMax): 

            mochila(X+[i], itens_pesos, itens_valores, (valor + itens_valores[i]), maiorValor, (pesoMax - itens_pesos[i]), i+1)

        mochila(X, itens_pesos, itens_valores, valor, maiorValor, pesoMax, i+1)


itens_pesos = {1:15, 2:5, 3:10, 4:5}
itens_valores = {1:20, 2:30, 3:50, 4:10}
mochila([], itens_pesos, itens_valores, 0, 0, 16, 1)

# X é a mochila