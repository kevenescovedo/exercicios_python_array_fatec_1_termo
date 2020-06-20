vetor = []
i = 1
reverso = []
resposta = "S"
while resposta == "S":
    vetor.append(input("digite um elemento para um vetor:\n"))
    resposta = input("Deseja continuar a inserir se sim diga S e se não diga N:\n").upper()
    

for n in vetor:
    if i == 1:
       reverso.append(vetor[len(vetor)-1])
    else:
         reverso.append(vetor[len(vetor)- i])
    i = i + 1
print(reverso)

if vetor == reverso:
    print("é um palindromo")
else:
    print("não é palindromo")
        
        
        
    
    
