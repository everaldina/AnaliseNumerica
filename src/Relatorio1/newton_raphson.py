import sympy as sp
import common
import os

x = sp.symbols('x')

def newton_raphson(expressao, x0, precisao, arquivo_saida):
    
    k = 1
    
    xk, fxk, f_xk = sp.symbols("xk fxk f_xk")
    exp_rap = sp.simplify("xk - ((fxk)/(f_xk))")
    while True:
        xk_val = x0.evalf()
        
        # calculo de f(xk) e f'(xk)
        fxk_val = expressao.subs(x, xk_val).evalf()
        f_xk_val = sp.diff(expressao, x).subs(x, xk_val).evalf()
            
        
        # escreve no arquivo de saida
        common.escrever_arquivo(arquivo_saida, f'{k:<7}\t')         
        common.escrever_arquivo(arquivo_saida, f'{xk.subs(xk, xk_val).evalf():.5f}{"":<5}')           
        common.escrever_arquivo(arquivo_saida, f'{fxk.subs(fxk, fxk_val).evalf():.5f}{"":<5}')           
        common.escrever_arquivo(arquivo_saida, f'{f_xk.subs(f_xk, f_xk_val).evalf():.5f}{"":<5}\n')
          
        
        
        # caso f(xk) = 0, então xk é a raiz
        if fxk_val == 0:
            return xk_val
        
        
        # verifica se o erro é menor que a tolerância
        if abs(fxk_val.evalf()) < precisao:
            return xk_val
        
        # calcula o proximo ponto xk
        x0 = exp_rap.subs(xk, xk_val).subs(fxk, fxk_val).subs(f_xk, f_xk_val).evalf()
        k += 1
    
def main():
    ##### EXERCICIO 3.3 #####
    ### Para g(0.1)
    #input = "exercicio_3.3-0.1.txt"
    #output = "exercicio_3.3-0.1.txt"
    ### Para g(0.9)
    #input = "exercicio_3.3-0.9.txt"
    #output = "exercicio_3.3-0.9.txt"
    ##### EXERCICIO 3.6 #####
    #input = "exercicio_3.6.txt"
    #output = "exercicio_3.6.txt"
    ##### EXERCICIO 3.8 #####
    #input = "exercicio_3.8-A.txt"
    #output = "exercicio_3.8-A.txt"
    #input = "exercicio_3.8-B.txt"
    #output = "exercicio_3.8-B.txt"
    
    metodo = "newton-raphson"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n')
        if len(entrada) == 3:
            x0 = common.expr_val(entrada[0])
            precisao = common.expr_val(entrada[1])
            expressao = common.expr_val(entrada[2])
        else:
            return
    
    
    if expressao is None or x0 is None or precisao is None:
        return
    else:
        arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
        arquivo_saida = open(arquivo_saida, 'w')
        common.escrever_arquivo(arquivo_saida, f"k{'':<10}xk{'':<10}fxk{'':<9}f'xk")
        common.escrever_arquivo(arquivo_saida, f"\n")
        raiz = newton_raphson(expressao, x0, precisao, arquivo_saida)
        common.escrever_arquivo(arquivo_saida, "\nx(k+1) = xk - (fxk)/(f'xk)\n")
        if raiz is not None:
            result = expressao.subs(x, raiz)
            if result == 0:
                common.escrever_arquivo(arquivo_saida, f'\nA raiz da funcao eh: {raiz}')
            else:
                common.escrever_arquivo(arquivo_saida, f'\nA raiz (aproximada) da funcao eh: {raiz}')
        else:
            common.escrever_arquivo(arquivo_saida, '\nNão foi possível encontrar uma raiz')
        arquivo_saida.close()
        return
        
        

if __name__ == "__main__":
    main()