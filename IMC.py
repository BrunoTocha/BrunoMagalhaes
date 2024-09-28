nome = (input("Digite seu nome: "))

peso = float(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))

imc = peso / (altura**2)

print("Olá")

print(f"{nome} O seu IMC é de: {imc:.2f}")