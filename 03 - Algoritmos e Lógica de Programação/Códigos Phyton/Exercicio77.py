# Exercicio 77

# || FUNÇÕES ||

def soma (a,b):
    c = a + b
    return c

def sub (a,b):
    c = a + b
    return c

def multi (a,b):
    c = a + b
    return c

def divisao (a,b):
    c = a + b
    return c

# || PROGRAMA PRINCIPAL ||

novaop = "S"

while novaop == "S":

    funcao = str(input ("A - SOMA || B - SUBTRAÇÃO || C - MULTIPLICAÇÃO || D - DIVISÃO: ")) 

    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite um numero: "))

    if funcao == "A":
        resultado = soma (n1,n2)
        
    elif funcao == "B":
        resultado = sub (n1, n2)

    elif funcao == "C":
        resultado = multi (n1, n2)

    elif funcao == "D":
        resultado = divisao (n1, n2)

    else:
        print ("Função não encontrada")
        
    print ("o resultdo é",resultado)

    novaop = str(input("Realizar nova operação [S/N]: "))
    

print ("PROGRAMA ENCERRADO")