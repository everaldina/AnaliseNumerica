import common
import sympy as sp
import os
import random

# defini seed para resultados serem congruentes
random.seed(1)

def aproximacao_polinomial(pontos, grau = None):
    n = len(pontos)
    
    # se o grau for definido, sao escolhidos numeros aleatorios na amostra
    if grau is not None:
        indices_aleatorios = random.sample(range(n), grau+2)
        indices_aleatorios.sort()
        pontos = [pontos[i] for i in indices_aleatorios]
    n = len(pontos)     
    
    
    mat_UU = sp.zeros(n-1, n-1)
    vet_yU = sp.zeros(n-1, 1)
    vet_U = []
    
    # iniciando vetor a com simbolos
    vet_a = sp.Matrix([])
    for i in range(n-1):
        nome = 'x' + str(i)
        vet_a = vet_a.row_insert(i, sp.Matrix([sp.symbols(nome)]))
    
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
    vet_a = common.result_sistema(mat_UU, vet_yU, vet_a)
    
    return vet_a    

    
    
def main():
    ##### EXERCICIO 8.1 #####
    #input = "exercicio_8.1.txt"
    #output = "exercicio_8.1.txt"
    ##### EXERCICIO 8.5 #####
    #input = "exercicio_8.5.txt"
    #output = "exercicio_8.5.txt"
    ##### EXERCICIO 10.6 #####
    #input = "exercicio_10.6.txt"
    # output = "exercicio_10.6_2.txt"
    #output = "exercicio_10.6_3.txt"
    
    
    metodo = "MMQ_discreta"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n') # separando as linhas
        
        pontos = []
        # criando pontos
        for i in entrada:
            coordenadas = i.split(' ')
            pontos.append(sp.Point(float(coordenadas[0]), float(coordenadas[1])))   
        

    # caminho do arquivo de saida
    arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
    arquivo_saida = open(arquivo_saida, 'w')
    
    # return a0, a1, cof_det, cof_cor, desvio_padrao
    coeficiente_a = aproximacao_polinomial(pontos, 2)
    cof_size = len(coeficiente_a)
    
    # imprimindo polinimo
    for i in range(cof_size):
        if i == cof_size-1:
            common.escrever_arquivo(arquivo_saida, f"{coeficiente_a[i, 0]}x^{i})\n\n")
        elif i == 0:
            common.escrever_arquivo(arquivo_saida, f"f(x) = {coeficiente_a[i, 0]} + (")
        else:
            common.escrever_arquivo(arquivo_saida, f"{coeficiente_a[i, 0]}x^{i}) + (")
    
    # imprimindo coeficientes
    for i in range(cof_size):
        common.escrever_arquivo(arquivo_saida, f"a{i} = {coeficiente_a[i, 0]}\n")
    
    
    arquivo_saida.close()
    return


if __name__ == "__main__":
    main()