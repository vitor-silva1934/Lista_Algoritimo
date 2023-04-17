numero = int(input("Digite um número: "))
 
if numero > 1:
   # Verificar se é divisível por algum número menor que ele
   for i in range(2, numero):
       if (numero % i) == 0:
           print(numero, "não é primo")
           break
   else:
       print(numero, "é primo")
else:
   print(numero, "não é primo")
