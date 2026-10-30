"""Capa de servicios: aqui se gestionan las operaciones de la tienda."""

from typing import List, Optional, Tuple

from models.Pedido import Pedido
from models.Producto import Producto, ProductoElectronico, ProductoRopa
from models.Usuario import Usuario, Cliente, Administrador


class TiendaService:
    """Guarda los usuarios, los productos y los pedidos de la tienda."""

    def __init__(self):
        self.usuarios: List[Usuario] = []
        self.productos: List[Producto] = []
        self.pedidos: List[Pedido] = []

    # ---------- USUARIOS ----------

    def registrar_usuario(self, tipo: str, nombre: str, email: str,
                          direccion: str = "") -> Usuario:
        """Crea un cliente o un administrador y lo guarda en la tienda."""
        if tipo == "cliente":
            usuario = Cliente(nombre, email, direccion)
        elif tipo == "admin":
            usuario = Administrador(nombre, email)
        else:
            raise ValueError("El tipo tiene que ser 'cliente' o 'admin'")

        self.usuarios.append(usuario)
        return usuario

    def buscar_usuario(self, usuario_id: str) -> Optional[Usuario]:
        """Devuelve el usuario con ese id, o None si no existe."""
        for usuario in self.usuarios:
            if usuario.id == usuario_id:
                return usuario
        return None

    # ---------- PRODUCTOS ----------

    def anadir_producto_electronico(self, nombre: str, precio: float, stock: int,
                                    garantia_meses: int) -> ProductoElectronico:
        """Crea un producto electronico y lo mete en el inventario."""
        producto = ProductoElectronico(nombre, precio, stock, garantia_meses)
        self.productos.append(producto)
        return producto

    def anadir_producto_ropa(self, nombre: str, precio: float, stock: int,
                             talla: str, color: str) -> ProductoRopa:
        """Crea un producto de ropa y lo mete en el inventario."""
        producto = ProductoRopa(nombre, precio, stock, talla, color)
        self.productos.append(producto)
        return producto

    def buscar_producto(self, producto_id: str) -> Optional[Producto]:
        """Devuelve el producto con ese id, o None si no existe."""
        for producto in self.productos:
            if producto.id == producto_id:
                return producto
        return None

    def eliminar_producto(self, producto_id: str) -> bool:
        """Borra un producto por su id. Devuelve True si lo ha borrado."""
        producto = self.buscar_producto(producto_id)
        if producto is None:
            return False
        self.productos.remove(producto)
        return True

    def listar_productos(self) -> None:
        """Imprime por consola todos los productos de la tienda."""
        print("---- PRODUCTOS DE LA TIENDA ----")
        if len(self.productos) == 0:
            print("No hay productos en el inventario")
        for producto in self.productos:
            print(producto)

    # ---------- PEDIDOS ----------

    def realizar_pedido(self, usuario_id: str,
                        productos_pedidos: List[Tuple[str, int]]) -> Optional[Pedido]:
        """Crea un pedido si el usuario existe y hay stock de todo.

        productos_pedidos es una lista de tuplas (id_producto, cantidad).
        Si algo falla devuelve None.
        """
        usuario = self.buscar_usuario(usuario_id)
        if usuario is None:
            print("ERROR: el usuario no existe")
            return None

        if not isinstance(usuario, Cliente):
            print("ERROR: solo los clientes pueden hacer pedidos")
            return None

        # primero comprobamos que hay stock de todos los productos
        lineas: List[Tuple[Producto, int]] = []
        for producto_id, cantidad in productos_pedidos:
            producto = self.buscar_producto(producto_id)
            if producto is None:
                print("ERROR: hay un producto que no existe")
                return None
            if not producto.hay_stock(cantidad):
                print(f"ERROR: no hay stock suficiente de {producto.nombre}")
                return None
            lineas.append((producto, cantidad))

        # si todo esta bien, creamos el pedido y descontamos el stock
        pedido = Pedido(usuario, lineas)
        for producto, cantidad in lineas:
            producto.actualizar_stock(-cantidad)

        self.pedidos.append(pedido)
        return pedido

    def listar_pedidos_usuario(self, usuario_id: str) -> List[Pedido]:
        """Devuelve los pedidos de un usuario ordenados por fecha."""
        pedidos_usuario = []
        for pedido in self.pedidos:
            if pedido.cliente.id == usuario_id:
                pedidos_usuario.append(pedido)

        pedidos_usuario.sort(key=lambda pedido: pedido.fecha)
        return pedidos_usuario
