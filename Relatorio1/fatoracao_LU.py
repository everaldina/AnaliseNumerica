import sympy as sp
import common

# verifica Teorema 4.1 - Teorema LU
def check_requisito_decomposicao(matrizA):
    n = sp.shape(matrizA)[0]
    matAux = matrizA.copy()
    
    # veerifica se determinante menor princiais de A são diferente de 0
    for i in range(n-1, 0, -1):
        matAux.row_del(i)
        matAux.col_del(i)
        if matAux.det() == 0:
            return False    
    return True

def matriz_LU(matrizA):
    n = sp.shape(matrizA)[0]
    
    # cria matrizes identidade com U e L com dimensão n
    matL = sp.eye(n)
    matU = sp.eye(n)
    
    # atribui os valores da primeira linha de U e primeira coluna de L
    # u0j = a0j
    # li0 = ai0/a00
    for i in range(n):
        matU[0, i] = matrizA[0, i]
        if i != 0:
            matL[i, 0] = matrizA[i, 0]/matrizA[0, 0]

    # atribui os valores de U e L
    # uij = aij - somatorio de 1 a k de lik*ukj, i <= j
    # lij = (aij - somatorio de 1 a k de lik*ukj)/ujj, i > j
    for i in range(n):
        for j in range(n):
            if i <= j and i != 0:
                matU[i,j] = matrizA[i,j]
                for k in range(0, i):
                    matU[i,j] -= matL[i,k]*matU[k,j]
                
            if i > j and j != 0:
                matL[i,j] = matrizA[i,j]
                for k in range(0, j):
                    matL[i,j] -= matL[i,k]*matU[k,j]
                matL[i,j] /= matU[j,j]
                
    return matL, matU

#mt = sp.Matrix([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]])
#rL, rU = matriz_LU(mt)
#print(common.print_matriz(rL, 'L', 'n'))
#print(common.print_matriz(rU, 'U', 'n'))
#mt2 = sp.Matrix([[5, 2, 1], [3, 1, 4], [1, 1, 3]])
#rL, rU = matriz_LU(mt2)
#print(common.print_matriz(rL, 'L', 'n'))
#print(common.print_matriz(rU, 'U', 'n'))
