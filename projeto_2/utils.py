
def obter_indice_intervalo(lista_x: list[float], x: float) -> int:
    n = len(lista_x)
    if x < lista_x[0] or x > lista_x[-1]:
        raise ValueError("x está fora do intervalo dos pontos fornecidos.")
    
    for i in range(n - 1):
        if lista_x[i] <= x <= lista_x[i + 1]:
            return i
    
    raise ValueError("Intervalo não encontrado para o valor de x fornecido.")
    
    
