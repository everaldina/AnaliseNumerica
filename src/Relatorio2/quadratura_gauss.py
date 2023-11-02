import sympy as sp
import common
import os
from sympy.integrals.quadrature import gauss_legendre

# Símbolo para a variável de integração
x = sp.symbols('x')

# Função para calcular a quadratura de Gauss
def quadratura_gauss(expressao, limite_inf, limite_sup, pontos):
    # pontos e pesos para quantidade de pontos
    xn, wn = gauss_legendre(pontos, 5)

    # transformação de variavel
    # achando novos valores de x e dx
    xd = ( (limite_sup + limite_inf) + (limite_sup - limite_inf) * x)/ 2
    dxd = (limite_sup - limite_inf) / 2
    # substituindo na expressão
    expressao = expressao.subs(x, xd)
    expressao = expressao * dxd 

    # calculando a integral
    integral = 0
    for i in range(len(xn)):
        integral += expressao.subs(x, xn[i]) * wn[i]


    return integral

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
    
    metodo = "quadratura_gauss"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n') # separando as linhas
        
        expressao = common.expr_val(entrada[0])
        limite_inf = sp.sympify(entrada[1]).evalf()
        limite_sup = sp.sympify(entrada[2]).evalf()
        pontos = int(entrada[3]) 
        
        

    # caminho do arquivo de saida
    arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
    arquivo_saida = open(arquivo_saida, 'w')
    
    integral = quadratura_gauss(expressao, limite_inf, limite_sup, pontos)
    
    common.escrever_arquivo(arquivo_saida, f"Integral por quadratura de Gauss ({pontos} pontos): {integral}\n")
    
    arquivo_saida.close()
    return


if __name__ == "__main__":
    main()