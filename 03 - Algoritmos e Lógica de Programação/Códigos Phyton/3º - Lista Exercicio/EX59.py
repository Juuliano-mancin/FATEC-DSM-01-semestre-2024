nome = str(input("Digite seu nome: "))
n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))
n3 = float(input("Digite a 3° nota: "))

media = (n1 + n2 + n3)/3

if media >= 7:
    print ("Parabens {}, você foi aprovado".format(nome))
elif media >= 5:
    print ("Você ficou com a media {} e está de recuperação".format(media))
else:
    print ("{} você está reprovado.".format(nome))
    
print ("FIM")