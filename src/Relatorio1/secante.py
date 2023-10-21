import sympy as sp
import common
import os

x = sp.symbols('x')

def secante(expressao, x0, x1, precisao, arquivo_saida):
    if x0 == x1: # caso x0 == x1, não é possivel calcular a secante
        return None
    else:
        k = 1
        xk, fxk, xk_1, fxk_1 = sp.symbols("xk fxk xk_1 fxk_1")
        exp_sec = sp.simplify("((fxk*xk_1) - (fxk_1 *xk))/(fxk - fxk_1)")
        x0_val = x0
        x1_val = x1
        
        # escreve a primeira linha com os argumentos da funcao
        common.escrever_arquivo(arquivo_saida, f'{k:<7}\t')         
        common.escrever_arquivo(arquivo_saida, f'{x0_val:.5f}{"":<5}')           
        common.escrever_arquivo(arquivo_saida, f'{expressao.subs(x, x0_val).evalf():.5f}{"":<5}')           
        common.escrever_arquivo(arquivo_saida, f'{x1_val:.5f}{"":<5}')           
        common.escrever_arquivo(arquivo_saida, f'{expressao.subs(x, x1_val).evalf():.5f}{"":<5}\n')
        
        k+=1
        while True:
            # calculo de f(xk) e f'(xk)
            fxk_val = expressao.subs(x, x1_val).evalf()
            fxk_1_val = expressao.subs(x, x0_val).evalf()
            
            # escreve no arquivo de saida
            common.escrever_arquivo(arquivo_saida, f'{k:<7}\t')         
            common.escrever_arquivo(arquivo_saida, f'{x1_val:.5f}{"":<5}')           
            common.escrever_arquivo(arquivo_saida, f'{fxk_val:.5f}{"":<5}')
            
            # calcula o proximo ponto xk
            xkpp_val = sp.simplify(exp_sec.subs(xk, x1_val).subs(fxk, fxk_val).subs(xk_1, x0_val).subs(fxk_1, fxk_1_val)).evalf()           
            f_xkpp_val = expressao.subs(x, xkpp_val).evalf()
            
            common.escrever_arquivo(arquivo_saida, f'{xkpp_val:.5f}{"":<5}')           
            common.escrever_arquivo(arquivo_saida, f'{f_xkpp_val:.5f}{"":<5}\n')
            
            
            
            # caso f(xk) = 0, então xk é a raiz
            if fxk_val == 0:
                return x1_val
            
            
            # verifica se o erro é menor que a tolerância
            if abs(fxk_val.evalf()) < precisao:
                return x1_val
            
            x0_val = x1_val
            x1_val = xkpp_val
            
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
    
    metodo = "secante"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n')
        if len(entrada) == 4:
            x0 = common.expr_val(entrada[0])
            x1 = common.expr_val(entrada[1])
            precisao = common.expr_val(entrada[2])
            expressao = common.expr_val(entrada[3])
        else:
            return
    
    if expressao is None or x0 is None or x1 is None or precisao is None:
        return
    else:
        arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
        arquivo_saida = open(arquivo_saida, 'w')
        common.escrever_arquivo(arquivo_saida, f"k{'':<10}xk{'':<9}fxk{'':<9}xk+1{'':<9}fxk+1")
        common.escrever_arquivo(arquivo_saida, f"\n")
        raiz = secante(expressao, x0, x1, precisao, arquivo_saida)
        common.escrever_arquivo(arquivo_saida, "\nx(k+1) = ((fxk*(xk-1)) - ((fxk-1) *xk))/(fxk - (fxk-1))\n")
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