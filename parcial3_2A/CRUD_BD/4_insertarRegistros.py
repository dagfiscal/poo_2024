
from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Juan Polainas', 'Col. del valle', '6181234567')"

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el SQL con exito
    conexion.commit()

except:
    print(f"Ocurrio un error por favor vuelva a intentar ... mas tarde ...")    
else:
    print("Registro Insertado con Exito")

