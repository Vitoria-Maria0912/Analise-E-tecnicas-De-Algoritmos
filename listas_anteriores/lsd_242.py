import sys
import itertools

def gen_binaries(n):
    half = (len(n)//2) + 1
    binaries_poss = (['0'] * half) + (['1'] * (half+1))
    binaries = list(set(itertools.permutations(binaries_poss, len(n))))
    return [int("".join(num)) for num in binaries]

def verify_sequency(n):
    list_n = list(range(1, n+1))
    count = 0
    binaries_poss = gen_binaries(str(n))

    for e in list_n: 
        if(e in binaries_poss): count += 1
    
    return count

n = int(sys.stdin.readline())
if(n > 0): print(verify_sequency(n))

# Testes
numbers = [0,    1, 10, 11, 30, 100, 110, 111, 1000, 1010, 1111, 2000, 23536]
answers = [None, 1,  2,  3,  3,   4,   6,   7,    8,   10,   15,   16,    31]
for i, num, asw in zip(range(1,len(numbers)+1), numbers, answers):
    result = verify_sequency(num) if (num > 0) else None
    assert result == asw, f"Erro {i}, entry={num} obtido={result} esperado={asw}"
print("All tests passed!")