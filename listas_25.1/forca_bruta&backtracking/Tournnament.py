import sys

def last_remain(k, j, n_int):
    j_force = n_int[j-1] 
    players = sorted(set(n_int), reverse=True)[:k]
    if ((k == 1) and (j_force not in players)): result = ("NO")    
    else: result = ("YES")
    return result

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, j, k = map(int, sys.stdin.readline().strip().split())
    n_int = list(map(int, sys.stdin.readline().strip().split()))
    
    if(len(n_int) == n): print(last_remain(k, j, n_int))

# Testes
players = [{'play': [5, 2, 3], 'n_int': [3, 2, 4, 4, 1]}, 
           {'play': [5, 4, 1], 'n_int': [5, 3, 4, 5, 2]}, 
           {'play': [6, 1, 1], 'n_int': [1, 2, 3, 4, 5, 6]}
          ]
answers = ["YES", "YES", "NO"]

for i, game, asw in zip((range(3)), players, answers):
    n, j, k = game['play']
    result = last_remain(k, j, game['n_int'])
    assert result == asw, f"Erro {i}: entry={game}, esperado={asw}, obtido={result}"
print("All tests passed!")


