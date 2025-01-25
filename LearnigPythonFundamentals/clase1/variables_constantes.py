#variable generada de forma implicita

from clase1.hello_world import message
message = "Hello Python World " #fines de lectura rapido de codigo


#variable generada de forma explicita
number_x: int = 10

print(type(message))
print(type(number_x))

#Declaracion de una constante
MAX_CONNECTIONS = 50

print(MAX_CONNECTIONS)

MAX_CONNECTIONS = 10
print(MAX_CONNECTIONS)
