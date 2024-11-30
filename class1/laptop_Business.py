from laptop import Laptop
import random


class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento,
                 duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duración_bateria = duracion_bateria

    def __str__(self):
        return f"Marca: {self.marca}\n Procesador: {self.procesador} \n Memoria: {self.memoria} \n Costo:{self.costo}\n Impuesto: {self.impuesto}\n Almanecamiento: {self.almacenamiento}\n Duración de Batería: {self.duración_bateria}\n"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().ralizar_diagnostico_sistema()
        verificar_red = self.verificar_conectividad_red()
        resultado_diagnostico["Verificando conectividad"] = verificar_red
        return resultado_diagnostico

    def verificar_conectividad_red(self):
        resultado = {
            "Disponibilidad de Wi-Fi": "OK" if random.choice([True, False]) else "No conexión al wifi",
            "Acceso a servidores empresariales": "Acceso Aceptado" if random.choice([True, False]) else "Acceso denegado",
            "Latencia de la red": "OK" if random.choice([True, False]) else "Red caída"
        }
        return resultado


pass
