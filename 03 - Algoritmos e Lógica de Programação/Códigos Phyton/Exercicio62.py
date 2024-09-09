# Escreva um algoritmo que carregue uma lista com seis numeros e informe
# para o usuario qual o maior numero da lista e em qual posição da lista
# ele se encontra

#base = 0
#
#print ("LISTA DE NÚMEROS")
#numeros = [1, 4, 3, 6, 2, 5]
#
#print (numeros)
#
#for n in numeros:
#    if n > base:
#        base = n        
#    else:
#        base = base
#        
#print ("O maior numero é {}, ".format (base))

print("-------SOLUÇÃO---------")

print ("LISTA DE NUMEROS")
numeros = [1, 4, 3, 6, 2, 5]    # Lista de numeros com valores pré-definidos
nmaior = 0                      # Variavel auxiliar para encontrar o maior numero
print (numeros)                  # Imprimi todos os elementos da lista de numeros
for i in range (0,6):            # Contador de repetição onde "i" é o contador.
    
    if numeros [i] > nmaior:    # numeros [i] percorre os elementos da lista.
        nmaior = numeros [i]    # nmaior salva o valor apenas se o valor que está na posição i for maior que o valor anterior de nmaior
        pos = i                 # pos é uma variavel auxiliar que salva a posição do contador, somente quando a condição do if é verdadeira

print ("O maior numero é: {}, e a sua posição é: {}".format(nmaior, pos+1)) #pos+1 porque a primeira posição da lista é zero.