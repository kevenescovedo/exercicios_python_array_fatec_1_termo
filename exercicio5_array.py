numeros = [10,7,9,8,12,5,0,2]
for number in numeros:
    if number % 2 == 0:
        print(number,"é par está na posição",numeros.index(number),"do array")
