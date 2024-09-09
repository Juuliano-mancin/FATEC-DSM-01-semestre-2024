# Manipulando as listas

frutas = ["Laranja", "Amora","Morango", "Banana", "Amora", "Mamão", "Banana"]

for fruta in frutas:
    print(fruta)

print("Quantidade de amoras:", frutas.count("Amora")) # Conta a quantidade de items dentro da lista
print("Quantidade de mangas:", frutas.count("Manga")) # Conta a quantidade de items dentro da lista
print("Quantidade de mamão:", frutas.index("Mamão"))  # Mostra a posição do item selecionado na lista || Lista começa na posição zero

print ("Adicionando uva")
frutas.append("Uva") # Adiciona um elemento a lista || o elemento adicionado vai para a ultima posição da lista

print(frutas)

print ("Invertendo a lista")
frutas.reverse() # Inverte a posição dos itens da lista || 1 2 3 4 5 6 vai para 6 5 4 3 2 1

print (frutas)

print ("Ordenando a lista")
frutas.sort() # Ordena os elementos da lista em ordem crescente || alfabetica [A-Z] numeros de [0-9]

print (frutas)