import sympy as sp

def regressao_linear(pontos):
    soma_x = 0
    soma_y = 0
    soma_xy = 0
    soma_x2 = 0
    n = len(pontos)
    
    for i in pontos:
        soma_x += i.x
        soma_y += i.y
        soma_xy += i.x*i.y
        soma_x2 += i.x**2
    
    a1 = (n*soma_xy - soma_x*soma_y)/(n*soma_x2 - soma_x**2)
    a0 = (soma_y - (a1*soma_x))/n
    
    residuo = residuo(pontos, a0, a1)
    Sr = Sr(residuo)
    desvio_padrao = desvio_padrao(Sr, n)
    St = St(pontos, n, soma_y)
    cof_det = coeficiente_determinacao(St, Sr)
    cof_cor = sp.sqrt(cof_det)
    
    return a0, a1, cof_det, cof_cor, desvio_padrao
    


def coeficiente_determinacao(St, Sr):
    return (St - Sr)/St


def Sr(residuo):
    Sr = 0
    for i in residuo:
        Sr += i**2
    return Sr

def St(pontos, n, soma_y):
    St = 0
    
    for i in range(n):
        St += (pontos[i].y - (soma_y/n))**2
        
    return St
        

def residuo(pontos, a0, a1):
    residuo = []
    for i in range(len(pontos)):
        residuo.append(pontos[i].y - (a0 + a1*pontos[i].x))
    return residuo

def desvio_padrao(Sr, n):
    if n == 2:
        return None
    return (Sr/(n-2))**(1/2)
    