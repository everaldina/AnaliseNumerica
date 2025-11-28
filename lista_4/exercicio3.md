# Derivação da Regressão Linear Simples (Caso $n=2$)

Para exemplificar a construção do sistema, consideramos um conjunto definido de **2 pontos**: $(x_1, y_1)$ e $(x_2, y_2)$. O modelo é $y = a_0 + a_1x + e$.

### a) Funções Base
As funções que compõem o modelo são constantes e lineares:
* $z_0 = 1$
* $z_1 = x$
* $z_2..n = 0$

### b) Componentes da Formulação Matricial
A equação matricial é $\{Y\} = [Z]\{A\} + \{E\}$. Para o caso de 2 pontos:

* **Vetor Y:** $\{y_1, y_2\}^T$
* **Matriz Z:**
    $$
    Z = \begin{bmatrix}
    1 & x_1 \\
    1 & x_2
    \end{bmatrix}
    $$
* **Vetor A:** $\{a_0, a_1\}^T$
* **Vetor E:** $\{e_1, e_2\}^T$

### c) Matriz de Mínimos Quadrados $[Z]^T[Z]$
Calculamos a transposta $[Z]^T$ e multiplicamos pela matriz original:

$$
[Z]^T = \begin{bmatrix}
1 & 1 \\
x_1 & x_2
\end{bmatrix}
$$

Realizando a multiplicação matricial:

$$
[Z]^T[Z] = \begin{bmatrix}
1 & 1 \\
x_1 & x_2
\end{bmatrix} \cdot
\begin{bmatrix}
1 & x_1 \\
1 & x_2
\end{bmatrix} = 
\begin{bmatrix}
2 & (x_1 + x_2) \\
(x_1 + x_2) & (x_1^2 + x_2^2)
\end{bmatrix} =
\begin{bmatrix}
n & \sum x_i \\
\sum x_i & \sum x_i^2
\end{bmatrix}

$$

### d) Vetor Independente $[Z]^T\{Y\}$

$$
[Z]^T\{Y\} = \begin{bmatrix}
1 & 1 \\
x_1 & x_2
\end{bmatrix} \cdot
\begin{bmatrix} y_1 \\ y_2 \end{bmatrix} =
\begin{bmatrix}
(1\cdot y_1 + 1\cdot y_2) \\
(x_1\cdot y_1 + x_2\cdot y_2)
\end{bmatrix} =
\begin{bmatrix}
\sum y_i \\
\sum x_i y_i
\end{bmatrix}
$$


## Conclusão
Com isso, ao expandirmos a formulação matricial $[Z]^T[Z]\{A\} = [Z]^T\{Y\}$ para um modelo de regressão polinomial ($y = a_0 + a_1x$), obtemos o seguinte sistema de equações normais (SELA):
$$\begin{bmatrix}
n & \sum x_i  \\
\sum x_i & \sum x_i^2 
\end{bmatrix}
\begin{bmatrix} a_0 \\ a_1 \end{bmatrix} =
\begin{bmatrix}
\sum y_i \\
\sum x_i y_i
\end{bmatrix}$$
A resolução deste sistema linear nos fornece diretamente os coeficientes $a_0$ e $a_1$ que minimizam o erro quadrático do ajuste.