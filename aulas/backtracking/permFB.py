def permFB(X, A, i):
    if(i == len(A)): print(X)
    else:
        for j in range(len(A)):
            if not (A[j] in X): permFB(X+[A[j]], A, i+1)

conjunto_int = [1,2,3]
permFB([], conjunto_int, 0) 