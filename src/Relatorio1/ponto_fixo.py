import sympy as sp
import src.utils as utils 
import os 

x = sp.symbols('x')

def ponto_fixo(expressao, x0, precisao, i_max=100) -> dict | None:
    result = {}
    k = 1
    desvio_relativo = float('inf')
    xk = x0.evalf()
    while k <= i_max and desvio_relativo > precisao:
        x_old = xk
        
        xk = float((expressao.subs(x, x_old)).evalf())
        fxk = float((expressao.subs(x, xk)).evalf())
        
        desvio_relativo = abs(xk - x_old)/xk
        result[k] = {'k': k, 'xk': x_old, 'f(xk)': fxk, 'desvio_relativo': desvio_relativo}
        k += 1
    return result
    
def run_ponto_fixo(entrada_dict: dict = None): 
    x0 = utils.expr_val(entrada_dict.get('x0'))
    precisao = utils.expr_val(entrada_dict.get('precisao'))
    expressao = utils.expr_val(entrada_dict.get('expressao'))
    iteracoes = entrada_dict.get('iteracoes')
    if expressao is None or x0 is None or precisao is None:
        raise ValueError("Entrada inválida")
    
    return ponto_fixo(expressao, x0, precisao, iteracoes)