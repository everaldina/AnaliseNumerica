import common
import sympy as sp
import os
from MMQ_discreta import aproximacao_polinomial as aproximacao_MMQd

x = sp.Symbol('x')

def aproximacao_polinomial(expressao, grau, limite_inf, limite_sup):
    mat_X = sp.zeros(grau + 1, grau + 1)
    vet_fx = sp.zeros(grau + 1, 1)
    
    # iniciando vetor a com simbolos
    vet_A = sp.Matrix([])
    for i in range(grau + 1):
        nome = 'x' + str(i)
        vet_A = vet_A.row_insert(i, sp.Matrix([sp.symbols(nome)]))
    
    
    for i in range (grau + 1):
        # preenchendo mat_X
        for j in range (grau + 1):
            if i > j:
                mat_X[i,j] = mat_X[j,i]
            else:
                # calculando integral de x^i*x^j de limite_inf a limite_sup
                mat_X[i,j] = sp.integrate(x**i * x**j, (x, limite_inf, limite_sup))
        
        # preenchendo vet_fx
        # calculando integral de f(x)*x^i de limite_inf a limite_sup
        vet_fx[i,0] = sp.integrate(expressao * (x**i), (x, limite_inf, limite_sup))
    
    # calculando matriz A
    vet_A = common.result_sistema(mat_X, vet_fx, vet_A)
    
    return vet_A

def main():
    ##### EXERCICIO 8.1 #####
    #input = "exercicio_8.1.txt"
    #output = "exercicio_8.1.txt"
    ##### EXERCICIO 8.5 #####
    #input = "exercicio_8.5.txt"
    #output = "exercicio_8.5.txt"
    ##### EXERCICIO 10.6 #####
    #input = "exercicio_10.6_2.txt"
    #output = "exercicio_10.6_2.txt"
    input = "exercicio_10.6_3.txt"
    output = "exercicio_10.6_3.txt"   
    
    metodo = "MMQ_continua"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n') # separando as linhas
        
    
        header = entrada[0].split(' ')
        expressao = ""
        # pegando expressao, grau, limite_inf e limite_sup
        grau = int(header[0])
        limite_inf = float(header[1])
        limite_sup = float(header[2])
        if len(header) >= 4:
            for i in range(3, len(header)):
                expressao += header[i]
        mmqd = False
        
        if(len(entrada) > 1):
            pontos = []
            # criando pontos
            for i in entrada[1:]:
                coordenadas = i.split(' ')
                pontos.append(sp.Point(float(coordenadas[0]), float(coordenadas[1])))
            mmqd = True
        

    # caminho do arquivo de saida
    arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
    arquivo_saida = open(arquivo_saida, 'w')
    
    # caso sejam dados pontos para aproximar isso é feito por uma aproximação polinomial discreta
    if mmqd:
        vet_a = aproximacao_MMQd(pontos)
        expressao = common.criar_polinomio(vet_a, x)
        
        
    # return a0, a1, cof_det, cof_cor, desvio_padrao
    coeficiente_a = aproximacao_polinomial(expressao, grau, limite_inf, limite_sup)
    cof_size = len(coeficiente_a)
    
    # imprimindo entrada
    common.escrever_arquivo(arquivo_saida, f"Aproximacao polinomial de grau {grau}\nf(x) = {expressao}\nintervalo: [{limite_inf}, {limite_sup}]\n\n")
    
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