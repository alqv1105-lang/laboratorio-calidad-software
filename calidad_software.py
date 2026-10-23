
def calcular_descuento(precio, descuento):
    resultado = precio - (precio * descuento / 100)
    return resultado

def procesar_venta(precio, descuento):
    if precio > 0:
        if descuento >= 0:
            if descuento <= 100:
                total = calcular_descuento(precio, descuento)
                print("Total:", total)
            else:
                print("Descuento incorrecto")
        else:
            print("Descuento incorrecto")
    else:
        print("Precio incorrecto")


def calcular_precio_final(precio, descuento):
    total = precio - (precio * descuento / 100)
    return total


procesar_venta(100, 20)


def calcular_igv(precio, impuesto):
    igv = precio * 0.18
    return precio + igv


def verificar_cliente(cliente):
    if cliente == None:
        print("Cliente no encontrado")
    else:
        print("Cliente registrado")


def calcular_total_venta(precio, cantidad):
    subtotal = precio * cantidad
    descuento_especial = 50
    return subtotal


print(calcular_total_venta(100, 3))

