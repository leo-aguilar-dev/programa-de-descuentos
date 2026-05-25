PRODUCTOS = [
    {
        "nombre": "Lasaña",
        "categoria": "Pastas",
        "precio": 20000,
    },
    {
        "nombre": "Pizza",
        "categoria": "Pastas",
        "precio": 15000,
    },
    {
        "nombre": "Espagueti",
        "categoria": "Pastas",
        "precio": 17000,
    },
    {
        "nombre": "Sobrebarriga",
        "categoria": "Carnes",
        "precio": 18000,
    },
    {
        "nombre": "Mute",
        "categoria": "Sopas",
        "precio": 15000,
    },
    {
        "nombre": "Sancocho",
        "categoria": "Sopas",
        "precio": 12000,
    }
]

def mostrar_productos():
    '''Muestra la lista de productos disponibles al usuario.'''
    print("Productos disponibles:")
    for producto in PRODUCTOS:
        print("----------------------")
        print(f"Nombre: {producto['nombre']}\n" +
              f"Categoría: {producto['categoria']}\n" +
              f"Precio base: ${producto['precio']:,.0f}")

def escoger_categoria():
    '''Permite al usuario seleccionar una categoría válida de los productos disponibles.'''
    while True:
        categoria = input("Ingrese la categoria objetivo: ").strip()

        for producto in PRODUCTOS:
            if producto['categoria'].lower() == categoria.lower():
                return categoria
            
        print("Categoría no encontrada. Por favor, intente de nuevo.")

def definir_umbral():
    '''Permite al usuario definir un umbral válido para aplicar el descuento.'''
    while True:
        try:
            umbral = int(input("Ingrese el umbral: "))
            if(umbral < 0):
                print("El valor no puede ser inferior a cero. Por favor, intente nuevamente.")
                continue

            return umbral
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def validar_descuento(categoria_objetivo, umbral):
    '''Valida que productos cumplen con los criterios para aplicar un descuento.'''
    descuento = 0.15

    productos_mas_descuento = []

    for producto in PRODUCTOS:
        if (producto['categoria']).lower() == categoria_objetivo.lower() and producto['precio'] > umbral:
            cantidad_descuento = producto['precio'] * descuento
            productos_mas_descuento.append({**producto, 'descuento': cantidad_descuento})
        else:
            productos_mas_descuento.append({**producto, 'descuento': 0})

    return productos_mas_descuento

def calcular_precio_total(producto):
    '''Calcula el precio total de un producto después de aplicar el descuento.'''
    return producto['precio'] - producto['descuento']

def main():
    print("Bienvenido.")

    mostrar_productos()
    categoria_objetivo = escoger_categoria()
    umbral = definir_umbral()
    productos_actualizados = validar_descuento(categoria_objetivo, umbral)

    print("----------------------")
    print("Productos actualizados:")
    for producto in productos_actualizados:
        print("----------------------")
        print(f"Nombre: {producto['nombre']}\n" +
              f"Categoría: {producto['categoria']}\n" +
              f"Precio base: ${producto['precio']:,.0f}\n" +
              f"Descuento aplicado: ${int(producto['descuento']):,.0f}\n" +
              f"Precio total: ${int(calcular_precio_total(producto)):,.0f}")

main()