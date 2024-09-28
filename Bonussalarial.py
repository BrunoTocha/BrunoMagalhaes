# Cálculo de Bônus Salarial
#Peça ao usuário para inserir seu salário e o tempo de serviço. Se o tempo de serviço
#for superior a 5 anos, conceda um bônus de 5% ao salário. Ao final deve ser mostrado o salário atualizado.

salario = float (input("Digite seu salario: "))

tempo = int(input("Digite o tempo de serviço:  "))

if tempo < 5:
    print("Voce nao tem bonus!")
    
else:
    salario
    print(f"o valor do seu novo salario é de: {salario + salario*0.05}")
