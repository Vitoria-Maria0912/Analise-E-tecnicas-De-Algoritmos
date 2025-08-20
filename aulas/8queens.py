def absolute(matrix, a, b): 
    if matrix[b] == 0: return a
    else: return abs(a - matrix[b])

def is_valid(matrix, col, element):
    diferent_lines = True if sum(map(lambda a: a != element, matrix)) == 4 else False
    #print(f"{ matrix } - q: { element } - resposta: {list(map(lambda a: a != element, matrix))}")
    diferent_diagonal1 = True if (col == 0) or (col > 0 and (absolute(matrix, element, (col-1)) != 1)) else False
    #print("que?",(abs(element - matrix[col-1]) ))
    #print(matrix)
    diferent_diagonal2 = True if (col == len(matrix)-1) or (col < len(matrix)-1 and (absolute(matrix, col, (col+1))) != 1) else False
    asw = diferent_lines and diferent_diagonal1 and diferent_diagonal2
    #print("q",diferent_diagonal1)
    return (element == 0) or asw


def queens(matrix, col): 
    if(col == len(matrix)): print(matrix)
    else:
        for element in range(len(matrix)):
            if (is_valid(matrix, col, element)): 
                matrix[col] = element
                # print(matrix)
                queens(matrix, col+1)

n = 4
matrix = [0] * n

queens(matrix, 0)