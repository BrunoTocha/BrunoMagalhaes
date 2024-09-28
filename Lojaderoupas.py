# # Atividade - Loja de Roupas
# Uma loja de roupas precisa de um programa que ajude a calcular o valor final da venda de produtos. Existem algumas regras que precisam ser respeitadas na venda de um produto:
 
# 1 – A vista – 10% de desconto, caso o valor da venda seja maior que 500 15%, caso seja maior que 1000, 20% de desconto;
# 2 – A prazo – A venda pode ser parcelada em até 18x. Caso seja parcelado em mais do que 10x possui juros:
# Apenas compras com mais de 800 reais podem ser parceladas acima de 5x;
# Juros:
#         #   1 – 11 vezes: 5% de juros ao mês.
#         #   2 – 12 vezes: 6.5% de juros ao mês.
#         #   3 – 13 vezes: 7% de juros ao mês.
        #   4 – 14 vezes: 9% de juros ao mês.
        #   5 – 15 vezes: 9.5% de juros ao mês.
        #   6 – 16 vezes: 10% de juros ao mês.
        #   7 – 17 vezes: 11.3% de juros ao mês.
        # #   8 – 18 vezes: 12% de juros ao mês. 

# O usuário informa o valor total da compra, a forma de pagamento e o numero de parcelas. Ao final o programa mostra o valor final.


ValorTotal = float (input("informe o valor de sua compra: "))

FormaPagamento = (input("Formas de pagamentos: \n 1 = A vista \n 2 = A prazo\n Digite a opcao desejada: "))

if FormaPagamento == "1":
        print(f"O valor da sua compra é de {ValorTotal-0.10}")
        
elif FormaPagamento == "2":
        print(f"gg")
        
else:
        print("Opcao invalida")


