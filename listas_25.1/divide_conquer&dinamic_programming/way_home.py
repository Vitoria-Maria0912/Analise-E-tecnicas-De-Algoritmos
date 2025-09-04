import sys

def way_home(n, d, s):

    if(len(s) == n): 

        posicao_atual = 0
        passos = 0

        while posicao_atual < n - 1:
            salto_encontrado = False
            for p in range(d, 0, -1):
                posicao_parcial = posicao_atual + p
                if (posicao_parcial < n) and (s[posicao_parcial] == '1'):
                    posicao_atual += p
                    passos += 1
                    salto_encontrado = True
                    break
            
            if not salto_encontrado: 
                passos = -1
                break
    return passos

n, d = list(map(int, sys.stdin.readline().split()))
s = sys.stdin.readline().strip()

print(way_home(n, d, s))

testes = [
    [8, 4, '10010101'],
    [4, 2, '1001'],
    [8, 4, '11100101'],
    [12, 3, '101111100101'],
    [5, 4, '11011']
    ]

respostas = [
            2,
            -1,
            3,
            4,
            1 
            ]
for e, r in zip(testes, respostas):
    n, d, s = e
    res = way_home(n, d, s)
    assert r == res, f"Erro entrada={n, d, s} esperado={r} obtido={res}"
print("✔️  Passou em todos os testes!")