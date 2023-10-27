import sympy as sp
from .. import common

def interpolacao_newton(ponto):
    n = len(ponto)
    # lista para armazenas as diferencas divididas
    lista_diferencas = []
    
    for i in range(n-1):
        lista_diferencas.append(ponto[i].y)
        
def diferenca_dividida(pontos, indices):
    n = len(indices)
    
    # caso base da primeira dividida
    if n == 2:
        return (pontos[indices[0]].y - pontos[indices[1]].y)/(pontos[indices[0]].x - pontos[indices[1]].x)
    else: # recursao para o resto dos casos
        return (diferenca_dividida(pontos, indices[:-1]) - diferenca_dividida(pontos, indices[1:]))/(pontos[indices[n-1]].x - pontos[indices[0]].x)
        
    
