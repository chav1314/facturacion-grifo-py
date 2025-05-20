ventas_dia = {}

def tipo_documento(doc):
    if len(doc) == 8 and doc.isdigit():
        return "DNI", "Boleta"
    elif len(doc) == 11 and doc.isdigit():
        return "RUC", "Factura"
    else:
        return None, None

def validar_repeticiones(doc):
    return ventas_dia.get(doc, 0) < 3

def validar_galones(galones, comprobante):
    if comprobante == "Boleta":
        return galones <= 100
    elif comprobante == "Factura":
        return galones <= 500
    return False

def registrar_venta(doc, galones, comprobante):
    ventas_dia[doc] = ventas_dia.get(doc, 0) + 1
    print(f"Venta registrada correctamente: {comprobante} por {galones} galones.")

def ejecutar_facturacion():
    while True:
        doc = input("\nIngrese DNI (8 dígitos) o RUC (11 dígitos), o 'salir' para terminar: ")
        if doc.lower() == 'salir':
            break

        tipo_doc, comprobante = tipo_documento(doc)
        if not tipo_doc:
            print("Documento inválido. Debe tener 8 (DNI) u 11 (RUC) dígitos.")
            continue

        if not validar_repeticiones(doc):
            print(" Límite diario alcanzado para este documento.")
            continue

        try:
            galones = float(input(f"Ingrese cantidad de galones para {comprobante}: "))
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")
            continue

        if not validar_galones(galones, comprobante):
            print(f" Límite excedido para {comprobante}. Máximo permitido: {'100' if comprobante == 'Boleta' else '500'} galones.")
            continue

        registrar_venta(doc, galones, comprobante)

if __name__ == "__main__":
    print("-Sistema de Facturación para Grifos-")
    ejecutar_facturacion()
