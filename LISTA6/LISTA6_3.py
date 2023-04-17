n = int(input("Digite o número de termos: "))

numerador = 1
denominador = 1

soma = 0

for i in range(n):
    termo = numerador / denominador
    soma += termo
    
    print(f"{numerador}/{denominador}", end="")
    
    numerador += 1
    denominador += 2
    
    if i == n-1:
        print(f" = {soma:.2f}")
    else:
        print(" + ", end="")