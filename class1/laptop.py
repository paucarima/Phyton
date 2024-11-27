import random


class Laptop:
    def __init__(self, marca, procesador, memoria, costo=500, impuesto=10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo+self.impuesto

    def valor_descuento(self, descuento):
        return (self.costo*descuento)/100

    def ralizar_diagnostico_sistema(self):
        resultado = {
            "MARCA": f"{self.marca}",
            "PROCESADOR": f"{self.procesador}",
            "MEMORIA RAM": "OK" if self.memoria >= 8 else "Aumentar memoria RAM",
            "BATERIA": "OK" if random.choice([True, False]) else "Cambiar de bateria"
        }
        return resultado

    @staticmethod
    def comparar_costo(lapto1, lapto2):
        if lapto1.costo == lapto2.costo:
            return "Los costos son iguales"
        return "los costos son diferentes"

    @classmethod
    def asus_laptop(cls, costo):
        marca = "asus"
        procesador = "i5"
        memoria = 16
        return cls(marca, procesador, memoria, costo)
