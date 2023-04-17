# Pede ao usuário para digitar um número
num = int(input("Digite um número: "))

# Inicializa a potência como 1
potencia = 1

# Repete enquanto a potência for menor ou igual ao número informado
while potencia <= num:
    # Imprime a potência atual
    print(potencia)
    
    # Calcula a próxima potência, que é o dobro da atual
    potencia = potencia * 2
