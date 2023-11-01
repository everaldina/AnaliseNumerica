import sympy as sp
import common
import os

x = sp.symbols('x')
 
# retorna o valor da integral de uma expressao usando a regra de simpson 1/3
def simpson_multiplo(expressao, limite_inf, limite_sup, segmentos): 
    h = (limite_sup - limite_inf)/segmentos
    
    # cria uma lista com os xn de cada segmento
    lista_segmentos = []
    for i in range(segmentos+1):
        lista_segmentos.append(limite_inf + (i*h))
    
    # faz o somatorio dos xn pares
    soma_par = 0
    for i in range(2, len(lista_segmentos) - 1, 2):
        soma_par += expressao.subs(x, lista_segmentos[i]).evalf()
        
    # faz o somatorio dos xn impares
    soma_impar = 0
    for i in range(1, len(lista_segmentos) - 1, 2):
        soma_impar += expressao.subs(x, lista_segmentos[i]).evalf()
        
    
    return (h/3)*(expressao.subs(x, lista_segmentos[0]).evalf() + (4*soma_impar) + (2*soma_par) + expressao.subs(x, lista_segmentos[-1]).evalf())

# retorna o valor da integral de uma expressao usando regra de simpson 1/3 uma vez
# seguindo a formula (b - a)*(f(a) + (4*f((a+b)/2))+ f(b))/6
def simpson_simples(expressao, limite_inf, limite_sup):
    media = (limite_inf + limite_sup)/2
    
    fx0 = expressao.subs(x, limite_inf).evalf()
    fx1 = expressao.subs(x, media).evalf()
    fx2 = expressao.subs(x, limite_sup).evalf()
    
    return (limite_sup - limite_inf)*(fx0 + (4*fx1) + fx2)/6

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
    
    metodo = "simpson_1_3"
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
    
    integral_simples = simpson_simples(expressao, limite_inf, limite_sup)
    integral_multiplo = simpson_multiplo(expressao, limite_inf, limite_sup, divisoes)
    
    common.escrever_arquivo(arquivo_saida, "Integral simples: " + str(integral_simples) + "\n")
    common.escrever_arquivo(arquivo_saida, "Integral multipla: " + str(integral_multiplo))
    
    
    arquivo_saida.close()
    return


if __name__ == "__main__":
    main()