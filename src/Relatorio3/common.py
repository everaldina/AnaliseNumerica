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
