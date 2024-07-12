class Personas:
    def __init__(self,nombre,edad,tel):
        self.nombre=nombre
        self.edad=edad
        self.tel=tel

    def info_persona(self):
        print(f"Informacion de la persona: {self.getNombre(), self.getEdad(), self.getTel()}")

    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad   
    def getTel(self):
        return self.tel
    def setNombre(self,nombre):
        self.nombre=nombre
    def setEdad(self,edad):
        self.edad=edad  
    def setTel(self,tel):
        self.tel=tel

class Estudiantes(Personas):
   def __init__(self,nombre,edad,tel,carrera,matricula):
      super().__init__(nombre,edad,tel)
      self.__carrera=carrera
      self.__matricula=matricula

   def info_persona(self):
        print(f"Informacion de la persona Estudiante: {self.getNombre(), self.getEdad(), self.getTel(), self.getCarrera(), self.getMatricula()}")

   def getCarrera(self):
        return self.__carrera
   def getMatricula(self):
        return self.__matricula   
    
   def setCarrera(self,carrera):
        self.__carrera=carrera
   def setMatricula(self,matricula):
        self.__matricula=matricula  

class Docentes(Personas):
   def __init__(self,nombre,edad,tel,modalidad,num_empleado):
      super().__init__(nombre,edad,tel)
      self._modalidad=modalidad
      self._num_empleado=num_empleado

   def info_persona(self):
        print(f"Informacion de la persona Docente: {self.getNombre(), self.getEdad(), self.getTel(), self.getModalidad(), self.getNum_empleado()}")

   def getModalidad(self):
        return self._modalidad
   def getNum_empleado(self):
        return self._num_empleado  
    
   def setModalidad(self,modalidad):
        self._modalidad=modalidad
   def setNum_empleado(self,num_empleado):
        self._num_empleado=num_empleado  








