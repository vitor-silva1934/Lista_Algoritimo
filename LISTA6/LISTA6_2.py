salario = float(input("Digite o salário inicial: "))

percentual = 0.015

ano_atual = 2023

for ano in range(2005, ano_atual + 1):
    if ano >= 2006:
        percentual *= 2
    aumento = salario * percentual
    salario += aumento

print(f"O salário atual é R${salario:.2f}.")