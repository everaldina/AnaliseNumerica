import sympy as sp
import common
import os

x = sp.Symbol('x')

def derivada_progressiva(expressao, ponto, H): 
    f_x1, f_x, h = sp.symbols("f_x1 f_x h")
    
    # formula da derivada progressiva
    derivada = sp.simplify("(f_x1 - f_x)/h")
    
    # substitui os valores na formula da derivada
    return derivada.subs(f_x1, expressao.subs(x, ponto + H).evalf()).subs(f_x, expressao.subs(x, ponto).evalf()).subs(h, H).evalf()


def derivada_retardada(expressao, ponto, H): 
    f_x1, f_x, h = sp.symbols("f_x1 f_x h")
    
    # formula da derivada retardada
    derivada = sp.simplify("(f_x - f_x1)/h")
    
    # substitui os valores na formula da derivada
    return derivada.subs(f_x1, expressao.subs(x, ponto - H).evalf()).subs(f_x, expressao.subs(x, ponto).evalf()).subs(h, H).evalf()

def derivada_central(expressao, ponto, H): 
    f_x1, fpx1, h = sp.symbols("f_x1 fpx1 h")
    
    # formula da derivada central
    derivada = sp.simplify("(fpx1 - f_x1)/(2*h)")
    
    # substitui os valores na formula da derivada
    return derivada.subs(f_x1, expressao.subs(x, ponto - H).evalf()).subs(fpx1, expressao.subs(x, ponto + H).evalf()).subs(h, H).evalf()

def derivada_segunda_ordem(expressao, ponto, h):
    # usando a formula de derivada progressiva e retardada para calcular a segunda ordem
    return (derivada_progressiva(expressao, ponto, h) - derivada_retardada(expressao, ponto, h))/ h 

def main():
    ##### EXEMPLO 8.1.2 #####
    input = "exemplo_8.1.2_i.txt"
    output = "exemplo_8.1.2_i.txt"
    input = "exemplo_8.1.2_ii.txt"
    output = "exemplo_8.1.2_ii.txt"
    input = "exemplo_8.1.2_iii.txt"
    output = "exemplo_8.1.2_iii.txt"
    
    metodo = "derivadas"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n') # separando as linhas
        
        expressao = common.expr_val(entrada[0])
        x = sp.sympify(entrada[1]).evalf()
        h = sp.sympify(entrada[2]).evalf()
        
    # caminho do arquivo de saida
    arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
    arquivo_saida = open(arquivo_saida, 'w')
    
    d_progressiva = derivada_progressiva(expressao, x, h)
    d_retardada = derivada_retardada(expressao, x, h)
    d_central = derivada_central(expressao, x, h)
    d_segunda = derivada_segunda_ordem(expressao, x, h)
    
    common.escrever_arquivo(arquivo_saida, f"Derivada progressiva: {d_progressiva}\n")
    common.escrever_arquivo(arquivo_saida, f"Derivada retardada: {d_retardada}\n")
    common.escrever_arquivo(arquivo_saida, f"Derivada central: {d_central}\n")
    common.escrever_arquivo(arquivo_saida, f"Derivada de segunda ordem: {d_segunda}\n")
    
    arquivo_saida.close()
    return


if __name__ == "__main__":
    main()