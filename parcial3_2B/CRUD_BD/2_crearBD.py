import mysql.connector

try:
    #Crear la conexion con la BD 
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
    )

except:
    print(f"Ocurrio un problema con el servidor ... por favor intentalo más tarde...")
else:
     #Verificar la conexion
    if conexion.is_connected():
        print("Se crear la conexion con exito")
    else:
        print("No fue posible conectarse")

    #Crear otro objeto para ejecutar las instrucciones
    micursor=conexion.cursor()

    #Crear la BD desde Python
    sql="create database bd_python"
    micursor.execute(sql)

    #verificar que se se creo la BD
    if micursor:
        print("Se creo la BD exitosamente")

    #Mostrar las BD que existen en mi servidor de MySQL
    micursor.execute("show databases")

    for x in micursor:
        print(x)




