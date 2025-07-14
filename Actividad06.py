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
        cantidad = int(input("¿Cuantos productos desea ingresar?: "))
        for i in range(cantidad):
            print(f"producto #{i+1}")
            codigo = input("Ingrese el codigo del producto: ")
            while codigo in productos:
                print("ya hay un producto con ese codigo, vuelva a intentarlo")
                codigo = input("Ingrese el codigo del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoria del producto: ")
            talla = input("Ingrese la talla del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            while precio <=0:
                print("El precio debe ser mayor a 0")
                precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
            while stock <=0:
                print("El stock debe ser mayor a 0")
                stock = int(input("Ingrese el stock del producto: "))
            productos[codigo] = {
                "nombre": nombre,
                "categoria": categoria,
                "talla": talla,
                "precio": precio,
                "stock": stock,
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
            print("-----------------------------")
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
        print("=== cantidad por categoria ===")
        categorias = {}
        for datos in productos.values():
            categoriaA = datos['categoria']
            if categoriaA not in categorias:
                categorias[categoriaA] = 0
            categorias[categoriaA] += 1
        for categoriaA, cantidad in categorias.items():
            print(f"{categoriaA}: {cantidad}")
    elif opcion == 5:
        print("=== Salir ===")
        print("saliendo del programa")
