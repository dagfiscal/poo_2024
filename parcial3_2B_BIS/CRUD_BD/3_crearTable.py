from conexionBD import *

try:
   micursor=conexion.cursor()

   sql="create table clientes3(id int primary key auto_increment, nombre varchar(60),direccion varchar(120), tel varchar(10))"

   micursor.execute(sql)
except:
   print(f"Ocurrio un problema por favor verifica ...")
else:
   print(f"Se creo la tabla Exitosamente")   
   
      
      