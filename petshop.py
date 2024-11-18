nome=input("Insira o nome do cachorrinho: ")
idade= int(input("insira a idade do cachorro: "))
porte=int(input("qual o porte dele, lembrando que 1:Grande, 2:Médio e 3:Pequeno "))
banho=int(input("quantos banhos ele tomou: "))

idadepet=idade*7

grande=1

medio=2

pequeno=3




if porte==grande :
     p_grande=float(75-20)*banho
     print(f"Olá,{nome}, tem, {idadepet},anos e nos ultimos 12 meses o lucro com este animal foi de {p_grande}")

elif porte==medio :
     p_medio=float(60-15)*banho
     print(f"Olá,{nome}, tem, {idadepet},anos e nos ultimos 12 meses o lucro com este animal foi de {p_medio}")

elif porte==pequeno :
     p_pequeno=float(50-5)*banho
     print(f"Olá,{nome}, tem,{idadepet},anos e nos ultimos 12 meses o lucro com este animal foi de {p_pequeno}")
else :
      print("PORTE NÃO INDENTIFICADO") 














