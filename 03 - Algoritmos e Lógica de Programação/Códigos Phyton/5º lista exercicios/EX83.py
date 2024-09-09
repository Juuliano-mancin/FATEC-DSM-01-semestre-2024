numeros = []
maior = 0

for i in range (1,6):
    num=int(input("Digite um numero: "))
    numeros.append(num)         # ADICIONA O NUMERO DIGITADO NA LISTA
    
    verificador = num           # VERIFICA O NUMERO DIGITADO
    if (maior < verificador): 
        maior = verificador     # GUARDA O MAIOR NUMERO DIGITADO
        
numeros.sort()                  # ORGANIZA A LISTA DO MENOR PARA O MAIOR

print (numeros)                 # IMPRIMIR A LISTA
        
print ("O maior numero é: {}".format(maior)) # IMPRIMI O MAIOR NUMERO DA LISTA