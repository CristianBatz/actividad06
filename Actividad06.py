productos ={}
opcion = 0

while opcion != 5:
    print("=== Inventario ===")
    print("1. Registra producto")
    print("2. Buscar producto")
    print("3. Valor total del inventario")
    print("4. Cantidad de productos")
    print("5. Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        print("=== Productos ===")
        codigo = input("Ingrese el codigo del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoria del producto: ")
        talla = input("Ingrese la talla del producto: ")
        stock = input("Ingrese el stock del producto: ")
        precio = input("Ingrese el precio del producto: ")
        productos[codigo] = {
            "nombre": nombre,
            "categoria": categoria,
            "talla": talla,
            "stock": stock,
            "precio": precio
        }
    if opcion == 2:
        print("=== Buscar productos ===")
        buscando = input("Ingrese el codigo del producto: ")
        if buscando in productos:
            print(f"nombre: {productos[buscando]['nombre']}")
            print(f"categoria: {productos[buscando]['categoria']}")
            print(f"talla: {productos[buscando]['talla']}")
            print(f"stock: {productos[buscando]['stock']}")
            print(f"precio: {productos[buscando]['precio']}")
        else:
            print("No se encontro el producto")
