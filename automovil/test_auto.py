from auto import Auto

mi_auto = Auto("Chevrolet", "Doble Cabina", "2011")
print(Auto.mostrar_información(mi_auto))

valor1 = input("Ingrese el kilometraje: \n")
valor2 = input("Ingrese otra vez kilometraje: \n")

Auto.actualizar_kilometraje(valor1)
Auto.realizar_viaje(valor2)
Auto.estado_auto()

auto_new = Auto.auto_news()
print("Auto nuevo------------------", auto_new.__dict__, "---------------")

auto_1 = Auto("Chevrolet", "4x4", "2024")

auto_2 = Auto("Toyota", "Doble Cabina", "2025", 6000)

print(Auto.comparar_kilometraje(auto_1, auto_2))
