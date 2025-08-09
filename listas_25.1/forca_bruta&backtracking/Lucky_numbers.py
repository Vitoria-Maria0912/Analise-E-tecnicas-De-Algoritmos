import sys
import itertools

def is_odd(a): return (a % 2) == 1

def is_lucky(n): 
    sum_n = sum(map(lambda num: num not in ['4', '7'], n))
    return sum_n == 0 and (n.count('4') == n.count('7'))

def join(n, i, asw): 
    if(i == len(n)-1): asw += str(n[i])
    else: asw = join(n, i+1, asw+str(n[i]))
    return asw

def gen_lucky_n(len_n): 
    if is_odd(len_n): len_n += 1
    return (([4] * (len_n//2)) + ([7] * (len_n//2)))

def permut_lucky(n, lucky_n): 
    return [join(num, 0, "") for num in list(itertools.permutations(lucky_n, len(lucky_n))) if int(join(num, 0, "")) > int(n)]

def find_next(n): 
    lucky_n = gen_lucky_n(len(n))
    join_lucky = (join(lucky_n, 0, ""))
    
    if(is_lucky(list(n))): result = n
    elif(int(join_lucky) >= int(n)): result = join_lucky
    else: 
        candidates = permut_lucky(n, lucky_n)
        if candidates: result = min(candidates)
        else: result = join(gen_lucky_n(len(n)+2), 0, "")
        
    return result
    
    
n = sys.stdin.readline().strip()
print(find_next(n))
        

# Teste
testes = ["1", "47", "100", "4500", "4587", "99999999", "74477744"]
answers = ["47", "47", "4477", "4747", "4747", "4444477777", "74477744"]

i = 0
for entry, esperado in zip(testes, answers):
    result = find_next(entry)
    assert result == esperado, f"Erro {i}: entry={entry}, esperado={esperado}, obtido={result}"
    i+=1
