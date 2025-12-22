
def obter_indice_intervalo(lista_x: list[float], x: float) -> int:
    """Retorna o índice do intervalo em que o valor x se encontra na lista de pontos lista_x.
    Args:
        lista_x (list[float]): Lista dos pontos x onde a função é avaliada.
        x (float): Valor para o qual se deseja encontrar o intervalo.
    Returns:
        int: Índice do intervalo onde x se encontra.
    """
    n = len(lista_x)
    if x < lista_x[0] or x > lista_x[-1]:
        raise ValueError("x está fora do intervalo dos pontos fornecidos.")
    
    for i in range(n - 1):
        if lista_x[i] <= x <= lista_x[i + 1]:
            return i
    
    raise ValueError("Intervalo não encontrado para o valor de x fornecido.")
    
    
