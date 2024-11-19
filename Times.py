matricula=int(input("insira o número de Matricula: "))

def par_ou_impar (matricula):
    if matricula % 2==0:
        return("Você esta no time Azul!!!!!!")
    
    else:
        return("Você está no time Amarelo!!!!!!")
print(par_ou_impar(matricula))
