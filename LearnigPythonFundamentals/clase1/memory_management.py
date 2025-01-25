numero_x = 10
numero_y = 20

address_id_x = id(numero_x)
address_id_y = id(numero_y)

print(" *** Antes de  actualizar la variable x ***")
print(address_id_x)
print(address_id_y)

numero_x = 20

address_id_x = id(numero_x)

print("\n *** Despues de actualizar la variable x ***")

print(address_id_x)
print(address_id_y)