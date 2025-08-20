from collections import Counter

def calculaTroco(total, conjunto):
    conjunto.sort(reverse=True)
    soma = 0
    qtt_moedas = 0
    conjunto_resposta = []
    i = 0
    while ((soma < total) and (i < len(conjunto))):
        maximo = max(conjunto[i:])
        if((soma + maximo) <= total):
            soma += maximo
            conjunto_resposta.append(maximo)
            qtt_moedas += 1
            i=0
        else: i+=1
    return qtt_moedas, dict(Counter(conjunto_resposta)), soma

# Testes
totais = [289, 8]
conjuntos = [[100, 25, 10, 5, 1], [6, 4, 1]]

for i, total, conjunto in zip(range(len(conjuntos)), totais, conjuntos):
    qtt_moedas, conjunto_resposta, soma = calculaTroco(total, conjunto)
    print(f"Resposta: { qtt_moedas }, { conjunto_resposta } e { soma }")