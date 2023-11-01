import sympy as sp
import common
import os

x = sp.symbols('x')
 
# retorna o valor da integral de uma expressao usando trapézios múltiplos
def trapezio_multiplo(expressao, limite_inf, limite_sup, segmentos): 
    h = (limite_sup - limite_inf)/segmentos
    
    # cria uma lista com os xn de cada segmento
    lista_segmentos = []
    for i in range(segmentos+1):
        lista_segmentos.append(limite_inf + (i*h))
    
    # faz o somatorio com os valores de cada segmento para f(x)
    soma = 0
    for i in lista_segmentos[1:-1]:
        soma += expressao.subs(x, i).evalf()
    
    return (h/2)*(expressao.subs(x, lista_segmentos[0]).evalf() + (2*soma) + expressao.subs(x, lista_segmentos[-1]).evalf())

# retorna o valor da integral de uma expressao usando apenas um trapezio
# segue a formula (b - a)*(f(a) + f(b))/2
def trapezio_simples(expressao, limite_inf, limite_sup):
    return (limite_sup - limite_inf)*(expressao.subs(x, limite_inf) + expressao.subs(x, limite_sup))/2
    
    
def main():
    ##### EXERCICIO 11.1 #####
    #input = "exercicio_11.1_i.txt"
    #output = "exercicio_11.1_i.txt"
    #input = "exercicio_11.1_ii.txt"
    #output = "exercicio_11.1_ii.txt"
    ##### EXERCICIO 11.6 #####
    #input = "exercicio_11.6_i.txt"
    #output = "exercicio_11.6_i.txt"
    #input = "exercicio_11.6_ii.txt"
    #output = "exercicio_11.6_ii.txt"
    ##### EXERCICIO 11.11 #####
    #input = "exercicio_11.11.txt"
    #output = "exercicio_11.11.txt" 
    
    metodo = "integracao_trapezio"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n') # separando as linhas
        
        expressao = common.expr_val(entrada[0])
        limite_inf = sp.sympify(entrada[1]).evalf()
        limite_sup = sp.sympify(entrada[2]).evalf()
        divisoes = int(entrada[3])
        
        

    # caminho do arquivo de saida
    arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
    arquivo_saida = open(arquivo_saida, 'w')
    
    integral_simples = trapezio_simples(expressao, limite_inf, limite_sup)
    integral_multiplo = trapezio_multiplo(expressao, limite_inf, limite_sup, divisoes)
    
    common.escrever_arquivo(arquivo_saida, "Integral simples: " + str(integral_simples) + "\n")
    common.escrever_arquivo(arquivo_saida, "Integral multipla: " + str(integral_multiplo))
    
    
    arquivo_saida.close()
    return


if __name__ == "__main__":
    main()
    