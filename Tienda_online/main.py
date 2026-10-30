"""Punto de entrada del programa. Sirve para probar la tienda por consola.

Practica 1.3 - Marcos Laso Garcia
"""

from Services.Tienda_service import TiendaService


def main():
    # creamos la tienda
    tienda = TiendaService()

    # ---- 1. REGISTRAMOS LOS USUARIOS ----
    print("===== REGISTRO DE USUARIOS =====")
    hermindo = tienda.registrar_usuario("cliente", "Hermindo Ozores", "hermindo@mail.com", "Calle Mayor 1, Madrid")
    agustin = tienda.registrar_usuario("cliente", "Agustin Carril", "agustin@mail.com", "Av. del Sol 22, Vigo")
    alex = tienda.registrar_usuario("cliente", "Alex Padilla", "alex@mail.com", "Plaza Nueva 5, Sevilla")
    admin = tienda.registrar_usuario("admin", "Marcos Laso", "marcos@tienda.com")

    for usuario in tienda.usuarios:
        print(usuario, "- es admin:", usuario.is_admin())

    # ---- 2. CREAMOS LOS PRODUCTOS ----
    print("\n===== ANADIENDO PRODUCTOS =====")
    portatil = tienda.anadir_producto_electronico("Portatil Lenovo IdeaPad Pro", 750.0, 5, 24)
    movil = tienda.anadir_producto_electronico("Movil Samsung", 400.0, 10, 12)
    auriculares = tienda.anadir_producto_electronico("Auriculares Sony", 120.0, 8, 6)
    camiseta = tienda.anadir_producto_ropa("Camiseta basica", 15.0, 20, "M", "Negro")
    sudadera = tienda.anadir_producto_ropa("Sudadera con capucha", 35.0, 12, "L", "Gris")
    print("Se han anadido 5 productos al inventario")

    # ---- 3. LISTAMOS EL INVENTARIO ----
    print()
    tienda.listar_productos()

    # ---- 4. SIMULAMOS CUATRO PEDIDOS ----
    print("\n===== PEDIDOS =====")

    pedido1 = tienda.realizar_pedido(hermindo.id, [(portatil.id, 1), (camiseta.id, 2)])
    print(pedido1)

    print()
    pedido2 = tienda.realizar_pedido(agustin.id, [(movil.id, 2), (auriculares.id, 1)])
    print(pedido2)

    print()
    pedido3 = tienda.realizar_pedido(hermindo.id, [(sudadera.id, 3)])
    print(pedido3)

    print()
    pedido4 = tienda.realizar_pedido(alex.id, [(auriculares.id, 2), (camiseta.id, 1)])
    print(pedido4)

    # probamos que pasa si se pide mas stock del que hay
    print("\n===== PEDIDO QUE FALLA (no hay stock) =====")
    pedido_malo = tienda.realizar_pedido(alex.id, [(portatil.id, 100)])
    print("Resultado:", pedido_malo)

    # ---- 5. HISTORICO DE PEDIDOS DE UN CLIENTE ----
    print("\n===== HISTORICO DE PEDIDOS DE HERMINDO =====")
    for pedido in tienda.listar_pedidos_usuario(hermindo.id):
        print(pedido)
        print()

    # ---- 6. STOCK ACTUALIZADO ----
    print("===== STOCK DESPUES DE LOS PEDIDOS =====")
    tienda.listar_productos()

    # ---- 7. ELIMINAMOS UN PRODUCTO ----
    print("\n===== ELIMINAMOS LA CAMISETA =====")
    print("Eliminado:", tienda.eliminar_producto(camiseta.id))
    tienda.listar_productos()


if __name__ == "__main__":
    main()
