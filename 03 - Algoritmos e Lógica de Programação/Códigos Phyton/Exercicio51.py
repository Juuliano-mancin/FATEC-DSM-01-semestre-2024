nome=str(input("Digite seu nome: "))
n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))

media= (n1 + n2)/2

if media >=7:
    print("Parabens {} Você foi aprovado com média {}".format (nome, media))
    
else:
    print ("Você ficou com média {} e foi reprovado".format (media))