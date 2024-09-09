# Exercicio 76

# Função

def calculo (a ,b):
    c = (b/a) * 100
    return c


# Programa Principal

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

resultado = calculo (n1, n2)

print ("{} é {} % de {}" .format(n2, resultado, n1))
