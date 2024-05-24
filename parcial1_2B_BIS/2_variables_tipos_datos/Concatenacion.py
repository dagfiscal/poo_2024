#Formas de concatenacion en python

nombre="Dagoberto Fiscal"
especialidad="Área de SW multiplataforma"
carrera="Ingeniería en Gestión y Desarrollo de SW"

#1er forma
print("Mi nombre es "+nombre+" estoy en la especialidad de "+especialidad+" en la carrera de "+carrera)

print("\n")

#2da forma
print("Mi nombre es ",nombre," estoy en la especialidad de ",especialidad," en la carrera de ",carrera)

print("\n")

#3er forma FORMA COMUN EN PYTHON
print(f"Mi nombre es ,{nombre}, estoy en la especialidad de ,{especialidad}, en la carrera de ,{carrera}")

print("\n")

#4TA forma 
print("Mi nombre es ,{}, estoy en la especialidad de ,{}, en la carrera de ,{}".format(nombre,especialidad,carrera))

print("\n")


#5ta forma
print('Mi nombre es '+nombre+' estoy en la especialidad de '+especialidad+' en la carrera de '+carrera)

print("\n")


