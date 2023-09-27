import sympy as sp
import common
    
x = sp.symbols('x')


def bisseccao(expressao, a, b, precisao, arquivo_saida):
    if common.check_solution(expressao, a, b):
        k = 1
        while True:
            fa = expressao.subs(x, a)
            fb = expressao.subs(x, b)
            
            # calcula o ponto médio
            xk = (a + b) / 2
            
            # calcula f(xk)
            fxk = expressao.subs(x, xk)
            
            # calcula o erro
            aprox = abs(b - a)
            aprox_relativa = aprox/abs(b)
            
            # escreve no arquivo de saida
            common.escrever_arquivo(arquivo_saida, f'{k:<7}\t{a:.5f}{"":<5}{b:.5f}{"":<5}{fa:.5f}{"":<5}{fb:.5f}{"":<5}{aprox:.5f}{"":<5}{aprox_relativa:.5f}{"":<5}{xk:.5f}{"":<5}{fxk:.5f}\n')
            
            # caso f(xk) = 0, então xk é a raiz
            if fxk == 0:
                return xk
            
            # verifica se o erro é menor que a tolerância
            if aprox_relativa < precisao:
                return xk
            
            k += 1
            if fa * fxk < 0: # verifica se f(a) * f(xk) < 0
                b = xk
            elif fxk * fb < 0: # verifica se f(xk) * f(b) < 0
                a = xk
            else: # caso não seja possível encontrar uma raiz
                return None
    else:
        return None
    

def main():
    input = "G:\Meu Drive\\facul\\analise numerica\Relatorio 1\input.txt"
    output = "G:\Meu Drive\\facul\\analise numerica\Relatorio 1\outputbis.txt"
    
    
    entrada = common.abrir_entrada(input)
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
        arquivo_saida = open(output, 'w')
        common.escrever_arquivo(arquivo_saida, f'k{"":<10}a{"":<11}b{"":<11}f(a){"":<8}f(b){"":<9}e{"":<9}e/|bk|{"":<7}xk{"":<7}f(xk)\n')
        raiz = bisseccao(expressao, a, b, precisao, arquivo_saida)
        common.escrever_arquivo(arquivo_saida, '\ne = |(bk - ak)|\n')
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

    