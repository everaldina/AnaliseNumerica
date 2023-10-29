import sympy as sp
import common
import os

x = sp.symbols('x')

def interpolacao_lagrange(pontos):
    n = len(pontos)
    
    # monta polinomio chamando lagrange para cada ponto e multiplicando pelo y do ponto
    polinomio = 0
    for i in range(n):
        polinomio += pontos[i].y*lagrange(pontos, i)
    
    return sp.simplify(sp.sympify(polinomio)).evalf()

# retorna o polinomio de lagrange k, para n pontos, k = 0, 1, 2, ..., n-1
def lagrange(pontos, k):
    n = len(pontos)
    polinomio = 1
    
    for i in range(n):
        if i != k:
            polinomio *= (x - pontos[i].x)/(pontos[k].x - pontos[i].x)
    return polinomio


def main():
    ##### EXERCICIO 10.2 #####
    #input = "exercicio_10.2.txt"
    #output = "exercicio_10.2.txt"
    ##### EXERCICIO 10.9 #####
    #input = "exercicio_10.9.txt"
    #output = "exercicio_10.9.txt"
    
    
    metodo = "interpolacao_lagrange"
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
    polinimio = interpolacao_lagrange(pontos)
    
    common.escrever_arquivo(arquivo_saida, f"f(x) = {polinimio}")
    
    
    arquivo_saida.close()
    return


if __name__ == "__main__":
    main()