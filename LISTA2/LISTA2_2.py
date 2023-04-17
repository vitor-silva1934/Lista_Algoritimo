numero = int(input("Digite um número para a tabuada: "))

# Itera de 1 a 10 e imprime o resultado da multiplicação
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
