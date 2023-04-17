n = int(input("Digite o número de termos que deseja gerar na sequência: "))

if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    a, b = 1, 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c