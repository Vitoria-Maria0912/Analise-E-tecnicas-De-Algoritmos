import sys

def dice_comb(n):
    lista = [0] * (n+1)
    lista[0] = 1

    for s in range(1, (n + 1)):
        for d in range(1, 7): 
            if(s >= d): lista[s] = (lista[s-d] + lista[s]) % (10**9 + 7)

    return lista[-1]

n = int(sys.stdin.readline())

print(dice_comb(n))

testes = [3, 4, 5]
respostas = [4, 8, 16]
for n, r in zip(testes, respostas):
    res = dice_comb(n)
    assert r == res, f"Erro entrada={n} esperado={r} obtido={res}"