# FUNÇÃO

def fatorial (a):
    fat = 1

    for i in range (1, num+1):
        fat = fat * i
    return fat


# SOFTWARE

num=int(input("Digite um numero: "))

while (num < 1):
     print ("Digite um numero positivo")
     num=int(input("Digite um numero: "))

resultado = fatorial(num)

print ("O Resultado fatorial de {} é: {}".format(num, resultado))


