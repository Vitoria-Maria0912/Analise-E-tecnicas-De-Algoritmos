def busca_binaria(array, x):
    if(len(array) == 0): resposta = -1
    else: 
        meio = len(array) // 2
        if(x == array[meio]): resposta = x
        elif(x < array[meio]): resposta = busca_binaria(array[:meio], x)
        else: resposta = busca_binaria(array[meio:], x)
    return resposta

entradas = [[1, 2], [10, 20]]
valores = [1, 0]
respostas = [1, -1]

for i, entrada, esperado in zip(range(len(entradas)), entradas, respostas):
    resultado = busca_binaria(entrada, valores[i])
    assert resultado == esperado, f"Erro {i}: esperado={esperado}, obtido={resultado}"
print("✔️  Passou em todos os testes!")