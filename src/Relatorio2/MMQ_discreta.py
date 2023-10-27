from .. import common
import sympy as sp

def aproximacao_polinomial(pontos):
    n = len(pontos)
    mat_UU = sp.zeros(n-1, n-1)
    vet_yU = sp.zeros(n-1, 1)
    vet_U = []
    vet_a = sp.zeros(n-1, 1)
    
    # preenchendo vetores x e y
    vet_y = sp.zeros(n, 1)
    vet_x = sp.zeros(n, 1)
    for i in range(n):
        vet_y[i, 0] = pontos[i].y
        vet_x[i, 0] = pontos[i].x
        
    # preenchendo matrizes U
    vet_U.append(sp.ones(n, 1))
    for i in range(1, n):
        vet_U.append(vet_U[i-1].copy())
        for j in range(n):
            vet_U[i][j, 0] *= vet_x[j, 0]
    

    for i in range(n-1):
        # preenchendo matrizUU
        for j in range(n-1):
            if (i > j):
                mat_UU[i, j] = mat_UU[j, i]
            else:
                mat_UU[i, j] = vet_U[i].dot(vet_U[j]) # calculando o produto interno
        # vetor yU
        vet_yU[i, 0] = vet_y.dot(vet_U[i])
        
    # resolvendo o sistema
    common.result_sistema(mat_UU, vet_yU, vet_a)
    
    return vet_a    

    
    
    
    