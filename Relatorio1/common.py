import sympy as sp


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
def abrir_entrada(nome_arquivo):
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
    variaveis = sp.simbols('x0:%d' % n)
    
    # calcula solução do sistema
    matriz_solucao = sp.solve(matrizA*matrizX - matrizB, variaveis)
    
    
    # retorna a matriz solução
    return matriz_solucao
