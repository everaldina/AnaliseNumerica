import sympy as sp
import src.utils as utils 
import os 

x = sp.symbols('x')

def posicao_falsa(expressao, a, b, precisao, i_max=100) -> dict | None:
    if utils.check_solution(expressao, a, b):
        result = {}
        k = 1
        desvio_relativo = float('inf')
        x_old = a if abs(expressao.subs(x, a)) < abs(expressao.subs(x, b)) else b
        fa = float(expressao.subs(x, a).evalf())
        fb = float(expressao.subs(x, b).evalf())
        while k <= i_max and desvio_relativo > precisao:
            denom = fb - fa
            xk = b + ((fb*(a-b)) / denom)
            fxk = float((expressao.subs(x, xk)).evalf())

            desvio_relativo = abs(xk - x_old)/xk
            
            result[k] = {'a': a, 'b': b, 'f(a)': fa, 'f(b)': fb, 'xk': xk, 'f(xk)': fxk, 'desvio_relativo': desvio_relativo}
            x_old = xk
            
            if fxk == 0:
                return result
            
            if fa * fxk < 0:
                b = xk
                fb = fxk
            elif fxk * fb < 0:
                a = xk
                fa = fxk
            else:
                None
            k += 1
        return result
    else:
        return None
    
def run_posicao_falsa(input_file: str = None, output_path: str = None, entrada_dict: dict = None): 
    if entrada_dict is not None:
        a = utils.expr_val(entrada_dict.get('a'))
        b = utils.expr_val(entrada_dict.get('b'))
        precisao = utils.expr_val(entrada_dict.get('precisao'))
        expressao = utils.expr_val(entrada_dict.get('expressao'))
        iteracoes = entrada_dict.get('iteracoes')
        if expressao is None or a is None or b is None or precisao is None:
            raise ValueError("Entrada inválida")
    else:
        entrada = utils.abrir_entrada('posicao_falsa', input_file)
        if entrada is None:
            raise FileNotFoundError("Arquivo de entrada não encontrado")
        
        entrada = entrada.split('\n')
        if len(entrada) == 4:
            a = utils.expr_val(entrada[0])
            b = utils.expr_val(entrada[1])
            precisao = utils.expr_val(entrada[2])
            expressao = utils.expr_val(entrada[3])
        else:
            raise ValueError("Entrada inválida")
        if expressao is None or a is None or b is None or precisao is None:
            raise ValueError("Entrada inválida")
    
    if output_path is not None:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as arquivo_saida:
            result = posicao_falsa(expressao, a, b, precisao)
            utils.escrever_arquivo(arquivo_saida, f'k{"":<10}a{"":<11}b{"":<11}f(a){"":<8}f(b){"":<9}e/|bk|{"":<7}xk{"":<7}f(xk)\n')
            if result is None:
                utils.escrever_arquivo(arquivo_saida, '\nNão foi possível encontrar uma raiz')
            for k, v in result.items():
                a = v['a']
                b = v['b']
                fa = v['f(a)']
                fb = v['f(b)']
                xk = v['xk']
                fxk = v['f(xk)']
                desvio_relativo = v['desvio_relativo']
            
                utils.escrever_arquivo(arquivo_saida, f'{k:<7}\t')         
                utils.escrever_arquivo(arquivo_saida, f'{a:.5f}{"":<5}')           
                utils.escrever_arquivo(arquivo_saida, f'{b:.5f}{"":<5}')           
                utils.escrever_arquivo(arquivo_saida, f'{fa:.5f}{"":<5}')           
                utils.escrever_arquivo(arquivo_saida, f'{fb:.5f}{"":<5}')                 
                utils.escrever_arquivo(arquivo_saida, f'{desvio_relativo:.5f}{"":<5}')           
                utils.escrever_arquivo(arquivo_saida, f'{sp.N(xk, 5)}{"":<5}')          
                utils.escrever_arquivo(arquivo_saida, f'{sp.N(fxk, 5)}\n')    
                utils.escrever_arquivo(arquivo_saida, '\nxk = (ak * fbk - bk * fak) / (fbk - fak)\t\te = |(bk - ak)|\n')
    else:
        return posicao_falsa(expressao, a, b, precisao, iteracoes)
        
        
def main(input_file: str = None, output_path: str = None):
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
    if input_file is None:
        input_file = "exercicio_3.1.txt"
    if output_path is None:
        output_path = os.path.join(utils.diretorio_atual, 'outputs', 'posicao_falsa', "exercicio_3.1.txt")
    run_posicao_falsa(input_file=input_file, output_path=output_path)
    
if __name__ == "__main__":
    main()