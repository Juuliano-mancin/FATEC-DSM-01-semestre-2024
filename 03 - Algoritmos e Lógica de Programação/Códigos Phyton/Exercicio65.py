# 65) Escreva um algoritmo para calcular uma progressão aritmetica
# O usuario entrará com o primeiro termo [a1] e a quantidade de termos [an] e a razão da PA

print ("PROGRESSÃO ARITIMÉTICA")
a1 = int(input("Digite o primeiro termo: "))
an = int(input("Digite a quantidade de termos da PA: "))
rz = int(input("Digite a razão: "))
resp = a1


for i in range (0,an):
    if i <= an:
        print ("a{} --- {}" .format(i+1, resp))
        resp += rz
        
        
    