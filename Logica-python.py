# exercícios de logica em python 

#Sintaxe Básica
#python
nome = "Alice"
idade = 30
print(f"Nome: {nome}, Idade: {idade}")
#Estruturas de Controle

#Condicionais (if, elif, else)
idade = 20
if idade < 18:
    print("Menor de idade")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
#Loops (for, while)
# Usando for
for i in range(5):
    print(i)
# Usando while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

#Funções
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Mundo"))

#Listas e Dicionários
frutas = ["maçã", "banana", "cereja"]
print(frutas[0])  # Imprime "maçã"

#Dicionários
aluno = {"nome": "Ana", "nota": 9.5}
print(aluno["nome"])  # Imprime "Ana"

#Compreensões de Lista
quadrados = [x ** 2 for x in range(10)]
print(quadrados)  # Imprime [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Exceções e Tratamento de Erros
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero não é permitida")