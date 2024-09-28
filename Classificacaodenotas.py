 #Classificação de Notas
#Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como
#"A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "F" (abaixo de 60).

nota = (input("Digite sua nota: "))

if nota >= "90" <= "100":
    print(f"Sua nota é A")
    
elif nota >= "80":
    print(f"Sua nota é B")
    
elif nota >= "70":
    print(f"Sua nota é C")
    
elif nota >= "60":
    print(f"Sua nota é D")
    
elif nota < "60":
    print(f"voce esta reprovado!")
    