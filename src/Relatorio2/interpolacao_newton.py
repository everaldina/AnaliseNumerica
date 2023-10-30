import sympy as sp
import common
import os



def interpolacao_newton(ponto):
    n = len(ponto)
    # lista para armazenas as diferencas divididas
    lista_diferencas = []
    
    indice = []
    for i in range(n):
        indice.insert(0, i) 
        lista_diferencas.append(diferenca_dividida(ponto, indice))
    
    polinomio = ""
    for i in range(len(lista_diferencas)):
        if i == 0:
            polinomio += str(float(lista_diferencas[i].evalf())) + " + "
        else:
            polinomio += str(float(lista_diferencas[i].evalf()))
            for j in range(i):
                polinomio += f"*(x - {ponto[j].x})"
                if j == i - 1:
                    if i != 1:
                        polinomio += ")"
                    if i < len(lista_diferencas) - 1:
                        polinomio += " + ("
    return str(sp.simplify(polinomio))
            
    
        
def diferenca_dividida(pontos, indices):
    n = len(indices)
    
    if n == 2: # caso base da primeira dividida
        return (pontos[indices[0]].y - pontos[indices[1]].y)/(pontos[indices[0]].x - pontos[indices[1]].x)
    elif n == 1:
        return pontos[indices[0]].y
    else: # recursao para o resto dos casos
        return (diferenca_dividida(pontos, indices[1:])-diferenca_dividida(pontos, indices[:-1]))/(pontos[indices[n-1]].x - pontos[indices[0]].x)
        
    
def main():
    ##### EXERCICIO 10.2 #####
    #input = "exercicio_10.2.txt"
    #output = "exercicio_10.2.txt"
    ##### EXERCICIO 10.9 #####
    #input = "exercicio_10.9.txt"
    #output = "exercicio_10.9.txt"
    
    metodo = "interpolacao_newton"
    entrada = common.abrir_entrada(metodo, input)
    if entrada is None:
        return
    else:
        entrada = entrada.split('\n') # separando as linhas
        
        pontos = []
        # criando pontos
        for i in entrada:
            coordenadas = i.split(' ')
            pontos.append(sp.Point(float(coordenadas[0]), float(coordenadas[1])))   
        

    # caminho do arquivo de saida
    arquivo_saida =  os.path.join(common.diretorio_atual, 'outputs', metodo, output)
    arquivo_saida = open(arquivo_saida, 'w')
    
    # return polinomio
    polinimio = interpolacao_newton(pontos)
    
    common.escrever_arquivo(arquivo_saida, f"f(x) = {polinimio}")
    
    
    arquivo_saida.close()
    return


if __name__ == "__main__":
    main()