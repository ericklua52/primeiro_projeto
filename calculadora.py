# Função para exibir a tabuada
def tabuada(numero):
    for i in range(1, 11):  # A tabuada vai de 1 a 10
        print(f"{numero} x {i} = {numero * i}")

# Solicita ao usuário um número
numero = int(input("Digite o número para ver a tabuada: "))

# Exibe a tabuada do número fornecido
tabuada(numero)