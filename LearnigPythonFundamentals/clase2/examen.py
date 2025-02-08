
nombre = input("Ingresa tu nombre: ")
materias = int(input("Ingresa el número de materias: "))


suma = 0


for i in range(materias):
    calif = float(input(f"Ingresa la calificación de la materia #{i+1}: "))
    suma += calif


promedio = suma / materias

print(f"\n{nombre}  El promedio de su cuatrimestre: {promedio:.2f}")
