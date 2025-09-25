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
- Exemplo de entrada

### Metodo de falsa posiçao
### Metodo de ponto fixo
### Metodo de Newton-Raphson
### Metodo da secante
## Relatorio 2
## Relatorio 3
