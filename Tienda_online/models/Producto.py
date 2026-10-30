"""Clases de los productos de la tienda."""

import uuid


class Producto:
    """Clase padre de todos los productos de la tienda."""

    def __init__(self, nombre: str, precio: float, stock: int):
        # el id se genera solo al crear el producto
        self.id: str = str(uuid.uuid4())
        self.nombre: str = nombre
        self.precio: float = precio
        self.stock: int = stock

    def hay_stock(self, cantidad: int) -> bool:
        """Devuelve True si hay stock suficiente para la cantidad pedida."""
        return self.stock >= cantidad

    def actualizar_stock(self, cantidad: int) -> None:
        """Suma o resta unidades al stock (positivo repone, negativo vende)."""
        self.stock = self.stock + cantidad

    def __str__(self) -> str:
        return f"[{self.id[:8]}] {self.nombre} - {self.precio}EUR - stock: {self.stock}"


class ProductoElectronico(Producto):
    """Producto electronico, tiene meses de garantia."""

    def __init__(self, nombre: str, precio: float, stock: int, garantia_meses: int):
        super().__init__(nombre, precio, stock)
        self.garantia_meses: int = garantia_meses

    def __str__(self) -> str:
        return (f"[{self.id[:8]}] {self.nombre} - {self.precio}EUR - stock: {self.stock}"
                f" - garantia: {self.garantia_meses} meses")


class ProductoRopa(Producto):
    """Producto de ropa, tiene talla y color."""

    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str):
        super().__init__(nombre, precio, stock)
        self.talla: str = talla
        self.color: str = color

    def __str__(self) -> str:
        return (f"[{self.id[:8]}] {self.nombre} - {self.precio}EUR - stock: {self.stock}"
                f" - talla: {self.talla} - color: {self.color}")
