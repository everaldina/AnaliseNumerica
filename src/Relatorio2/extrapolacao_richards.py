import sympy as sp
import common
import os
from integracao_trapezio import trapezio_multiplo

x = sp.symbols('x')

# retorna a extrapolação de richarda para uma expressao, usando duas aproximações de integrais por trapezio com n1 e n2 segmentos
# segue a formula: I = I2 + ((I2 - I1)/((h1/h2)^2 - 1))
def extrapolacao_richards(expressao, limite_inf, limite_sup, n1, n2):
    # calcula as aproximações para de integrais para n1 e n2, usando a regra dos trapezios multiplos
    i1 = trapezio_multiplo(expressao, limite_inf, limite_sup, n1)
    i2 = trapezio_multiplo(expressao, limite_inf, limite_sup, n2)
    
    # calcula largura de cada segmento cada uma das integrais
    h1 = (limite_sup - limite_inf)/n1
    h2 = (limite_sup - limite_inf)/n2
    
    return i1, i2, h1, h2, i2 + ((i2 - i1)/((h1/h2)**2 - 1))

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
    
    metodo = "extrapolacao_richards"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n') # separando as linhas
        
        expressao = common.expr_val(entrada[0])
        limite_inf = sp.sympify(entrada[1]).evalf()
        limite_sup = sp.sympify(entrada[2]).evalf()
        n1 = int(entrada[3])
        n2 = int(entrada[4])
        
        

    # caminho do arquivo de saida
    arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
    arquivo_saida = open(arquivo_saida, 'w')
    
    i1, i2, h1, h2, integral = extrapolacao_richards(expressao, limite_inf, limite_sup, n1, n2)
    
    common.escrever_arquivo(arquivo_saida, f"I({h1}) = {i1}\n")
    common.escrever_arquivo(arquivo_saida, f"I({h2}) = {i2}\n")
    common.escrever_arquivo(arquivo_saida, f"Extrapolacao de Richards: {integral}\n")
    
    arquivo_saida.close()
    return


if __name__ == "__main__":
    main()
    
    