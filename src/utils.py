import sympy as sp
import os
from typing import Optional, Any

diretorio_atual = os.path.dirname(os.path.abspath(__file__))


def analisar_limite(expressao, x, ponto, lado='both'):
    """Analisa se o limite tende a +inf ou -inf"""
    try:
        # Tenta limite pela direita e pela esquerda
        if lado == 'direita' or lado == 'both':
            lim_dir = sp.limit(expressao, x, ponto, '+')
        if lado == 'esquerda' or lado == 'both':
            lim_esq = sp.limit(expressao, x, ponto, '-')
        
        # Se ambos os lados tendem ao mesmo infinito, retorna esse valor
        if lado == 'both':
            if lim_dir == lim_esq and lim_dir in [sp.oo, -sp.oo]:
                return lim_dir
            elif lim_dir in [sp.oo, -sp.oo]:
                return lim_dir
            elif lim_esq in [sp.oo, -sp.oo]:
                return lim_esq
        
        if lado == 'direita' and lim_dir in [sp.oo, -sp.oo]:
            return lim_dir
        if lado == 'esquerda' and lim_esq in [sp.oo, -sp.oo]:
            return lim_esq
            
    except:
        pass
    
    return None

def check_solution(expressao, a, b):
    """Retorna true se existe pelo menos uma raiz no intervalo [a, b]"""
    x = sp.symbols('x')
    
    # calcula f(a) e f(b)
    fa = expressao.subs(x, a)
    fb = expressao.subs(x, b)

    return fa * fb < 0
 
def expr_val(expressao: Any) -> sp.Expr | None:
    """Retorna o valor da expressão se ela for válida, caso contrário retorna None."""
    try:
        return sp.sympify(expressao)
    except (sp.SympifyError, ValueError, TypeError):
        return None
    
def escrever_arquivo(arquivo, dados):
    """Escreve os dados no arquivo de saida"""
    if arquivo is not None:
        try:
            arquivo.write(dados)
        except Exception as e:
            return None
    else:
        return None
    
def abrir_entrada(metodo, nome_arquivo):
    """Abre o arquivo de entrada e retorna o conteudo"""
    nome_arquivo = os.path.join(diretorio_atual, 'inputs', metodo, nome_arquivo)
    try:
        with open(nome_arquivo, 'r') as arquivo:
            entrada = arquivo.read()
        return entrada
    except FileNotFoundError:
        return None

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


def criar_polinomio(vet_a, var):
    """ Retorna um polinomio a partir de um vetor de coeficientes"""
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

def return_variacao(vet_1, vet_0):
    """ Retorna eabsoluto e erelativo
    eabsoluto = || x(k+1) - x(k) ||oo
    erelativo = || x(k+1) - x(k) ||oo / || x(k+1) ||oo
    
    """
    k1_norm_inf = vet_1.norm(sp.oo)
    sk1_k0_norm_inf = (vet_1 - vet_0).norm(sp.oo)
    return sk1_k0_norm_inf, (sk1_k0_norm_inf / k1_norm_inf).evalf()
    
         
def check_converge(matrizB):
    """ 
    Retorna True se a matriz B converge para a solução, False caso contrario
    
    Pelo Corolario 5.1 - (Critério Geral de convergência)
    O processo iterativo definido por é convergente se para qualquer norma de matrizes, || B || < 1
    """
    if matrizB.norm() < 1: # verifica se norma euclidiana é menor que 1
        return True
    elif matrizB.norm(1) < 1: # verifica se norma de coluna é menor que 1
        return True
    elif matrizB.norm(sp.oo) < 1: # verifica se norma de linha é menor que 1
        return True
    else:
        return False
    

def return_matrizB(matrizA, n):
    """
    Retorna a matriz B para o sistema Ax = b, para x = B x + g, onde:
    B = I − A
    g = b
    I: matriz identidade
    A: matriz dos coeficientes
    b: matriz dos termos independentes
    n: numero de linhas/colunas da matriz A
    
    """
    
    # cria matriz quadrada n x n com zeros
    matrizB = sp.zeros(n)
    
    # para isolar variavei i, cada elemento Bi,j é igual a -Ai,j/Ai,i
    for i in range(n):
        for j in range(n):
            if i != j:
                matrizB[i,j] = -matrizA[i,j]/matrizA[i,i]
    return matrizB


def return_vetorG(matrizA, matrizB, n= None):
    """ Retorna o vetor G para o sistema Ax = b, para x = B x + g, onde:
    B = I − A
    g = b
    I: matriz identidade
    A: matriz dos coeficientes
    b: matriz dos termos independentes
    n: numero de linhas/colunas da matriz A
    """
    # se n for None, n = numero de linhas da matriz A
    if n is None:
        n = sp.shape(matrizA)[0]
    
    # vetorG recebe matrizB
    vetorG = matrizB.copy()
    
    # cada elemento Gi,0 é dividido por coeficiente Ai,i
    for i in range(n):
        vetorG[i,0] /= matrizA[i,i]
    return vetorG