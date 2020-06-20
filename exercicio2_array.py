i = 0;
altura = [];
soma = 0;
contador = 0;
idade = []
while i <= 35:
    idade.append(int(input("Digite a idade do aluno:\n")))
    if idade[i] > 25:
       print("o aluno",i,"´tem uma idade  maior que 25 anos")
       contador = contador + 1
    altura.append(float(input("Digite a altura do aluno:\n")))
   
              
              
    soma = altura[i] + soma
    
    print(i)
    i = i + 1
media = soma/i
print("a média de soma das  alturas é de:",media)
print("a qtd de pessoas maiores que 25 anos é de:",contador)
    
                 
    
    
