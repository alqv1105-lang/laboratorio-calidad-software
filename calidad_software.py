def calcular_igv(precio):
    igv = precio * 0.18
    return precio + igv


def verificar_cliente(cliente):
    if cliente is None:
        print("Cliente no encontrado")
    else:
        print("Cliente registrado")


def calcular_total_venta(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


print(calcular_total_venta(100, 3))
