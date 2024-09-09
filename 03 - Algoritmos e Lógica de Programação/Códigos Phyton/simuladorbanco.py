print ("----------------------------------")
print ("    Seja bem vindo ao MyBank      ")
print ("    Simulador de emprestimos      ")
print ("----------------------------------")

cliente = str(input ("Cliente [S/N]: "))


emprestimo = float(input("Valor do emprestimo R$:"))
parcelas = int(input("numero parcelas: "))
segdesemprego = str(input("Seguro desemprego [s/n]"))

iof = 0.0038 

if segdesemprego == "S" or segdesemprego == "s":
    segurodesemprego = 50
else:
    segurodesemprego = 0

if cliente == "s" or cliente == "S":
    
    juros = 0.03
    
    totaljuros = emprestimo * parcelas * juros #Valor Total do Juros
    
    valoremprestimo = (totaljuros + emprestimo + segurodesemprego) #Valor total do emprestimo (com os juros)
    
    valoremprestimo_iof = (valoremprestimo) + (valoremprestimo * iof) #Valor total do emprestimo (com os juros) com IOF declarado
    
    valorparcela = valoremprestimo_iof / parcelas #Valor da parcela com juros e IOF
    
else:
    
    score = int (input ("SERASA Score: "))
    tarifa_cadastro = 35
    
    if score <= 299:
        
        juros = (20/100)
        totaljuros = emprestimo * parcelas * juros #Valor Total do Juros
        valoremprestimo = (totaljuros + emprestimo + segurodesemprego + tarifa_cadastro) #Valor total do emprestimo (com os juros)    
        valoremprestimo_iof = (valoremprestimo) + (valoremprestimo * iof) #Valor total do emprestimo (com os juros) com IOF declarado    
        valorparcela = valoremprestimo_iof / parcelas #Valor da parcela com juros e IOF
        
    elif score <= 499:
        
        juros = (15/100)
        totaljuros = emprestimo * parcelas * juros #Valor Total do Juros
        valoremprestimo = (totaljuros + emprestimo + segurodesemprego + tarifa_cadastro) #Valor total do emprestimo (com os juros)    
        valoremprestimo_iof = (valoremprestimo) + (valoremprestimo * iof) #Valor total do emprestimo (com os juros) com IOF declarado    
        valorparcela = valoremprestimo_iof / parcelas #Valor da parcela com juros e IOF
        
    elif score <= 699:
        
        juros = (10/100)
        totaljuros = emprestimo * parcelas * juros #Valor Total do Juros
        valoremprestimo = (totaljuros + emprestimo + segurodesemprego + tarifa_cadastro) #Valor total do emprestimo (com os juros)    
        valoremprestimo_iof = (valoremprestimo) + (valoremprestimo * iof) #Valor total do emprestimo (com os juros) com IOF declarado    
        valorparcela = valoremprestimo_iof / parcelas #Valor da parcela com juros e IOF
        
    else:
        
        juros = (5/100)
        totaljuros = emprestimo * parcelas * juros #Valor Total do Juros
        valoremprestimo = (totaljuros + emprestimo + segurodesemprego + tarifa_cadastro) #Valor total do emprestimo (com os juros)    
        valoremprestimo_iof = (valoremprestimo) + (valoremprestimo * iof) #Valor total do emprestimo (com os juros) com IOF declarado    
        valorparcela = valoremprestimo_iof / parcelas #Valor da parcela com juros e IOF
        

print ("Quantidade de parcelas: ",parcelas)
print ("Valor das parcelas: ", valorparcela)
print ("Custo efetivo total:", valoremprestimo_iof)


