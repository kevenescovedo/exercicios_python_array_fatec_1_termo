numeros = []
positivos = []
negativos = []
i = 0;

while i < 10:
    numeros.append(int(input("Digite o numero inteiro:\n")))
    i =  i + 1;

    
for numero in numeros:
   
        if numero > 0:
          positivos.append(numero)
        elif numero < 0:
          negativos.append(numero)
            
print("vetor de numeros negativos", negativos)
print("vetor de numeros positivos", positivos)
    
        
    
    
        
        
    
    
