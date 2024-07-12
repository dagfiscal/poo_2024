import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
except:
    print(f"Ocurrio un error con el Sistema por favor verifique ...")
else:
   #Crear un objeto de tipo cursor que permita ejecutar instrucciones SQL
    micursor=conexion.cursor()

    sql="create database bd_python"
    #Ejecutar la consulta SQL
    micursor.execute(sql)

    if micursor:
        print(f"Se creo la BD exitosamente")

    #Mostrar las BD que existen en el SGBD MySQL
    micursor.execute("show databases")

    for x in micursor:
        print(x)

