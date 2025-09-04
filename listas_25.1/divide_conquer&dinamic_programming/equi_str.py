import sys

def equi_str(str):
    if ((len(str) % 2) == 1): resposta = str
    else: 
        meio = len(str) // 2
        esquerda, direita = (equi_str(str[:meio])), (equi_str(str[meio:]))

        if(esquerda <= direita): resposta = esquerda + direita
        else: resposta = direita + esquerda 

    return resposta

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

print("YES" if (equi_str(a) == equi_str(b)) else "NO")

entradas = [["casa", "casa"], ["casa", "saca"], ["lapis", "pisla"], ["lapis", "lapis"], ["bbcb", "bcbb"], ["bbaa", "baba"]]
respostas = [          "YES",            "YES",               "NO",              "YES",            "YES",            "NO"]

for i, entrada, esperado in zip(range(len(entradas)), entradas, respostas):
    a, b = entrada
    resultado = "YES" if (equi_str(a) == equi_str(b)) else "NO"
    print(f"Erro {i}: esperado={esperado}, obtido={resultado}")
    assert resultado == esperado, f"Erro {i}: esperado={esperado}, obtido={resultado}"
print("✔️  Passou em todos os testes!")