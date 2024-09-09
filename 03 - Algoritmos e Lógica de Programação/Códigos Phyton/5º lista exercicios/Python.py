num = int(input("Digite um numero: "))

if (num == 2):
    print ("Numero Primo")

else:
    resultado = num % 2

    if (resultado == 0):
        print ("Não é Numero Primo")
    
    else:


        for i in range (3, num):

            resultado = num / i
            i =+ 2
                
        if (resultado == 1):

            print ("Não é Numero Primo")
            print (resultado)

        else:

            print ("Numero Primo")
            print (resultado)
