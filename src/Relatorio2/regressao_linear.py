import sympy as sp
import common
import os

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
    a1 = ((n*soma_xy - soma_x*soma_y)/(n*soma_x2 - soma_x**2)).evalf()
    a0 = ((soma_y - (a1*soma_x))/n).evalf()
    
    # calculando medidas de dispersao
    res = residuo(pontos, a0, a1)
    sr = Sr(res)
    d_padrao = (desvio_padrao(sr, n)).evalf()
    st = St(pontos, n, soma_y)
    cof_det = (coeficiente_determinacao(st, sr)).evalf()
    cof_cor = (sp.sqrt(cof_det)).evalf()
    
    return a0, a1, cof_det, cof_cor, d_padrao
    

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


def main():
    ##### EXERCICIO 8.1 #####
    #input = "exercicio_8.1.txt"
    #output = "exercicio_8.1.txt"
    ##### EXERCICIO 8.11 #####
    #input = "exercicio_8.11.txt"
    #output = "exercicio_8.11.txt"
    
    metodo = "regressao_linear"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n') # separando as linhas
        
        pontos = []
        # criando pontos
        for i in entrada:
            coordenadas = i.split(' ')
            
            # para funcao linear
            pontos.append(sp.Point(float(coordenadas[0]), float(coordenadas[1])))
            
            # para caso de funcao potencial
            #pontos.append(sp.Point(sp.log(float(coordenadas[0])), sp.log(float(coordenadas[1]))))
        

    # caminho do arquivo de saida
    arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
    arquivo_saida = open(arquivo_saida, 'w')
    
    # return a0, a1, cof_det, cof_cor, desvio_padrao
    a0, a1, coef_determinacao, coef_correlacao, desvio_padrao = regressao_linear(pontos)
    
    
    
    # escrevendo resultado para funcao linear
    common.escrever_arquivo(arquivo_saida, f"f(x) = {a0} + {a1}x\n")
    common.escrever_arquivo(arquivo_saida, f"a0 = {a0} | a1 = {a1}\n")
    
    # escrevendo resultado para funcao potencial
    #common.escrever_arquivo(arquivo_saida, f"f(x) = {sp.exp(a0)}x^{a1}\n")
    #common.escrever_arquivo(arquivo_saida, f"a = {sp.exp(a0)} | b = {a1}\n")
    
    # escrevendo medidas estatisticas
    common.escrever_arquivo(arquivo_saida, f"r^2 = {coef_determinacao}\n")
    common.escrever_arquivo(arquivo_saida, f"r = {coef_correlacao}\n")
    common.escrever_arquivo(arquivo_saida, f"S(x/y) = {desvio_padrao}")
    
    arquivo_saida.close()
    return
        
        

if __name__ == "__main__":
    main()