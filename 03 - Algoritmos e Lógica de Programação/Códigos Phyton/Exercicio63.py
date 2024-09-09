# Exercicio 63
# Algoritmo que carregue a lista de numeros [10 11 12 13 14 15 16]
# Digitar um numero da lista e em seguida substitui o numero digitado pelo numero "7"

numeros = [10, 11, 12, 13, 14 ,15, 16]
num = int(input("Digite um numero entre 10 e 16: "))

for i in range (0,7):
    if  numeros[i] == num:
        numeros[i] = 7

print (numeros)
