# AnaliseNumerica
Repositorio para implementações de codigo de analise numerica encontrada no livro "Cálculo Numérico - Franco"


## Para rodar os codigos
- Crie um ambiente virtual
```bash
python -m venv venv
```
- Ative o ambiente virtual (Windows)
```bash
.\venv\Scripts\activate
```
- Ative o ambiente virtual (Linux/Mac)
```bash
source venv/bin/activate
```
- Instale as dependencias
```bash
pip install -r requirements.txt
```
- Rode o codigo desejado

## Relatorio 1

### Metodo bisseção
Para funções continuas f(x) é definido um intervalo [a,b] com f(a) e f(b) de sinais opostos, existe pelo menos uma raiz r em (a,b) tal que f(r) = 0.

O metodo faz diversas divisões do intervalo [a,b] até que a raiz seja encontrada com a precisão desejada.


- Passos
    1. Definir o intervalo [a,b] tal que f(a) e f(b) tenham sinais opostos
    2. Calcular o ponto médio xk = (a+b)/2
    4. Se f(xk) = 0, então xk é a raiz
    5. Se f(xk) != 0, verificar o sinal de f(xk)
    6. Se f(a) e f(xk) tiverem sinais opostos, então a raiz está no intervalo [a,xk], logo b = xk
    7. Se f(b) e f(xk) tiverem sinais opostos, então a raiz está no intervalo [xk,b], logo a = xk
    8. Repetir os passos 2 a 7 até que a precisão desejada seja alcançada
- Notas
    - Melhor metodo para verificar erro de aproximação é |xk - xk-1|/|xk|
    - Convergencia lenta: O numero de iterações pode ficar grande para alcançar a precisão desejada.
    - Comportamento oscilatorio que pode descartar uma boa aproximação da raiz.
    - Incondinicionalmente convergente: Sempre que f(a) e f(b) tiverem sinais opostos, o metodo sempre irá convergir para uma raiz em (a,b).
    - Facil de implementar 


### Metodo de falsa posiçao
O metodo de falsa posição escolhe como aproximação da raiz o ponto de interseção da reta que passa pelos pontos (a,f(a)) e (b,f(b)) com o eixo x. O extremo do intervalo de maior valor absoluto de f(x) permanece fixo, enquanto o outro extremo é substituído pela nova aproximação da raiz.

- Passos
    1. Definir o intervalo [a,b] tal que f(a) e f(b) tenham sinais opostos
    2. Calcular a aproximação da raiz xk = xb + (f(b)*(a-b))/(f(b)-f(a))
    3. Se f(xk) = 0, então xk é a raiz
    4. Se f(xk) != 0, verificar se o valor absoluto de f(a) é menor que o valor absoluto de f(b)
    5. Se f(a) * f(xk) < 0, então a raiz está no intervalo [a,xk], logo b = xk
    6. Se f(b) * f(xk) < 0, então a raiz está no intervalo [xk,b], logo a = xk
    7. Repetir os passos 2 a 6 até que a precisão desejada seja alcançada

- Notas
    - Melhor metodo para verificar erro de aproximação é |xk - xk-1|/|xk|
    - Convergencia lenta em curvas muito acentuadas.
    - Precisa calcular o valor absoluto da função.
    - Facil implementação
    - Geralmente converge mais rápido que o metodo da bisseção.
    - Aproximação continua da raiz
    - Avalia apenas uma vez f(x) por iteração

### Metodo de ponto fixo
Dada equação f(x) = 0 ela é reescrita isolando x, ou seja, x = g(x). O metodo de ponto fixo consiste em escolher um valor inicial x0 e calcular a sequência xk+1 = g(xk) até que a precisão desejada seja alcançada.

- Passos
    1. Reescrever a equação f(x) = 0 na forma x = g(x)
    2. Escolher um valor inicial x0
    3. Calcular a sequência xk+1 = g(xk)
    4. Repetir o passo 3 até que a precisão desejada seja alcançada

- Exemplos de reescrita
    - f(x) = x^2 - 2x + 3 = 0
        => x^2 + 3 = 2x
        => x = (x^2 + 3)/2
    - f(x) = sen x = 0
        => sen x = 0
        => senx + x = x
        => x = senx + x
    - f(x) = e^x - x = 0
        => e^x = x
        => x = e^x

- Notas
    - A escolha de x0 e a forma de g(x) são cruciais para a convergência do metodo.
    - Se |g'(x)| < 1 em um intervalo contendo a raiz, o metodo converge.
    - Se |g'(x)| > 1, o metodo diverge.
    - Convergência linear

### Metodo de Newton-Raphson
### Metodo da secante
## Relatorio 2
## Relatorio 3
