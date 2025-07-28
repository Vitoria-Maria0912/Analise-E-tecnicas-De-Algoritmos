def promissor(elemento, somaParcial, restanteMax, soma):
    return (somaParcial + restanteMax >= soma) and (somaParcial == soma or somaParcial + elemento <= soma)

def sum_sub(A, B, d, sum_parcial, resto, i, sum): 
    if(sum_parcial == d): print(f"Array: { A } = { sum_parcial }")
    else:
        # print(A)
        if(i < (len(B)) and (promissor(B[i], sum_parcial, resto, sum))):
            sum_sub(A+[B[i]], B, d, sum_parcial+B[i], resto-B[i], i+1, sum)
            sum_sub(A, B, d, sum_parcial, resto, i+1, sum)


conjunto = [1, 2, 5, 6, 8]
total_sum = sum(conjunto) # 22
d = 9
sum_sub([], conjunto, d, 0, total_sum, 0, sum=total_sum)