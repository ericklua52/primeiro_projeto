cliente=input("Insira seu nome: ")
mes=input("em que mês você fez a compra?: ")
valor=input("Valor Gasto: ")
desconto=43
cupom=(cliente+"É43")


print("Olá " + cliente + ", em " + mes + " você realizou uma compra no valor de R$" , float(valor) , " e ganhou um desconto de " , int(desconto) , "% em sua próxima compra. Use o cupom " + cupom)

