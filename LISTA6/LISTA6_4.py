N = int(input("Digite o valor de N: "))

H = 0

for i in range(1, N+1):
    H += 1/i

print(f"O valor de H com {N} termos é {H:.2f}")