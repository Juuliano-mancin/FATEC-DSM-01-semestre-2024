num = 1
lista01 = []
lista02 = []
lista03 = []
lista04 = []
count01 = 0
count02 = 0
count03 = 0
count04 = 0

while (num != 0):
    
    num=int(input("Digite um numero[0 para encerrar]: "))
    while (num < 0) or (num > 100):
        print ("Numero invalido")
        break
    
    if (num == 0):
        print ("Programa encerrado")
        
    elif (num <= 25):
        lista01.append(num)
        count01 = count01 + 1
        print ("Lista 01:" ,lista01)
        print ("Numero de elementos na lista:" ,count01)
        
                
    elif (num <= 50):
        lista02.append(num)
        count02 = count02 + 1
        print ("Lista 02:" ,lista02)
        print ("Numero de elementos na lista:" ,count02)
        
    elif (num <= 75):
        lista03.append(num)
        count03 = count03 + 1
        print ("Lista 03:" ,lista03)
        print ("Numero de elementos na lista:" ,count03)
        
    else:
        lista04.append(num)
        count04 = count04 + 1
        print ("Lista 04:" ,lista04)
        print ("Numero de elementos na lista:" ,count04)
        

    