# Calculadora Simples
#Peça ao usuário para inserir dois números e uma operação (+, -, *, /).
#Realize a operação e exiba o resultado

numero1 = float(input("Digite o primeiro numero:"))

numero2 = float(input("Digite o segundo:"))

operacao = (input("Digite a operacao desejada:"))

if operacao == "+":
    print(f"A soma deles é : {numero1 + numero2}")
    
elif operacao == "-":
    print(f"A subtracao deles é : {numero1 - numero2}")
        
elif operacao == "/":
    if numero2 == "0":
    print("Nao é possivel dividir por zero")
    
    else
    print(f"o resultado dessa operacao é : {numero1 / numero2}")
    
elif operacao == "*":
    print(f"A multiplicacao desses numeros é de: ")
    
else:
    print (f"Operacao invalida")