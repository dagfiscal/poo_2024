from conexionBD import *

try:
    micursor=conexion.cursor()

    nombre=input("¿Cual es el nombre: ")
    direccion=input("¿Cual es tu direccion?: ")
    tel=input("¿Cual es tu numero de telefono?: ")

    # sql="insert into clientes (id,nombre,direccion,tel) values (null,'Daniel Contreras','Col. centro','6181234567')"
    sql="insert into clientes (id,nombre,direccion,tel) values (null,%s,%s,%s)"
    valores=(nombre,direccion,tel)
    micursor.execute(sql,valores)

    #Sirve para finalizar la ejecucion del SQL
    conexion.commit()
except: 
    print(f"Ocurrio un problema por favor verifica ...")    
else:
    print(f"Registro Insertardo Exitosamente")