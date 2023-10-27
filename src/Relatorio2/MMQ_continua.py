from .. import common
import sympy as sp

x = sp.Symbol('x')

def aproximacao_polinomia(expressao, grau, limite_inf, limite_sup):
    mat_X = sp.zeros(grau - 1, grau - 1)
    vet_A = sp.zeros(grau - 1, 1)
    vet_fx = sp.zeros(grau - 1, 1)
    
    
    for i in range (grau - 1):
        # preenchendo mat_X
        for j in range (grau - 1):
            if i > j:
                mat_X[i,j] = mat_X[j,i]
            else:
                # calculando integral de x^i*x^j de limite_inf a limite_sup
                mat_X[i,j] = sp.integrate(x**i * x**j, (x, limite_inf, limite_sup))
        
        # preenchendo vet_fx
        # calculando integral de f(x)*x^i de limite_inf a limite_sup
        vet_fx[i,0] = sp.integrate(expressao * (x**i), (x, limite_inf, limite_sup))
    
    # calculando matriz A
    common.result_sistema(mat_X, vet_fx, vet_A)
    
    return vet_A