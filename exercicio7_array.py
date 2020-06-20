alturas = []
maiorqtd = 0;
posicao = [];
soma = 0;
divisor = 0;
media = 0;

resposta = "S"

while resposta == "S":
    alturas.append(float(input("Digite a altura da pessoa:\n")))
    resposta = input("deseja continuar digite S/N:").upper()
    
for altura in alturas:
    if altura > 1.80:
        maiorqtd = maiorqtd + 1
        posicao.append(alturas.index(altura))
        soma = soma + altura
        divisor = len(alturas)
        media = soma/divisor
print("HÁ",maiorqtd," alunos que tem altura maior de 1.80")
print("média de alunos quem tem altura maior que 1.80 é", media)
print("--------------------- posições dos alunos comforme a idade digitada----")
for p in posicao:
    print(p)
        
        
    
    
    
    
    
