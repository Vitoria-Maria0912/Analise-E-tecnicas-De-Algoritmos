def count_split(esquerda, direita):
    count, i, j = 0, 0, 0
    resposta = []
    while i < len(esquerda) and j < len(direita):
        if(esquerda[i] <= direita[j]):
            resposta.append(esquerda[i])
            i += 1
        else: 
            resposta.append(direita[j])
            count += (len(esquerda) - i) 
            j += 1
    resposta.extend(esquerda[i:])
    resposta.extend(direita[j:])
    return count, resposta


def count_(array, resposta):
    
    if len(array) <= 1: resposta = [0, array]
    else:
        meio = len(array) // 2
        inv_esq, esquerda = count_(array[:meio], resposta)
        inv_dir, direita = count_(array[meio:], resposta)
        inv_merge, array_ordenado = count_split(esquerda, direita)
        resposta = [(inv_esq + inv_dir + inv_merge), array_ordenado]
    return resposta

entradas = [[8, 3, 2, 9, 7, 1, 5, 4]]
respostas = [17]

for i, ent, esperado in zip(range(len(entradas)), entradas, respostas):
    resultado = count_(ent, 0)[0]
    assert resultado == esperado, f"Erro {i}: esperado={esperado}, obtido={resultado}"
print("✔️  Passou em todos os testes!")
