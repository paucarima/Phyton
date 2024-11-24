class Auto:
    def __init__(self, marca, modelo, anio, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje

    def mostrar_información(self):

        print(f"Marca: {self.marca} ,Modelo: {self.modelo} , Anio: {
              self.anio} ,Kilometraje: {self.kilometraje}")

    def actualizar_kilometraje(self, valor):
        if float(valor) <= 0:
            print("No se puede reducir el kilometraje:")
        else:
            self.kilometraje = valor
            print(f"Tu kilometraje es: {self.kilometraje}")
            return self.kilometraje

    def realizar_viaje(self, valor):
        if float(valor) <= 0:
            print("la cantidad de kilómetros debe ser positiva:")
        else:
            self.kilometraje = float(self.kilometraje)+float(valor)
            print(f"Tu kilometraje es: {self.kilometraje}")
            return self.kilometraje

    def estado_auto(self):
        if (self.kilometraje < 20000):
            print("Estoy como nuevo")
        elif (self.kilometraje >= 20000 and self.kilometraje <= 100000):
            print("Ya estoy usado")
        elif (self.kilometraje > 100000):
            print("¡Ya déjame descansar por favor!")


mi_auto = Auto("Chevrolet", "Doble Cabina 4x4", "2011")
mi_auto.mostrar_información()
valor1 = input("Ingrese el kilometraje: \n")
valor2 = input("Ingrese otra vez kilometraje: \n")
mi_auto.actualizar_kilometraje(valor1)
mi_auto.realizar_viaje(valor2)
mi_auto.estado_auto()
