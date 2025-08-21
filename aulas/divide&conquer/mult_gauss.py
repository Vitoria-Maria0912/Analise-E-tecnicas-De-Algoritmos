def mult_gauss(a, b):
    if a < 10 or b < 10: resposta = int(a) * int(b)
    else:
        n = max(len(str(a)), len(str(b)))
        meio = (n // 2)
        ae = a // (10 ** meio)
        ad = a % (10 ** meio)
        be = b // (10 ** meio)
        bd = b % (10 ** meio)
        x = mult_gauss(ae, be)
        y = mult_gauss(ad, bd)
        z = mult_gauss((ae+ad), (be+bd))
        resposta = (x * (10 ** (2 * meio))) + (z - x - y) * (10 ** meio) + y

    return resposta


entradas = [[1, 2], [10, 20], [1823, 2093]]
respostas = [2, 200, 3815539]

for i, entrada, esperado in zip(range(len(entradas)), entradas, respostas):
    a, b = entrada
    resultado = mult_gauss(a, b)
    assert resultado == esperado, f"Erro {i}: esperado={esperado}, obtido={resultado}"
print("✔️  Passou em todos os testes!")