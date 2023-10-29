import sympy as sp
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# retorna true se existe pelo menos uma raiz no intervalo [a, b]
def check_solution(expressao, a, b):
    x = sp.symbols('x')
    
    # calcula f(a) e f(b)
    fa = expressao.subs(x, a)
    fb = expressao.subs(x, b)

    # pelo teorema Teorema 3.1
    # se f(a) * f(b) < 0, então existe pelo menos uma raiz no intervalo [a, b] 
    if fa * fb < 0:
        return True
    else:
        return False
 
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

def check_sistema_solucao(matrizA, matrizB, matrizX,):
    # verifica se as matrizes nao estao vazias
    if matrizA is None or matrizX is None or matrizB is None:
        return False
    
    # verifica se a matriz A é quadrada
    if sp.shape(matrizA)[0] != sp.shape(matrizA)[1]:
        return False
    
    # verifica se a matriz A tem a mesma quantidade de linhas que a matriz B e X
    if sp.shape(matrizA)[0] != sp.shape(matrizB)[0] or sp.shape(matrizA)[0] != sp.shape(matrizX)[0]:
        return False
    
    # verifica se a matriz B e X tem apenas uma coluna
    if sp.shape(matrizB)[1] != 1 or sp.shape(matrizX)[1] != 1:
        return False
    
    # verifica se a determinante de A é diferente de 0
    if matrizA.det() == 0:
        return False
    else:
        return True

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

def print_matriz(matriz, nome, tipo = 'n'):
    linha, coluna = sp.shape(matriz)
    tamNome = len(nome)
    result_print = ""
    
    
    for i in range(linha):
        if (i == int(linha/2) and coluna !=1) or linha == 1 or (coluna == 1 and i == 0):
            result_print += f"{nome} = |  "
        elif coluna != 1:
            result_print += f"{'':<{tamNome + 3}}|  "
        for j in range(coluna):
            if tipo == 'n':
                result_print += f"{matriz[i,j]:.4f}{'':<2}"
            elif tipo == 's':
                result_print += f"{matriz[i,j]}{'':<4}"
        if coluna != 1:
            result_print += f"|\n"
    if coluna == 1:
        result_print += f"|"
    return result_print

# Retorna eabsoluto e erelativo
# eabsoluto = || x(k+1) - x(k) ||oo
# erelativo = || x(k+1) - x(k) ||oo / || x(k+1) ||oo
def return_variacao(vet_1, vet_0):
    k1_norm_inf = vet_1.norm(sp.oo)
    sk1_k0_norm_inf = (vet_1 - vet_0).norm(sp.oo)
    return sk1_k0_norm_inf, (sk1_k0_norm_inf / k1_norm_inf).evalf()
    
     

# Ve se uma matriz B (matriz de iteraçao) converge pra solução
# Pelo Corolario 5.1 - (Critério Geral de convergência)
# O processo iterativo definido por é convergente se para qualquer norma de matrizes, || B || < 1       
def check_converge(matrizB):
    if matrizB.norm() < 1: # verifica se norma euclidiana é menor que 1
        return True
    elif matrizB.norm(1) < 1: # verifica se norma de coluna é menor que 1
        return True
    elif matrizB.norm(sp.oo) < 1: # verifica se norma de linha é menor que 1
        return True
    else:
        return False
    

# retorno matriz B para o sistema Ax = b, para x = B x + g, onde:
# B = I − A
# g = b
#
# I: matriz identidade
# A: matriz dos coeficientes
# b: matriz dos termos independentes
def return_matrizB(matrizA, n):
    
    # cria matriz quadrada n x n com zeros
    matrizB = sp.zeros(n)
    
    # para isolar variavei i, cada elemento Bi,j é igual a -Ai,j/Ai,i
    for i in range(n):
        for j in range(n):
            if i != j:
                matrizB[i,j] = -matrizA[i,j]/matrizA[i,i]
    return matrizB


# retorno vetor B para o sistema Ax = b, para x = B x + g, onde:
# B = I − A
# g = b
#
# I: matriz identidade
# A: matriz dos coeficientes
# b: matriz dos termos independentes
def return_vetorG(matrizA, matrizB, n= None):
    # se n for None, n = numero de linhas da matriz A
    if n is None:
        n = sp.shape(matrizA)[0]
    
    # vetorG recebe matrizB
    vetorG = matrizB.copy()
    
    # cada elemento Gi,0 é dividido por coeficiente Ai,i
    for i in range(n):
        vetorG[i,0] /= matrizA[i,i]
    return vetorG

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