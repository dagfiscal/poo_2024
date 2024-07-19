

from conexionBD import *
import hashlib
import datetime
import funciones


class Usuario:
    def __init__(self, nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos=apellidos
        self.email=email
        #self.contrasena = self.hash_password(password)
        self.contrasena=password
    
    #Funcion para encriptar la contraseña
    def hash_password(self,contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()
   
    def registrar(self):
        try:
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into usuarios values (null,%s,%s,%s,%s,%s)",
                (self.nombre,self.apellidos,self.email,self.contrasena,fecha)
            )
            conexion.commit()
            return True
        except:
            return False    

    
    def iniciar_sesion(self):
        contrasena=hashlib.sha256(self.contrasena.encode()).hexdigest()
        try:
           cursor.execute(
             "select * from usuarios where email=%s and password=%s",
             (self.email,contrasena)
           )
        #    print(f"email: {self.email}")
        #    print(f"contraseña: {contrasena}")
           usuario=cursor.fetchone()
        #    print(f"Valor del registro: {usuario}")
        #    funciones.esperarTecla()
           if usuario:
               return usuario
           else:
               return []    
        except:  
            # print(f"Entre a la excepcion")
            # funciones.esperarTecla()  
            return []  
        
    # @staticmethod
    # def iniciar_sesion(email,contrasena):
    #     contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
    #     try:
    #        cursor.execute(
    #          "select * from usuarios where email=%s and password=%s",
    #          (email,contrasena)
    #        )
    #        usuario=cursor.fetchone()
    #        if usuario:
    #            return usuario
    #        else:
    #            return []    
    #     except:    
    #         return []  
