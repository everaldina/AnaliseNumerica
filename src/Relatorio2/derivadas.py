import sympy as sp

x = sp.Symbol('x')

def derivada_progressiva(expressao, ponto, h): 
    f_x1, f_x, h = sp.symbols("f_x1 f_x h")
    
    # formula da derivada progressiva
    derivada = sp.simplify("(f_x1 - f_x)/h")
    
    # substitui os valores na formula da derivada
    return derivada.subs(f_x1, expressao.subs(x, ponto.x + h).evalf()).subs(f_x, expressao.subs(x, ponto.x).evalf()).subs(h, h).evalf()


def derivada_retardada(expressao, ponto, h): 
    f_x1, f_x, h = sp.symbols("f_x1 f_x h")
    
    # formula da derivada retardada
    derivada = sp.simplify("(f_x - f_x1)/h")
    
    # substitui os valores na formula da derivada
    return derivada.subs(f_x1, expressao.subs(x, ponto.x - h).evalf()).subs(f_x, expressao.subs(x, ponto.x).evalf()).subs(h, h).evalf()

def derivada_central(expressao, ponto, h): 
    f_x1, fpx1, h = sp.symbols("f_x1 fpx1 h")
    
    # formula da derivada central
    derivada = sp.simplify("(fpx1 - f_x1)/(2*h)")
    
    # substitui os valores na formula da derivada
    return derivada.subs(f_x1, expressao.subs(x, ponto.x - h).evalf()).subs(fpx1, expressao.subs(x, ponto.x + h).evalf()).subs(h, h).evalf()

