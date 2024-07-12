import mysql.connector

try:
    #Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python'
    )
except Exception as e:
#    print(f"Error: {e}")
   print(f"Tipo de excepción: {type(e).__name__}") 
   print(f"Ocurrio un error con el Servidor ... por favor verifica ...")  
else:         
    #verificar si la conexion fue exitosa
    if conexion.is_connected():
        print(f"Se creo la conexion con la BD exitosamente ...")
    else:
        print(f"No fue posible conectar con la BD ... verifique...")    