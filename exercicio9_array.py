i = 1;
numeros = []
npar = 0;
nimpar = 0;
soma = 0;

while i <= 101:
    numeros.append(i)
    i = i + 1;
print(numeros)
contador = 0;
for n in numeros:
    
    if contador == 0:
        maior = n
        menor = n
    else:
        if n >= maior:
            maior = n
        elif n <= menor:
            menor = n
    contador = contador + 1;
    soma = n + soma
    if n % 2 == 0:
        npar = npar + 1;
    else:
        nimpar = nimpar + 1;
     

print("Maior número: ",maior)
print("Maior número: ", menor)
print("Percentual de numeros pares: ", (npar * 100)/100)
print("Percentual de numeros impares: ",(nimpar * 100)/100)
print("Média de elementos:", soma/100)
            
         
    
