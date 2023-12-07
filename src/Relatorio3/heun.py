import common
import sympy as sp
import os

x = sp.Symbol('x')
y = sp.Symbol('y')

def heun(expressao, h, a, b, y0):
    resultados = []
    
    # adiciona o primeiro valor
    xi = a
    yi = y0
    resultados.append((xi, yi))
    
    
    # calcula os valores de x e y para cada iteração
    while xi < b:
        k = expressao.subs(x, xi).subs(y, yi).evalf()
        k1 = expressao.subs(x, xi + h).subs(y, yi + k*h).evalf()
        yi = yi + (k + k1)*(h/2)
        xi += h
        resultados.append((xi, yi))
    
    return resultados

def main():
    ##### EXERCICIO 12.3 #####
    #input = "exercicio_12.3.txt"
    #output = "exercicio_12.3.txt"
    ##### EXERCICIO 12.10 #####
    #input = "exercicio_12.10.txt"
    #output = "exercicio_12.10.txt"
    ##### EXERCICIO 12.16 #####
    #input = "exercicio_12.16_1.txt"
    #output = "exercicio_12.16_1.txt"
    #input = "exercicio_12.16_2.txt"
    #output = "exercicio_12.16_2.txt"
    
    metodo = "heun"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        print("Entrada nula")
        return
    else:
        entrada = entrada.split('\n') # separando as linhas
        
        if len(entrada) != 4:
            print("Entrada invalida")
            return
        expressao = common.expr_val(entrada[0]) # expressao
        amplitude = float(entrada[1]) # amplitude
        
        # limites inferior e superior
        limite_inf, limite_sup = entrada[2].split(' ')
        limite_inf = float(limite_inf)
        limite_sup = float(limite_sup)
        
        if limite_inf >= limite_sup:
            print("Entrada invalida")
            return
        
        valor_inicial = float(entrada[3]) # valor inicial
        

    # caminho do arquivo de saida
    arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
    arquivo_saida = open(arquivo_saida, 'w')
        
        
    # gera uma lista de tuplas (x, y)
    resultados = heun(expressao, amplitude, limite_inf, limite_sup, valor_inicial)
    
    # escreve os resultados no arquivo de saida
    common.escrever_arquivo(arquivo_saida, f"Resultado do metodo de Heun\n[ ")
    for i in range(len(resultados)):
        common.escrever_arquivo(arquivo_saida, f"{i}({resultados[i][0]:.5f}, {resultados[i][1]:.5f})")
        if i == len(resultados) - 1:
            common.escrever_arquivo(arquivo_saida, f" ]")
        else:
            common.escrever_arquivo(arquivo_saida, f", ")
        if i % 3 == 0 and i:
            common.escrever_arquivo(arquivo_saida, "\n  ")
    
    
    arquivo_saida.close()
    return


if __name__ == "__main__":
    main()