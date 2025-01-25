from itertools import count

print('Manejo de las listas en PYTHON\n\n')

#Declaracion de una lista
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'Valores actuales de mi lista: {my_list}' )
my_list.append(0)
my_list.append(11)
print(f'Valores modificacdos de mi lista: {my_list}')

#Ordenar los elemtos de mis lista mediante SORT
my_list .sort()

print(f'Los elementos de mi listas han sido ordenados: {my_list}')

#Modificar y eliminar un elemento de mi lista
my_list[0] = 'Esta es una cadena'

my_list.pop()
print(f'Valores actuales de mi lista, ejemplo POP: {my_list}')


#Creacion de una sublista [0:5]
my_sublist = my_list[0:5]

print(f'Valores actuales de mi sublista: {my_sublist}')

#Imprimir los valores de mi lista
print(f'\n\nEstos son los elementos de mi lista, los cuales seran impresos mediante un ciclo for')
count = 0
for item in my_list :

    print(f'Elemento de mi lista {count} - {item}')
    count += 1