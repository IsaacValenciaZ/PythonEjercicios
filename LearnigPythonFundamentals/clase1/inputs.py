#Entrada de datos mediante la consola INPUT

name = input("¿Cual es tu nombre?")
age = int(input("¿Cual es tu edad?"))
salary = float(input("¿Cual es tu salario?"))
total_pets = eval(input("¿Cuantas mascotas tienes?")) #lo tranforma a otro tipode dato
university = input("¿Cual es tu Universidad?")


print(f"Hola me llamo {name}, mi edad es {age} y el nombre de mi universidad es {university}")

print(type(name))
print(type(age))
print(type(salary))
print(type(total_pets))



