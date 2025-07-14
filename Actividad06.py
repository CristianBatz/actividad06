productos ={}
opcion = 0

while opcion != 5:
    print("=== Inventario ===")
    print("1. Registrar producto")
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
        stock = int(input("Ingrese el stock del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        productos[codigo] = {
            "nombre": nombre,
            "categoria": categoria,
            "talla": talla,
            "stock": stock,
            "precio": precio
        }

    elif opcion == 2:
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

    elif opcion == 3:
        total= 0
        print("=== Valor total del inventario ===")
        for datos in productos.values():
            total += datos['stock'] * datos['precio']
            print(f"Valor total del inventario es de: {total}")

    elif opcion == 4:
        print("=== Cantidad de productos ===")
        print(f"Cantidad total de productos: {len(productos)}")

