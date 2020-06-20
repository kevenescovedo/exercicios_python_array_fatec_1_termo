
notas = [10.0,7.5,9.0,8.8,7.8,8.5,9.0,9.8,6.2,7.0]
qtd_mais = 0
qtd_menos = 0
soma = sum(notas)
divisor = len(notas)
media = soma/divisor
for nota in notas:
    if nota > media:
        qtd_mais = qtd_mais + 1
    elif nota < media:
        qtd_menos = qtd_menos + 1
print("Houve",qtd_mais,"notas maiores que",media)
print("Houve",qtd_menos,"notas maiores que",media)
        

    
