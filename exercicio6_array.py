nomes = ["keven","Angela","Anselmo","Tiago","Fernando","Juliana","Marcio","Paulo","Ana", "Hercúles"]
nome_input = input("Escreva o nome para ver se ela está presente em um array:\n")


existe = nome_input in nomes:
print(existe)
if existe:
    print("O nome",nome_input,"está na posição",nomes.index(nome_input))
else:
    print("valor não encontrado")
