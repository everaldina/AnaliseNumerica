import sympy as sp

def regressao_linear(pontos): 
    # iniciando somatorios
    soma_x = 0
    soma_y = 0
    soma_xy = 0
    soma_x2 = 0
    n = len(pontos)
    
    # calculando somatorios
    for i in pontos:
        soma_x += i.x
        soma_y += i.y
        soma_xy += i.x*i.y
        soma_x2 += i.x**2
    
    # calculando a0 e a1
    a1 = (n*soma_xy - soma_x*soma_y)/(n*soma_x2 - soma_x**2)
    a0 = (soma_y - (a1*soma_x))/n
    
    # calculando medidas de dispersao
    residuo = residuo(pontos, a0, a1)
    Sr = Sr(residuo)
    desvio_padrao = desvio_padrao(Sr, n)
    St = St(pontos, n, soma_y)
    cof_det = coeficiente_determinacao(St, Sr)
    cof_cor = sp.sqrt(cof_det)
    
    return a0, a1, cof_det, cof_cor, desvio_padrao
    

# retorna o coeficiente de determinação
def coeficiente_determinacao(St, Sr):
    return (St - Sr)/St

# retorna Sr
def Sr(residuo):
    Sr = 0
    for i in residuo:
        Sr += i**2
    return Sr

# retorna St
def St(pontos, n, soma_y):
    St = 0
    
    media_y = soma_y/n
    for i in range(n):
        St += (pontos[i].y - media_y)**2
        
    return St
        
# retorna o vetor de residuos
def residuo(pontos, a0, a1):
    residuo = []
    for i in range(len(pontos)):
        residuo.append(pontos[i].y - (a0 + a1*pontos[i].x)) # y - (a0 + a1*x)
    return residuo

# retorna o desvio padrão
def desvio_padrao(Sr, n):
    if n == 2:
        return None
    return (Sr/(n-2))**(1/2)
    