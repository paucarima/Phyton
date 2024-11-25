class Auto:
    def __init__(self, marca, modelo, anio, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje

    @staticmethod
    def mostrar_información(auto):
        return auto.__dict__

    @classmethod
    def actualizar_kilometraje(cls, valor):
        if float(valor) <= 0:
            print("No se puede reducir el kilometraje:")
        else:
            cls.kilometraje = valor
            print(f"Tu kilometraje inicial: {cls.kilometraje}")
            return cls.kilometraje

    @classmethod
    def realizar_viaje(cls, valor):
        if float(valor) <= 0:
            print("la cantidad de kilómetros debe ser positiva:")
        else:
            cls.kilometraje = float(cls.kilometraje)+float(valor)
            print(f"Tu kilometraje en viaje: {cls.kilometraje}")
            return cls.kilometraje

    @classmethod
    def estado_auto(cls):
        if (cls.kilometraje < 20000):
            print("Estoy como nuevo")
        elif (cls.kilometraje >= 20000 and cls.kilometraje <= 100000):
            print("Ya estoy usado")
        elif (cls.kilometraje > 100000):
            print("¡Ya déjame descansar por favor!")

    @classmethod
    def auto_news(cls):
        anio = "2024"
        marca = "Toyota"
        modelo = "4x4"
        kilometraje = 0
        return cls(marca, modelo, anio, kilometraje)

    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "Los kilometros son iguales"
        return "Los kilometros son diferentes"
