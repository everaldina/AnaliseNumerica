import sympy as sp
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
 
# retorna o valor da expressão se ela for valida, caso contrario retorna None   
def expr_val(expressao):
    try:
        # tenta analisar a expressão
        expressao_analisada = sp.sympify(expressao)
        
        return expressao_analisada
    
    #caso nao seja uma expressao valida
    except (sp.SympifyError, ValueError) as e:
        return None
    
# escreve no arquivo de saida
def escrever_arquivo(arquivo, dados):
    if arquivo is not None:
        try:
            arquivo.write(dados)
        except Exception as e:
            return None
    else:
        return None
    
# abre o arquivo de entrada o conteudo
def abrir_entrada(metodo, nome_arquivo):
    nome_arquivo = os.path.join(diretorio_atual, 'inputs', metodo, nome_arquivo)
    try:
        with open(nome_arquivo, 'r') as arquivo:
            entrada = arquivo.read()
    except FileNotFoundError:
        return None
    
    return entrada

def result_sistema(matrizA, matrizB, matrizX):
    n = sp.shape(matrizA)[0]
    variaveis = sp.symbols('x0:%d' % n)
    
    # calcula solução do sistema
    solucao = sp.solve(matrizA*matrizX - matrizB, variaveis)
    

    # cria matriz solucao
    matriz_solucao = sp.Matrix([])
    for i in range(n):
        matriz_solucao = matriz_solucao.row_insert(i, sp.Matrix([solucao[variaveis[i]]]))
    
    # retorna a matriz solução
    return matriz_solucao


# retorna um polinomio a partir de um vetor de coeficientes
def criar_polinomio(vet_a, var):
    n = len(vet_a)
    polinomio = ""
    for i in range(n):
        if i == 0:
            polinomio += str(vet_a[i,0]) + " + (" 
        elif i == n-1:
            polinomio += str(vet_a[i,0]) + "* " + str(var) +"**" + str(i) + ")"
        else:
            polinomio += str(vet_a[i,0]) + "* "+ str(var) + "**" + str(i) + ") + ("
            
    return sp.sympify(polinomio)