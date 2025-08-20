import sys
import itertools

def div(a, b): return (a // b)

def rest(a, b): return (a % b)

def is_even_and_mult(m, n, asw): 
    if(rest(asw, n) == 0 and (m < n)) : asw += 0
    else: 
        print(m, n, asw)
        div_m = div(m, 2)
        if(rest(m, 2) == 0): 
            if(rest(div_m, n) == 0): asw += div_m
            else: 
                div_m -= 1
                asw += div_m + (n - div_m)
                is_even_and_mult(m, n, asw)

        else: 
            if(rest(div_m, n) == 0):
                asw += div_m
                m -= div_m
            else: 
                div_m -= 1
                asw += div_m
                m -= div_m
            is_even_and_mult(m, n, asw)

        
    return int(asw)

def minimun_path(m, n):

    asw = -1
    asw = is_even_and_mult(m, n, 0)
    return asw

#m, n = map(int, sys.stdin.readline().split())

# Testes
inputs =  [[10, 5],[10, 2], [3, 5], [10, 5]]
answers = [      5,6,     -1,       5]

for i, entry, asw in zip(range(1, len(inputs)+1), inputs, answers):
    m, n = entry
    result = minimun_path(m, n)
    assert result == asw, f"Erro {i} entrada={entry} esperado={asw} obtido={result}" 