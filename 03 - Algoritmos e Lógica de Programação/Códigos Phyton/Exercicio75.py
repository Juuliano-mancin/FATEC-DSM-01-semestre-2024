# Exercicio 75

def area (b, h):
    a = b * h
    return a

# Programa Principal

b = float(input("Digite a largura do terreno: "))
h = float(input("Digite o comprimento do terreno: "))

areatotal = area (b,h)

print ("A area do terreno é de {} metros quadradados" .format(areatotal))