def equi_str(a, b):
    if a == b: resposta = True
    elif (len(a) != len(b) or len(a) % 2 != 0): resposta = False
    else: 
        meio = len(a) // 2
        a1, a2 = a[:meio], a[meio:]
        b1, b2 = b[:meio], b[meio:]
        resposta = (equi_str(a1, b1) and equi_str(a2, b2)) or (equi_str(a1, b2) and equi_str(a2, b1))
    return resposta

entradas = [["casa", "casa"], ["casa", "saca"], ["lapis", "pisla"], ["lapis", "lapis"], ["bbcb", "bcbb"], ["bbaa", "baba"]]
respostas = [           True,             True,              False,               True,             True,           False]

for i, entrada, esperado in zip(range(len(entradas)), entradas, respostas):
    a, b = entrada
    n = max(len(a), len(b))
    resultado = equi_str(a, b)
    assert resultado == esperado, f"Erro {i}: esperado={esperado}, obtido={resultado}"
print("✔️  Passou em todos os testes!")