# Guia de Lógica de Programação em Python

### Python é uma linguagem conhecida por sua simplicidade e legibilidade, tornando-a ideal para iniciantes e desenvolvedores experientes. Vamos explorar alguns conceitos fundamentais:
----------
![](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHVreG52NWdsZW1zY3B0dWYzeWg1NG14dXZuN2xwZzRoMHFxc2t1dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/coxQHKASG60HrHtvkt/giphy.gif)
# 1 Sintaxe Básica
````
nome = "Alice"
idade = 30
print(f"Nome: {nome}, Idade: {idade}")
````
# 2 Estruturas de Controle
````
Condicionais (if, elif, else)
python
idade = 20
if idade < 18:
    print("Menor de idade")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
Loops (for, while)
python
# Usando for
for i in range(5):
    print(i)

# Usando while
contador = 0
while contador < 5:
    print(contador)
    contador += 1
`````` 
# 3 Funções
````
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Mundo"))
````
# 4 Listas e Dicionários
````
frutas = ["maçã", "banana", "cereja"]
print(frutas[0])  # Imprime "maçã"
Dicionários
python
aluno = {"nome": "Ana", "nota": 9.5}
print(aluno["nome"])  # Imprime "Ana"
````
 # 5 Compreensões de Lista
````
quadrados = [x ** 2 for x in range(10)]
print(quadrados)  # Imprime [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
````
# 6 Exceções e Tratamento de Erros
````
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero não é permitida")`
`````
#### Python oferece muitos outros recursos poderosos, mas esses são alguns dos fundamentos para começar a desenvolver lógica de programação na linguagem.