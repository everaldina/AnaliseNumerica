import sympy as sp
import common

def matriz_LU(matrizA):
    n = sp.shape(matrizA)[0]
    
    # cria matrizes identidade com U e L com dimensão n
    matL = sp.eye(n)
    matU = sp.eye(n)
    
    for i in range(n):
        matU[0, i] = matrizA[0, i]
        if i != 0:
            matL[i, 0] = matrizA[i, 0]/matU[0, 0]

    print(common.print_matriz(matL, 'L', 'n'))
    print(common.print_matriz(matU, 'U', 'n'))
    for i in range(n):
        for j in range(n):
            if i <= j and i != 0:
                print("\nu(", i, j, ") = ", end = '')
                matU[i,j] = matrizA[i,j]
                print(matU[i,j], end = ' - ')
                for k in range(0, i):
                    print(matL[i,k]*matU[k,j], end="")
                    matU[i,j] -= matL[i,k]*matU[k,j]
                print()
                
            if i > j and j != 0:
                print("\nl(", i, j, ") = ", end = '')
                matL[i,j] = matrizA[i,j]
                print(matL[i,j], end = ' - ')
                for k in range(0, j):
                    print(matL[i,k]*matU[k,j], end="")
                    matL[i,j] -= matL[i,k]*matU[k,j]
                matL[i,j] /= matU[j,j]
                
    return matL, matU

