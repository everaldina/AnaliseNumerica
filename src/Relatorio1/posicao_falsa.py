import sympy as sp
import common 
import os 

x = sp.symbols('x')

def posicao_falsa(expressao, a, b, precisao, arquivo_saida):
    if common.check_solution(expressao, a, b):
        k = 1
        
        exp_falsa = sp.simplify("((ax * fbx) - (bx * fax)) / (fbx - fax)")
        ax, bx, fax, fbx = sp.symbols('ax bx fax fbx')
        while True:
            fa = expressao.subs(x, a)
            fb = expressao.subs(x, b)
            
            # calcula o ponto x
            xk = exp_falsa.subs(ax, a).subs(bx, b).subs(fax, fa).subs(fbx, fb).evalf()
            
            # calcula f(xk)
            fxk = expressao.subs(x, xk)
            
            # calcula o erro
            aprox = abs(b - a)
            aprox_relativa = aprox/abs(b)
            
            
            # escreve no arquivo de saida
            common.escrever_arquivo(arquivo_saida, f'{k:<7}\t')         
            common.escrever_arquivo(arquivo_saida, f'{a:.5f}{"":<5}')           
            common.escrever_arquivo(arquivo_saida, f'{b:.5f}{"":<5}')           
            common.escrever_arquivo(arquivo_saida, f'{fa:.5f}{"":<5}')           
            common.escrever_arquivo(arquivo_saida, f'{fb:.5f}{"":<5}')           
            common.escrever_arquivo(arquivo_saida, f'{aprox:.5f}{"":<5}')           
            common.escrever_arquivo(arquivo_saida, f'{aprox_relativa:.5f}{"":<5}')           
            common.escrever_arquivo(arquivo_saida, f'{sp.N(xk, 5)}{"":<5}')          
            common.escrever_arquivo(arquivo_saida, f'{sp.N(fxk, 5)}\n')    
            
            
            # caso f(xk) = 0, então xk é a raiz
            if fxk == 0:
                return xk
            
            # verifica se o erro é menor que a tolerância
            if aprox_relativa < precisao or k > 1000:
                return xk
            

            k += 1
            if fa * fxk < 0: # verifica se f(a) * f(xk) < 0
                b = xk
            elif fb * fxk < 0: # verifica se f(xk) * f(b) < 0
                a = xk
            else: # caso não seja possível encontrar uma raiz
                return None
    else:
        return None
    
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
    
    metodo = "posicao_falsa"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n')
        if len(entrada) == 4:
            a = common.expr_val(entrada[0])
            b = common.expr_val(entrada[1])
            precisao = common.expr_val(entrada[2])
            expressao = common.expr_val(entrada[3])
        else:
            return
    
    if expressao is None or a is None or b is None or precisao is None:
        return
    else:
        arquivo_saida = os.path.join(common.diretorio_atual, 'outputs', metodo, output)
        arquivo_saida = open(arquivo_saida, 'w')
        
        common.escrever_arquivo(arquivo_saida, f'k{"":<10}a{"":<11}b{"":<11}f(a){"":<8}f(b){"":<9}e{"":<9}e/|bk|{"":<7}xk{"":<7}f(xk)\n')
        raiz = posicao_falsa(expressao, a, b, precisao, arquivo_saida)
        common.escrever_arquivo(arquivo_saida, '\nxk = (ak * fbk - bk * fak) / (fbk - fak)\t\te = |(bk - ak)|\n')
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