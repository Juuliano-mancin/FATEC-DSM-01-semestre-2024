print ("--------------------")

def saudacao ():
    print ("Ola Mundo!")

# PROGRAMA PRINCIPAL
saudacao()

print ("--------------------")

def contaletras(texto):
    tamanho = len(texto)
    print ("Quantidade de letras em {} é {} letras".format(texto, tamanho))
    
# PROGRAMA PRINCIPAL

contaletras ("João")
contaletras ("Maria")


print ("--------------------")

def soma (a, b):
    c = a + b
    return c # A Função soma retorna o que está na variavel c || No caso a soma de a + b ||

# PROGRAMA PRINCIPAL

resultado = soma (3, 4)
print ("A soma é: ", resultado)

resultado = soma (8, 7)
print ("A soma é: ", resultado)

print ("--------------------")

