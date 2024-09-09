numeros = []


for i in range (1,6):
    num=int(input("Digite um numero: "))
    numeros.append(num)
    numeros.sort(reverse=True)

print (numeros)   