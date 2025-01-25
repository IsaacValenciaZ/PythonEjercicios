#Otros metodos
from operator import indexOf
message= "Los cuervos de la UTVT"

#len
size = len(message)

#replace
new_message = message.replace(' ',',')

#find
indexOf = message.find('U')

#split
message_sliced = message.split()

print(f'Longitud de la  cadena: {size}')
print(f'Nueva cadena: {new_message}')
print(f'Posicion del elemento buscado: {indexOf}')
print(f'Cadena particionada: {message_sliced}')



