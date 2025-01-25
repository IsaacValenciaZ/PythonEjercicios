print('Ejemplo de tuplas\n\n')

#Definicion de una tupla

tupla_information = ('Rafael Isaac', 22, 99.5)
print(f'Informacion de la tupla: {tupla_information}')

#Destructuracion o unpacking
full_name, age, salary = tupla_information
print(f'Nombre: {full_name}, edad: {age}, salario: {salary}')

print('\nImpresion de la tupla con un ciclo for')
#Impresion de los elemntos de un tupla

for item in tupla_information:
    print(item)
