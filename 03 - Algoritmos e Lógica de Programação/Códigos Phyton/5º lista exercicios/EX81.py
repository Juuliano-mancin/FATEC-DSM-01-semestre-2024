# Função

def somatoria (a):
    b = 0
    for i in range (1, a+1):
        b = b + i               # || variavel b = recebe a soma dos valores do contador || 0 = 0 + 1 ------> 1 = 1 + 2 ------> 2 = 2 + 3 || 
    return b

# Software

num=int(input("Digite um numero: "))

resultado = somatoria(num)

print ("O Resultado é: {}".format(resultado))