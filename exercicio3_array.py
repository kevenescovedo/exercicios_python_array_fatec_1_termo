nome = ["keven","Angela","Anselmo","Tiago","Fernando","Juliana","Marcio","Paulo","Ana", "Hercúles"]
massa = [60,65,67,88,78,65,90,78,62,100]
peso_maximo = max(massa)

indice_nome_max = massa.index(peso_maximo)
print(nome[indice_nome_max], "Tem altura maxima de",peso_maximo,"Kg")
peso_minimo = min(massa)
indice_nome_min = massa.index(peso_minimo)

print(nome[indice_nome_min], "Tem altura minima de",peso_minimo,"Kg")

print("-----------------------------------------------------------")
contador = 0;
for peso in massa:
    if contador == 0:
        peso_maior = peso
        peso_menor = peso
    
    else:
        if peso >= peso_maior:
            peso_maior = peso
        elif peso <= peso_menor:
            peso_menor = peso
    contador = contador + 1;
indice_nome_maior = massa.index(peso_maior)
indice_nome_menor = massa.index(peso_menor)
print(nome[indice_nome_maior], "Tem altura maxima de",peso_maior,"Kg")
print(nome[indice_nome_menor], "Tem altura maxima de",peso_menor,"Kg")


            
    
    
