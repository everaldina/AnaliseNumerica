import sympy as sp
import common
import os

def jacobi(arquivo_saida, matrizB, vetorG, precisao, vet_inical = None):
    # verifica se a matriz B como é convergente 
    if common.check_converge(matrizB):
        n = sp.shape(matrizB)[0]
        
        # se vet_inical for None, vet_inical = vetor nulo
        if vet_inical is None:
            vet_inical = sp.zeros(n, 1)

        k = 0 # contador de iterações
        
        common.escrever_arquivo(arquivo_saida, common.print_matriz(vet_inical, f"x{k}", 'n'))
        common.escrever_arquivo(arquivo_saida, "\n")
        # vet_0 recebe vet_inical
        vet_0 = vet_inical.copy()
        
        # vet_1 vai receber o resultado da iteração
        vet_1 = matrizB*vet_0 + vetorG
        
        # calcula erro absoluto e relativo
        eabs, erel = common.return_variacao(vet_1, vet_0)
        
        # enquanto erro absoluto ou relativo for maior que precisao continua iteração
        while(eabs > precisao or erel > precisao):
            vet_0 = vet_1.copy() # vet_0 recebe vet_1
            k+=1
            common.escrever_arquivo(arquivo_saida, common.print_matriz(vet_0, f"x{k}", 'n'))
            common.escrever_arquivo(arquivo_saida, f"\t eabsoluto: {eabs:.5f} | erelativo: {erel:.5f}\n")
            vet_1 = matrizB*vet_0 + vetorG # recalcula vet_1
            eabs, erel = common.return_variacao(vet_1, vet_0) # recalcula erro absoluto e relativo
        return vet_0
    else:
        return None


def main():
    ##### EXERCICIO 5.1 #####
    #input = "exercicio-5.1.txt"
    #output = "exercicio-5.1.txt"
    ##### EXERCICIO 5.2 #####
    input = "exercicio-5.2.txt"
    output = "exercicio-5.2.txt"

    
    metodo = "jacobi"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n')
        x0_definido = entrada[0].split(' ')[0] == 'x0'
        
        # caso as entradas sejam x0 forem esfecificadas
        if x0_definido:
            n = common.expr_val(entrada[1]) # quantidade de expressoes
            x0 = sp.Matrix(entrada[0].split(' ')[1:])
            precisao = common.expr_val(entrada[2])
            b = sp.Matrix(entrada[3].split(' '))
        else:
            n = common.expr_val(entrada[0]) #quantidade de expressoes
            precisao = common.expr_val(entrada[1])
            b = sp.Matrix(entrada[2].split(' '))
            x0 = None

        #criando matrizX
        matrizX = sp.Matrix([])
        for i in range(n):
            nome = 'x' + str(i)
            matrizX = matrizX.row_insert(i, sp.Matrix([sp.symbols(nome)]))
        #criando matrizA
        matrizA = sp.Matrix([])
        for i in range(4, len(entrada)):
            if x0_definido:
                matrizA = matrizA.row_insert(i-4, sp.Matrix([entrada[i].split(' ')[0:]]))
            else:
                matrizA = matrizA.row_insert(i-4, sp.Matrix([entrada[i-1].split(' ')[0:]]))
        if not x0_definido:
            matrizA = matrizA.row_insert(n-1, sp.Matrix([entrada[len(entrada)-1].split(' ')[0:]]))
    #print(matrizA, b, matrizX)
    # verifica se o sistema tem solução
    if not common.check_sistema_solucao(matrizA, b, matrizX):
        return
    else:
        arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
        arquivo_saida = open(arquivo_saida, 'w')
        # escrevendo matrizes de entrada
        
        
        matB = common.return_matrizB(matrizA, n)
        vetG = common.return_vetorG(matrizA, b, n)
        
        # matriz na forma de jacobi
        common.escrever_arquivo(arquivo_saida, "Matriz B:\n")
        common.escrever_arquivo(arquivo_saida, common.print_matriz(matB, 'B', 'n'))
        common.escrever_arquivo(arquivo_saida, "\n")
        common.escrever_arquivo(arquivo_saida, "Vetor G:\n")
        common.escrever_arquivo(arquivo_saida, common.print_matriz(vetG, 'G', 'n'))    
        
        
        common.escrever_arquivo(arquivo_saida, "\n\nIteracoes:\n")
        result = jacobi(arquivo_saida, matB, vetG, precisao, x0)
        
        common.escrever_arquivo(arquivo_saida, f"\nAproximacao com {precisao} de precisa: ")
        common.escrever_arquivo(arquivo_saida, common.print_matriz(result, 'x', 'n'))
        
        
        
        arquivo_saida.close()
        return
        
        

if __name__ == "__main__":
    main()

    
    
