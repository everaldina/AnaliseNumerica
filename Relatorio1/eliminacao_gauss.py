import sympy as sp
import common

def matriz_triangular_sup(matrizA, matrizB):
    n = sp.shape(matrizA)[0]
    
    matA_tri = matrizA
    matB_tri = matrizB
    
    count_eliminacao = 1
    while(count_eliminacao < n):
        aux = count_eliminacao - 1
        for i in range(count_eliminacao, n):
            mij = matA_tri[i,aux]/matA_tri[aux, aux]
            matB_tri[i, 0] -= matB_tri[aux, 0]*(matA_tri[i, aux]/matA_tri[aux, aux])
            for j in range(n):
                matA_tri[i,j] -= matA_tri[aux, j]*mij
        count_eliminacao += 1
    return matA_tri, matB_tri


def eliminacao_de_gauss(matrizA, matrizB, matrizX):
    # nova_matrizA e nova_matrizB são as matrizes A e B modificadas pela eliminação de Gauss
    nova_matrizA, nova_matrizB = matriz_triangular_sup(matrizA, matrizB)
    
    # calcula a solução do sistema
    matriz_solucao = common.result_sistema(nova_matrizA, nova_matrizB, matrizX)
    return matriz_solucao
    
def main():
    input = "G:\Meu Drive\\facul\\analise numerica\AnaliseNumerica\Relatorio1\input_gauss.txt"
    output = "G:\Meu Drive\\facul\\analise numerica\AnaliseNumerica\Relatorio1\output_gauss.txt"
    
    
    entrada = common.abrir_entrada(input)
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
            matrizA = matrizA.row_insert(i-2, sp.Matrix([entrada[i].split(' ')]))
        
    # verifica se o sistema tem solução
    if not common.check_sistema_solucao(matrizA, matrizB, matrizX):
        return
    else:
        arquivo_saida = open(output, 'w')
        # escrevendo matrizes de entrada
        common.escrever_arquivo(arquivo_saida, "Matriz A:\n")
        common.escrever_arquivo(arquivo_saida, common.print_matriz(matrizA, 'A', 'n'))
        common.escrever_arquivo(arquivo_saida, "\n")
        common.escrever_arquivo(arquivo_saida, "Matriz B:\n")
        common.escrever_arquivo(arquivo_saida, common.print_matriz(matrizB, 'B', 'n'))
        common.escrever_arquivo(arquivo_saida, "\n")
        common.escrever_arquivo(arquivo_saida, "Matriz X:\n")
        common.escrever_arquivo(arquivo_saida, common.print_matriz(matrizX, 'X', 's'))
        
        matrizA_, matrizB_ = matriz_triangular_sup(matrizA, matrizB)
        
        # escrevendo matrizes resultantes
        common.escrever_arquivo(arquivo_saida, "\nMatriz A modificada pela eliminacao de Gauss:\n")
        common.escrever_arquivo(arquivo_saida, common.print_matriz(matrizA_, 'A', 'n'))
        common.escrever_arquivo(arquivo_saida, "\n")
        common.escrever_arquivo(arquivo_saida, "Matriz B modificada pela eliminacao de Gauss:\n")
        common.escrever_arquivo(arquivo_saida, common.print_matriz(matrizB_, 'B', 'n'))
        
        result = eliminacao_de_gauss(matrizA, matrizB, matrizX)
        # escrevendo resultado
        common.escrever_arquivo(arquivo_saida, "\nResultado:\n")
        common.escrever_arquivo(arquivo_saida, common.print_matriz(result, 'X', 'n'))
        
        
        
        arquivo_saida.close()
        return
        
        

if __name__ == "__main__":
    main()
    