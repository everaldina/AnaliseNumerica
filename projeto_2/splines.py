import sympy as sp

def calc_subinterval(expression: sp.Expr, x_vector: list[float], c_vector: list[float], i: int) -> sp.Expr:
    """Calcula a expressão do spline cúbico para o subintervalo i de [x_i, x_{i+1}].
    
    Args:
        expression (sp.Expr): Expressão simbólica da função original.
        x_vector (list[float]): Lista dos pontos x onde a função é avaliada.
        c_vector (list[float]): Lista dos coeficientes c calculados para os splines.
        i (int): Índice do subintervalo atual.
    Returns:
        sp.Expr: Expressão simbólica do spline cúbico no subintervalo i.
    """
    x = sp.symbols('x')
    h = x_vector[i+1] - x_vector[i]
    a = expression.subs(x, x_vector[i])
    a_seguinte = expression.subs(x, x_vector[i+1])
    b = (1/h*(a_seguinte - a)) - (h/3 * (2*c_vector[i] + c_vector[i+1]))
    d = (c_vector[i+1] - c_vector[i]) / (3*h)
    
    spline_expression = a + b*(x - x_vector[i]) + c_vector[i]*(x - x_vector[i])**2 + d*(x - x_vector[i])**3
    
    # retorna expressao simplificada
    return sp.simplify(spline_expression).evalf()

def calc_c_values(expression: sp.Expr, x_vector: list[float], condicao: str) -> list[float]:
    """Calcula os valores dos coeficientes c para os splines cúbicos com base na condição de contorno fornecida.
    Args:
        expression (sp.Expr): Expressão simbólica da função original.
        x_vector (list[float]): Lista dos pontos x onde a função é avaliada.
        condicao (str): Condição de contorno ('natural' ou 'fixada').
    Returns:
        list[float]: Lista dos coeficientes c calculados.
    """
    n = len(x_vector)
    h_vector = [x_vector[i+1] - x_vector[i] for i in range(n-1)]
    f_vector = [expression.subs(sp.symbols('x'), x_vector[i]) for i in range(n)]
    
    if condicao.lower() in ('natural', 'livre'):
        A, B = condicao_contorno_natural(f_vector, h_vector)
    elif condicao.lower() in ('fixada', 'controle', 'fixado'):
        A, B = condicao_contorno_fixada(expression, x_vector, f_vector, h_vector)
    else:
        raise ValueError("Condição de contorno inválida. Use 'natural' ou 'fixada'.")
    
    c_values = sp.linsolve((A, B))
    if not c_values:
        raise ValueError("O sistema linear não tem solução.")
    
    return list(list(c_values)[0])
        
        
def condicao_contorno_fixada(expression: sp.Expr, x_vector: list[float], f_vector: list[float], h_vector: list[float]) -> tuple[sp.Matrix, sp.Matrix]:
    """Calcula as matrizes A e B para o sistema linear dos coeficientes c com condição de contorno fixada.
    Args:
        expression (sp.Expr): Expressão simbólica da função original.
        x_vector (list[float]): Lista dos pontos x onde a função é avaliada.
        f_vector (list[float]): Lista dos valores da função nos pontos x.
        h_vector (list[float]): Lista dos intervalos entre os pontos x.
    Returns:
        tuple[sp.Matrix, sp.Matrix]: Matrizes A e B do sistema linear.
    """
    n = len(x_vector)
    A = sp.zeros(n, n)
    B = sp.zeros(n, 1)
    
    # preenche a matriz A 
    for i in range(n):
        for j in range(n):
            dif_ij = j - i
            if abs(dif_ij) > 1:
                continue
            
            # diagonal principal
            if dif_ij == 0:
                if i == 0 or i == n-1:
                    A[i, j] =  h_vector[0] if i == 0 else h_vector[-1]
                    A[i, j] *= 2
                else:
                    A[i, j] = 2 * (h_vector[i-1] + h_vector[i])
            else:
                A[i, j] = h_vector[min(i, j)]
                
    # preenche o vetor B
    diff_x0 = expression.diff(sp.symbols('x')).subs(sp.symbols('x'), x_vector[0])
    diff_xn = expression.diff(sp.symbols('x')).subs(sp.symbols('x'), x_vector[-1])
    print("Derivadas nos extremos [a, b]:")
    sp.pprint(diff_x0)
    sp.pprint(diff_xn)
    for i in range(n):
        if i == 0:
            B[i] = (3/h_vector[0]) * (f_vector[i+1] - f_vector[i]) - 3 * diff_x0
        elif i == n-1:
            B[i] = 3 * diff_xn - (3/h_vector[-1]) * (f_vector[i] - f_vector[i-1])
        else:
            B[i] = (3/h_vector[i]) * (f_vector[i+1] - f_vector[i]) - (3/h_vector[i-1]) * (f_vector[i] - f_vector[i-1])
        
    return A, B

def condicao_contorno_natural(f_vector: list[float], h_vector: list[float]) -> tuple[sp.Matrix, sp.Matrix]:
    """Calcula as matrizes A e B para o sistema linear dos coeficientes c com condição de contorno natural.
    Args:
        f_vector (list[float]): Lista dos valores da função nos pontos x.
        h_vector (list[float]): Lista dos intervalos entre os pontos x.
    Returns:
        tuple[sp.Matrix, sp.Matrix]: Matrizes A e B do sistema linear.
    """
    n = len(f_vector)
    A = sp.zeros(n, n)
    B = sp.zeros(n, 1)
    
    A[0, 0] = 1  # primeira linha
    A[n-1, n-1] = 1  # ultima linha
    
    
    # preenche o matriz A
    for i in range(1, n-1):
        for j in range(n):
            dif_ij = j - i
            if abs(dif_ij) > 1:
                continue
            
            # diagonal principal
            if dif_ij == 0:
                A[i, j] = 2 * (h_vector[i-1] + h_vector[i])
            else:
                A[i, j] = h_vector[min(i, j)]
          
    # preenche o vetor B
    for i in range(1, n-1):
        B[i] = (3/h_vector[i]) * (f_vector[i+1] - f_vector[i]) - (3/h_vector[i-1]) * (f_vector[i] - f_vector[i-1])      
    
        
    return A, B

def get_splines(expression_str: str, lista_x: list[float], condicao: str) -> list[sp.Expr]:
    """Gera os splines cúbicos para os pontos fornecidos e a condição de contorno especificada.
    Args:
        expression_str (str): Expressão da função original como string.
        lista_x (list[float]): Lista dos pontos x onde a função é avaliada.
        condicao (str): Condição de contorno ('natural' ou 'fixada').
    Returns:
        list[sp.Expr]: Lista das expressões simbólicas dos splines cúbicos.
    """
    expression = sp.sympify(expression_str)
    c_vector = calc_c_values(expression, lista_x, condicao)
    n = len(lista_x)
    splines = []
    
    for i in range(n-1):
        spline_i = calc_subinterval(expression, lista_x, c_vector, i)
        splines.append(spline_i)
        
    return splines