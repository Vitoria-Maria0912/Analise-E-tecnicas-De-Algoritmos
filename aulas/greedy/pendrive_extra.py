def pendrive(n, c, t, out, parcial, i, soma):
    if(i >= n): 
        if(soma == c): out += [parcial]
    else:
        soma = sum(parcial)
        if(soma < c): 
            out = pendrive(n, c, t, out, parcial+[t[i]], i+1, soma)
        out = pendrive(n, c, t, out, parcial, i+1, soma)
    return out

# Testes
ns = [8]
cs = [90]
ts = [[10, 15, 20, 20, 30, 35, 40, 50]]
esperado = [4]

for i, n, c, t, out in zip(range(8), ns, cs, ts, esperado):
    t = sorted(t, reverse=True)
    resposta = pendrive(n, c, t, [], [], 0, 0)
    resposta_final = len(max(resposta, key=len))
    assert resposta_final == out, f"Erro {i}: esperado:{out}, tamanho:{resposta_final}, conjunto:{resposta}"
print("✔️  Passou em todos os testes!")