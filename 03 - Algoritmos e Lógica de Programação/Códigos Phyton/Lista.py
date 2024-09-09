# Estrutura de dados - Listas

print ("----- Exemplo 01 -----")

nomes = ["Amanda", "Bruno","Camila","Davi", "Elen","Felipe"] # Lista de nomes || começa no numero 0
# Amanda = 0 || Bruno = 1 || Camila = 2 || ... || Felipe = 5

# Imprime apenas os nomes selecionados
print (nomes [1])
print (nomes [3])

print ("----- Exemplo 02 -----")

#Imprimi os nomes que estão especificados no laço de repetição
for i in range (0,6,2): # 0 e 6 valor inicial e final || 2 representa o valor que vai ser acrescentado no contador
    print (nomes [i])   # i recebe os valores de 0, 2 e 4 

print ("----- Exemplo 03 -----")

numeros = [1, 5, 12, 13, 20, 39]

print ("numeros originais")
for num in numeros: # "num" é uma variavel que está substituindo "i" || a variavel "i" não é obrigatória, mas sim uma convenção; podendo ser substituida quando necessario
    print (num)
    
print ("numeros alterados")
for num in numeros:
    print (num + 3)

print ("----- Exemplo 04 -----")