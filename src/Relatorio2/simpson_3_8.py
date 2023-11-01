import sympy as sp
import common
import os

x = sp.symbols('x')
 
# retorna o valor da integral de uma expressao usando a regra de simpson 1/3
# segue a formula: ((b-a)/8)*(f(x0) + (3*f(x1)) + (3*f(x2))+ f(x3))
def simpson_3_8(expressao, limite_inf, limite_sup): 
    h = (limite_sup - limite_inf)/3
    
    # cria uma lista com os xn de cada segmento
    lista_segmentos = []
    for i in range(4):
        lista_segmentos.append(limite_inf + (i*h))
    
    # calcula o valor de cada f(xn)
    f = []
    for i in lista_segmentos:
        f.append(expressao.subs(x, i).evalf())
        
    
    return ((limite_sup - limite_inf)/8)*(f[0] + (3*f[1]) + (3*f[2]) + f[3])

def main():
    ##### EXERCICIO 11.1 #####
    #input = "exercicio_11.1.txt"
    #output = "exercicio_11.1.txt"
    ##### EXERCICIO 11.6 #####
    #input = "exercicio_11.6_i.txt"
    #output = "exercicio_11.6_i.txt"
    #input = "exercicio_11.6_ii.txt"
    #output = "exercicio_11.6_ii.txt"
    ##### EXERCICIO 11.11 #####
    #input = "exercicio_11.11.txt"
    #output = "exercicio_11.11.txt" 
    
    metodo = "simpson_3_8"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n') # separando as linhas
        
        expressao = common.expr_val(entrada[0])
        limite_inf = sp.sympify(entrada[1]).evalf()
        limite_sup = sp.sympify(entrada[2]).evalf()
        
        

    # caminho do arquivo de saida
    arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
    arquivo_saida = open(arquivo_saida, 'w')
    
    integral = simpson_3_8(expressao, limite_inf, limite_sup)
    
    common.escrever_arquivo(arquivo_saida, "Integral por Simpson 3/8: " + str(integral))
    
    arquivo_saida.close()
    return


if __name__ == "__main__":
    main()