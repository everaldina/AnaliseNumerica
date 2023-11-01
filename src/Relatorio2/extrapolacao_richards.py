import sympy as sp
import common
import os
from integracao_trapezio import trapezio_multiplo

x = sp.symbols('x')

# retorna a extrapolação de richarda para uma expressao, usando duas aproximações de integrais por trapezio com n1 e n2 segmentos
# segue a formula: I = I2 + ((I2 - I1)/((h1/h2)^2 - 1))
def extrapolacao_richarda(expressao, limite_inf, limite_sup, n1, n2):
    # calcula as aproximações para de integrais para n1 e n2, usando a regra dos trapezios multiplos
    i1 = trapezio_multiplo(expressao, limite_inf, limite_sup, n1)
    i2 = trapezio_multiplo(expressao, limite_inf, limite_sup, n2)
    
    # calcula largura de cada segmento cada uma das integrais
    h1 = (limite_sup - limite_inf)/n1
    h2 = (limite_sup - limite_inf)/n2
    
    return i2 + ((i2 - i1)/((h1/h2)**2 - 1))


    
    