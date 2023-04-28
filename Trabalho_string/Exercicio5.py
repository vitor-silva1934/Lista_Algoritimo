# A funcionalidade do comando split no python é de permite dividir o conteúdo da variável de acordo com as condições especificadas em cada parâmetro da função ou com os valores predefinidos por padrão.

objetos = "copo, garrafa, colher, faca, garfo"

# Vai dividir a string em uma lista, usando a virgula como separador.
lista_objetos = objetos.split(",")

# Irá mostrar os objetosseparados por linha.
print("Os objetos separados são:")
for objeto in lista_objetos:
    print(objeto)


#RECADO PARA O PROFESSOR: caso o programa não rode, pode retirar so comentarios, pois estão bugando a funcionalidade desles.