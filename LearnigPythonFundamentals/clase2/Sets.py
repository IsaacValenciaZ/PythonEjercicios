from django.template.defaultfilters import first

print('Ejemplo del uso de colecciones de tipos SET')

#Definir ejemplos de colecciones
first_collection = {1,2,3,4,5}
second_collection={3,4,5,6,7,8}


#Imprimir el contenido de un a coleccion de tipo SET
print(f'Mi coleccion de tipo set: {first_collection}')

#Remover un elemento de la coleccion REMOVE
first_collection.remove(4)

print(f'Mi coleccion actualizada: {first_collection}')

#Agregar un elemnto a la coleccion
first_collection.add('Hola mundo')
print(f'Mi coleccion actualizada, ADD: {first_collection}')

#Iteracion sobre una coleccion con un ciclo for
print('\n Impresion del contenido de la coleccion \n')
for item in first_collection:
    print(item)

#Operaciones con colecciones
union_set = first_collection.union(second_collection)
intersection_set =  first_collection.intersection(second_collection)
diference_set= first_collection.difference(second_collection)

print(f'Union de colecciones: {union_set}')
print(f'Interseccion de colecciones: {intersection_set}')
print(f'Diferencia en colecciones: {diference_set}')

