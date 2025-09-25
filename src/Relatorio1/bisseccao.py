import sympy as sp
import utils
import os

x = sp.symbols('x')

def bisseccao(expressao, a, b, precisao, i_max=100, arquivo_saida=None) -> float | None:
    if utils.check_solution(expressao, a, b):
        result = {}
        k = 1
        aprox_relativa = float('inf')
        x_old = 0
        while k <= i_max or aprox_relativa > precisao:
            fa = expressao.subs(x, a)
            fb = expressao.subs(x, b)
            xk = (a + b) / 2
            fxk = expressao.subs(x, xk)
            
            aprox_relativa = abs(xk - x_old)/xk
            x_old = xk
            
            result[k] = {'a': a, 'b': b, 'f(a)': fa, 'f(b)': fb, 'xk': xk, 'f(xk)': fxk, 'desvio_relativo': aprox_relativa}
                            
            if fxk == 0:
                return result
            if aprox_relativa < precisao:
                return result
            
            k += 1
            if fa * fxk < 0:
                b = xk
            elif fxk * fb < 0:
                a = xk
            else:
                return None
    else:
        return None

def run_bisseccao(input_file: str = None, output_path: str = None, entrada_dict: dict = None):
    if entrada_dict is not None:
        # Entrada via dict
        a = utils.expr_val(entrada_dict.get('a'))
        b = utils.expr_val(entrada_dict.get('b'))
        precisao = utils.expr_val(entrada_dict.get('precisao'))
        expressao = utils.expr_val(entrada_dict.get('expressao'))
        iteracoes = entrada_dict.get('iteracoes')
        if expressao is None or a is None or b is None or precisao is None:
            raise ValueError("Entrada inválida")
    else:
        # Entrada via arquivo
        entrada = utils.abrir_entrada("bisseccao", input_file)
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
    # Cria diretório de saída se não existir
    if output_path is not None:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as arquivo_saida:
            utils.escrever_arquivo(arquivo_saida, f'k{"":<10}a{"":<11}b{"":<11}f(a){"":<8}f(b){"":<9}|x-xk|/xk{"":<7}xk{"":<7}f(xk)\n')
            result = bisseccao(expressao, a, b, precisao, arquivo_saida)
            for k, v in result.items():
                a = v['a']
                b = v['b']
                fa = v['f(a)']
                fb = v['f(b)']
                aprox_relativa = v['desvio_relativo']
                xk = v['xk']
                fxk = v['f(xk)']
                utils.escrever_arquivo(arquivo_saida, f'{k:<7}\t{a:.5f}{"":<5}{b:.5f}{"":<5}{fa:.5f}{"":<5}{fb:.5f}{"":<5}{aprox_relativa:.5f}{"":<5}{xk:.5f}{"":<5}{fxk:.5f}\n')
            else:
                utils.escrever_arquivo(arquivo_saida, '\nNao foi possivel encontrar uma raiz')
    else:
        return bisseccao(expressao, a, b, precisao, iteracoes)

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
        output_path = os.path.join(utils.diretorio_atual, 'outputs', 'bisseccao', "exercicio_3.1.txt")
    run_bisseccao(input_file=input_file, output_path=output_path)

if __name__ == "__main__":
    main()
