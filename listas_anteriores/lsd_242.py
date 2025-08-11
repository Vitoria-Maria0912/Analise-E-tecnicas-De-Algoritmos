import sys
import itertools

def gen_binaries(n):
    binaries = list(set(itertools.permutations(['0', '1', '1'], len(n))))
    return [int("".join(num)) for num in binaries]

def verify_sequency(n):
    list_n = list(range(1, n+1))
    count = 0

    for e in list_n: 
        if(e in gen_binaries(str(n))): count += 1
    
    return count

n = int(sys.stdin.readline())
if(n > 0): print(verify_sequency(n))

# Testes
numbers = [0,    1, 10, 11, 30, 100, 1000]
answers = [None, 1,  2,  3,  3,   6,   11]

for i, num, asw in zip(range(1,4), numbers, answers):
    result = verify_sequency(num) if (num > 0) else None
    assert result == asw, f"Erro {i}, entry={num} obtido={result} esperado={asw}"
print("All tests passed!")