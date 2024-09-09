import random
#importa uma biblioteca para gerar numeros aleatórios

print ("------------------------")
print ("   Jogo de Adivinhação  ")
print ("------------------------")

segredo = random.randrange (1, 11)
#print (segredo) # Numero sorteado

acertou = False
tentativas = 3

for i in range (1, 4):
    print ("Você possui", tentativas, "tentativas de 3\n")
    numero = int(input("Digite um numero entre 1 e 10: "))
    
    if numero > 10 or numero < 0:
        print ("Numero invalido")
    
        if numero == segredo:
            acertou = True
            
        if acertou:
                
            print ("--------------------------------")
            print (" VOCÊ ACERTOU !!! PARABENS  !!! ")
            print ("--------------------------------")
            break
            
        else:
                
                print ("Você errou! Tente Novamente\n")
                tentativas -= 1
        
print ("O numero correto era: ", segredo)
print ("fim de jogo")


