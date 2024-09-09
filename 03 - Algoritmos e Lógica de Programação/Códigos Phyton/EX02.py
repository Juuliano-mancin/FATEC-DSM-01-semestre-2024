# Tipagem de variaveis

n1 = int(input ("Digite um numero: "))
n2 = int(input ("Digite outro numero: "))
soma = n1 + n2
print ("A soma é: ",soma)
print ("A soma de {} + {} = {}" .format (n1, n2, soma))
print (f"A soma é: {soma}")

# Desvio Condicional 01

idade = int(input("Digite sua idade: "))

if idade > 18:
    print ("maior de idade")
else:
    print ("menor de idade")
    
print ("Programa Encerrado")

# Desvio condicional 02

aluno = str(input("É aluno ? [s/n]: "))

if aluno == "s" or aluno == "S" :
    print ("Bem Vindo Aluno")
elif aluno == "n" or aluno == "N" :
    print ("Bem Vindo Convidado")
else:
    print ("Opção Inválida")
    
print ("Programa encerrado")

