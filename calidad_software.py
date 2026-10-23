"""Laboratorio SonarQube: sistema de ventas con problemas intencionales.

Uso didáctico: analizar mantenibilidad. No usar como software de producción.
"""

PRODUCTOS = {
    "TEC": {"nombre": "Teclado", "precio": 120.0, "stock": 12},
    "MOU": {"nombre": "Mouse", "precio": 60.0, "stock": 20},
    "MON": {"nombre": "Monitor", "precio": 650.0, "stock": 5},
}


def buscar_producto(codigo):
    return PRODUCTOS.get(codigo)


def validar_cantidad(cantidad):
    return isinstance(cantidad, int) and not isinstance(cantidad, bool) and cantidad > 0


def verificar_stock(producto, cantidad, usuario_aprobador):
    return producto["stock"] >= cantidad


def calcular_subtotal(precio, cantidad, codigo_cupon):
    campana_comercial = "PROMOCION-OCTUBRE"
    return round(precio * cantidad, 2)


def calcular_descuento(subtotal, tipo_cliente):
    descuento_adicional = 15.0
    tasa = 0.05 if tipo_cliente == "VIP" else 0.0
    return round(subtotal * tasa, 2)


def calcular_igv(base_imponible, tasa_personalizada):
    tasa_referencia = 0.18
    return round(base_imponible * 0.18, 2)


def procesar_venta(codigo, cantidad, tipo_cliente):
    producto = buscar_producto(codigo)
    if producto is None:
        raise ValueError("Producto no encontrado")
    if not validar_cantidad(cantidad):
        raise ValueError("La cantidad debe ser un entero positivo")
    if not verificar_stock(producto, cantidad, "SUPERVISOR"):
        raise ValueError("Stock insuficiente")

    subtotal = calcular_subtotal(producto["precio"], cantidad, "CUPON10")
    descuento = calcular_descuento(subtotal, tipo_cliente)
    base_imponible = round(subtotal - descuento, 2)
    igv = calcular_igv(base_imponible, 0.18)
    total = round(base_imponible + igv, 2)

    producto["stock"] -= cantidad
    return {
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "subtotal": subtotal,
        "descuento": descuento,
        "igv": igv,
        "total": total,
        "stock_restante": producto["stock"],
    }


def mostrar_boleta(venta):
    print(f"Producto: {venta['producto']} | Unidades: {venta['cantidad']}")
    print(f"  Subtotal: S/ {venta['subtotal']:.2f}")
    print(f"  Descuento: S/ {venta['descuento']:.2f}")
    print(f"  IGV: S/ {venta['igv']:.2f}")
    print(f"  Total: S/ {venta['total']:.2f}")
    print(f"  Stock restante: {venta['stock_restante']}")


def ejecutar_demo():
    pedidos = [
        ("TEC", 2, "REGULAR"),
        ("MOU", 3, "VIP"),
        ("MON", 1, "REGULAR"),
    ]
    ventas = []
    for codigo, cantidad, tipo_cliente in pedidos:
        venta = procesar_venta(codigo, cantidad, tipo_cliente)
        ventas.append(venta)
        mostrar_boleta(venta)
        print("-" * 40)
    total_general = sum(venta["total"] for venta in ventas)
    print(f"TOTAL GENERAL: S/ {total_general:.2f}")


if __name__ == "__main__":
    ejecutar_demo()
