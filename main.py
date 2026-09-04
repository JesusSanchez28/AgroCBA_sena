import json

try:
    with open("producto.json", "r", encoding="utf-8") as archivo:
        productos = json.load(archivo)
except (FileNotFoundError, json.JSONDecodeError):
    productos = []


def menu():
    print("=====================================")
    print("          SISTEMA AGROCBA            ")
    print("=====================================")
    print("Sistema iniciado correctamente")


def menuPp():
    print("=============================================")
    print("                SISTEMA AGROCBA              ")
    print("=============================================")
    print("=     1. Registrar producto                 =")
    print("=     2. Consultar productos                =")
    print("=     3. Buscar producto                    =")
    print("=     4. Actualizar producto                =")
    print("=     5. Eliminar producto                  =")
    print("=     6. Mostrar valor total del inventario =")
    print("=     7. Salir                              =")
    print("=============================================")


def registrar_producto():

    while True:
        codigo = input("Escriba el codigo del producto: ").strip()

        if codigo == "":
            print("El codigo no puede estar vacio.")
            continue

        repetido = False

        for producto in productos:
            if producto["codigo"] == codigo:
                repetido = True
                break

        if repetido:
            print("Ya se ha registrado un producto con este codigo.")
        else:
            break

    while True:
        nombre = input("Escriba el nombre: ").strip()

        if nombre != "":
            break

        print("El nombre no puede estar vacio.")

    while True:
        categoria = input("Escriba la categoria: ").strip()

        if categoria != "":
            break

        print("La categoria no puede estar vacia.")

    while True:
        try:
            cantidad = int(input("Escriba la cantidad: "))

            if cantidad >= 0:
                break

            print("La cantidad debe ser mayor o igual a cero.")

        except ValueError:
            print("La cantidad debe ser un numero entero.")

    while True:
        try:
            precio = float(input("Escriba el precio: "))

            if precio > 0:
                break

            print("El precio debe ser mayor que cero.")

        except ValueError:
            print("El precio debe ser numerico.")

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio
    }

    productos.append(nuevo_producto)

    with open("producto.json", "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)

    print("Producto registrado correctamente.")


def consultar_producto():

    print("=============================================")
    print("               CONSULTAR PRODUCTOS           ")
    print("=============================================")

    if not productos:
        print("No hay productos registrados en este momento.")
        return

    for prod in productos:
        print("=============================================")
        print(f"Codigo: {prod['codigo']}")
        print(f"Nombre: {prod['nombre']}")
        print(f"Categoria: {prod['categoria']}")
        print(f"Cantidad: {prod['cantidad']}")
        print(f"Precio: ${prod['precio']}")
        print("=============================================")


def buscar_producto():

    print("=============================================")
    print("               BUSCAR PRODUCTO               ")
    print("=============================================")

    busqueda = input("Ingrese el codigo que desea buscar: ").strip()

    encontrado = False

    for producto in productos:

        if producto["codigo"] == busqueda:

            print(f"Codigo: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoria: {producto['categoria']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: ${producto['precio']}")

            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")


def actualizar_producto():

    busqueda = input("Ingrese el codigo del producto que desea actualizar: ").strip()

    encontrado = False

    for producto in productos:

        if producto["codigo"] == busqueda:

            print("Producto encontrado.")

            while True:
                nombre = input("Escriba el nuevo nombre: ").strip()

                if nombre != "":
                    break

                print("El nombre no puede estar vacio.")

            while True:
                categoria = input("Escriba la nueva categoria: ").strip()

                if categoria != "":
                    break

                print("La categoria no puede estar vacia.")

            while True:
                try:
                    cantidad = int(input("Escriba la nueva cantidad: "))

                    if cantidad >= 0:
                        break

                    print("La cantidad debe ser mayor o igual a cero.")

                except ValueError:
                    print("Debe ingresar un numero entero.")

            while True:
                try:
                    precio = float(input("Escriba el nuevo precio: "))

                    if precio > 0:
                        break

                    print("El precio debe ser mayor que cero.")

                except ValueError:
                    print("El precio debe ser numerico.")

            producto["nombre"] = nombre
            producto["categoria"] = categoria
            producto["cantidad"] = cantidad
            producto["precio"] = precio

            with open("producto.json", "w", encoding="utf-8") as archivo:
                json.dump(productos, archivo, ensure_ascii=False, indent=4)

            print("Producto actualizado correctamente.")

            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")


def eliminar_producto():

    busqueda = input("Ingrese el codigo del producto que desea eliminar: ").strip()

    encontrado = False

    for producto in productos:

        if producto["codigo"] == busqueda:

            print(f"Producto encontrado: {producto['nombre']}")

            confirmacion = input("¿Desea eliminarlo? si / no: ").strip().lower()

            if confirmacion == "si":

                productos.remove(producto)

                with open("producto.json", "w", encoding="utf-8") as archivo:
                    json.dump(productos, archivo, ensure_ascii=False, indent=4)

                print("Producto eliminado correctamente.")

            else:
                print("Eliminacion cancelada.")

            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")


def mostrar_valor_total():

    if not productos:
        print("No hay productos registrados.")
        return

    total = 0

    for producto in productos:
        subtotal = producto["cantidad"] * producto["precio"]
        total = total - subtotal

    print(f"El valor total del inventario es de: ${total}")


def todo():

    control = True

    menu()

    input("Presione ENTER para continuar...")

    while control:

        menuPp()

        try:
            op = int(input("Seleccione una opcion: "))

            match op:

                case 1:
                    registrar_producto()

                case 2:
                    consultar_producto()

                case 3:
                    buscar_producto()

                case 4:
                    actualizar_producto()

                case 5:
                    eliminar_producto()

                case 6:
                    mostrar_valor_total()

                case 7:
                    print("Has salido del programa.")
                    control = False

                case _:
                    print("Opcion invalida. Seleccione una opcion del 1 al 7.")

        except ValueError:
            print("Debe ingresar un numero.")


todo()