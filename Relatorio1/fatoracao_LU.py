import sympy as sp
import common
import os

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

def fatoracao_LU(matrizA, matrizB, matrizX):
    # matrizL e matrizU são o resultado da decomposição LU da matriz A
    matrizL, matrizU = matriz_LU(matrizA)
    matriz_y = matrizX.copy()
    
    
    # calcula os valores de Y
    matriz_y = common.result_sistema(matrizL, matrizB, matriz_y)
    
    # calcula os valores de X
    matriz_solucao = common.result_sistema(matrizU, matriz_y, matrizX)
    return matrizL, matrizU, matriz_y, matriz_solucao


def main():
    ##### EXERCICIO 4.1 #####
    #input = "exercicio_4.1.txt"
    #output = "exercicio_4.1.txt"
    ##### EXERCICIO 4.3 #####
    #input = "exercicio_4.3.txt"
    #output = "exercicio_4.3.txt"
    ##### EXERCICIO 4.6 #####
    input = "exercicio_4.6.txt"
    output = "exercicio_4.6.txt"
    
    metodo = "fatoracao_LU"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n')
        #dimensao da matriz
        n = common.expr_val(entrada[0])
        #criando matrizB
        matrizB = sp.Matrix(entrada[1].split(' '))
        #criando matrizX
        matrizX = sp.Matrix([])
        for i in range(n):
            nome = 'x' + str(i)
            matrizX = matrizX.row_insert(i, sp.Matrix([sp.symbols(nome)]))
        #criando matrizA
        matrizA = sp.Matrix([])
        for i in range(2, len(entrada)):
            matrizA = matrizA.row_insert(i, sp.Matrix([entrada[i].split(' ')]))
        
    # verifica se o sistema tem solução e se a matriz A pode ser decomposta
    if not common.check_sistema_solucao(matrizA, matrizB, matrizX) or not check_requisito_decomposicao(matrizA):
        return
    else:
        arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
        arquivo_saida = open(arquivo_saida, 'w')
        
        matrizL, matrizU, matriz_y, result = fatoracao_LU(matrizA, matrizB, matrizX)
        
        # escrevendo matrizes L, U e Y
        common.escrever_arquivo(arquivo_saida, common.print_matriz(matrizL, 'L', 'n'))
        common.escrever_arquivo(arquivo_saida, "\n")
        common.escrever_arquivo(arquivo_saida, common.print_matriz(matrizU, 'U', 'n'))
        common.escrever_arquivo(arquivo_saida, "\n")
        common.escrever_arquivo(arquivo_saida, common.print_matriz(matriz_y, 'Y', 's'))

        # escrevendo resultado
        common.escrever_arquivo(arquivo_saida, "\nResultado:\n")
        common.escrever_arquivo(arquivo_saida, common.print_matriz(result, 'X', 'n'))
        
        arquivo_saida.close()
        return
        
        

if __name__ == "__main__":
    main()
