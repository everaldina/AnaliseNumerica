import sympy as sp
import common



def interpolacao_newton(ponto):
    n = len(ponto)
    # lista para armazenas as diferencas divididas
    lista_diferencas = []
    
    indice = []
    for i in range(n):
        indice.insert(0, i) 
        lista_diferencas.append(diferenca_dividida(ponto, indice))
        
def diferenca_dividida(pontos, indices):
    n = len(indices)
    
    if n == 2: # caso base da primeira dividida
        return (pontos[indices[0]].y - pontos[indices[1]].y)/(pontos[indices[0]].x - pontos[indices[1]].x)
    elif n == 1:
        return pontos[indices[0]].y
    else: # recursao para o resto dos casos
        return (diferenca_dividida(pontos, indices[:-1]) - diferenca_dividida(pontos, indices[1:]))/(pontos[indices[n-1]].x - pontos[indices[0]].x)
        
    
