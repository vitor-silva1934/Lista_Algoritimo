def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero-1)

numero = 5
resultado = fatorial(numero)
print(f'O fatorial de {numero} é {resultado}')
