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
    # verifica se o sistema tem solução
    if(common.check_sistema_solucao(matrizA, matrizB, matrizX)):
        # nova_matrizA e nova_matrizB são as matrizes A e B modificadas pela eliminação de Gauss
        nova_matrizA, nova_matrizB = matriz_triangular_sup(matrizA, matrizB)
        
        # calcula a solução do sistema
        matriz_solucao = common.result_sistema(nova_matrizA, nova_matrizB, matrizX)
        return matriz_solucao
    else:
        return None
    
def main():
    input = "G:\Meu Drive\\facul\\analise numerica\Relatorio 1\input_gauss.txt"
    output = "G:\Meu Drive\\facul\\analise numerica\Relatorio 1\output_gauss.txt"
    
    
    entrada = common.abrir_entrada(input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n')
        if len(entrada) == 4:
            x0 = common.expr_val(entrada[0])
            x1 = common.expr_val(entrada[1])
            precisao = common.expr_val(entrada[2])
            expressao = common.expr_val(entrada[3])
        else:
            return
    
    if expressao is None or x0 is None or x1 is None or precisao is None:
        return
    else:
        arquivo_saida = open(output, 'w')
        common.escrever_arquivo(arquivo_saida, f"k{'':<10}xk{'':<9}fxk{'':<9}xk+1{'':<9}fxk+1")
        common.escrever_arquivo(arquivo_saida, f"\n")
        raiz = secante(expressao, x0, x1, precisao, arquivo_saida)
        common.escrever_arquivo(arquivo_saida, "\nx(k+1) = ((fxk*(xk-1)) - ((fxk-1) *xk))/(fxk - (fxk-1))\n")
        if raiz is not None:
            result = expressao.subs(x, raiz)
            if result == 0:
                common.escrever_arquivo(arquivo_saida, f'\nA raiz da funcao eh: {raiz}')
            else:
                common.escrever_arquivo(arquivo_saida, f'\nA raiz (aproximada) da funcao eh: {raiz}')
        else:
            common.escrever_arquivo(arquivo_saida, '\nNão foi possível encontrar uma raiz')
        arquivo_saida.close()
        return
        
        

if __name__ == "__main__":
    main()
    