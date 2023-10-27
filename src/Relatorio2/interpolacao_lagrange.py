import sympy as sp
from .. import common

x = sp.symbols('x')

def interpolacao_lagrange(pontos):
    n = len(pontos)
    
    # monta polinomio chamando lagrange para cada ponto e multiplicando pelo y do ponto
    polinomio = 0
    for i in range(n):
        polinomio += pontos[i].y*lagrange(pontos, i)

# retorna o polinomio de lagrange k, para n pontos, k = 0, 1, 2, ..., n-1
def lagrange(pontos, k):
    n = len(pontos)
    polinomio = 1
    
    for i in range(n):
        if i != k:
            polinomio *= (x - pontos[i].x)/(pontos[k].x - pontos[i].x)
    return polinomio    
    