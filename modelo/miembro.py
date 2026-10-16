# aqui definimos la clase Miembro y sus subclases MiembroBasico y MiembroPremium
class Miembro:
    def __init__(self, codigo, nombre, apellido, edad, meses, activo, plan):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__meses = meses
        self.__activo = activo
        self.__plan = plan
        
#creamos los getters paraobetner los valores de los atributos privados    
    def get_codigo(self):
        return self.__codigo
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_edad(self):
        return self.__edad
    def get_meses(self):
        return self.__meses
    def get_activo(self):
        return self.__activo
    def get_plan(self):
        return self.__plan
    
    def set_activo(self, activo):
        self.__activo = activo
    

class MiembroBasico(Miembro):
    def __init__(self, codigo, nombre, apellido, edad, meses, activo, plan):
        super().__init__(codigo, nombre, apellido, edad, meses, activo, plan)
    
    def calcular_pago(self):
        return self.get_meses() * 80000
    
class MiembroPremium(Miembro):
    def __init__(self, codigo, nombre, apellido, edad, meses, activo, plan):
        super().__init__(codigo, nombre, apellido, edad, meses, activo, plan)
        
    def calcular_pago(self):
        return self.get_meses() * 120000
