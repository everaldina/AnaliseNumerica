import sympy as sp
from .. import common

x = sp.symbols('x')


# retorna o polinomio de lagrange k, para n pontos, k = 0, 1, 2, ..., n-1
def lagrange(pontos, k):
    n = len(pontos)
    polinomio = 1
    
    for i in range(n):
        if i != k:
            polinomio *= (x - pontos[i].x)/(pontos[k].x - pontos[i].x)
    return polinomio    
    