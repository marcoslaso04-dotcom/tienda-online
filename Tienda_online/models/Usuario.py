"""Clases de los usuarios de la tienda."""

import uuid


class Usuario:
    """Clase padre de cualquier persona que use la tienda."""

    def __init__(self, nombre: str, email: str):
        self.id: str = str(uuid.uuid4())
        self.nombre: str = nombre
        self.email: str = email

    def is_admin(self) -> bool:
        """Por defecto un usuario no es administrador."""
        return False

    def __str__(self) -> str:
        return f"[{self.id[:8]}] {self.nombre} ({self.email})"


class Cliente(Usuario):
    """Usuario que compra en la tienda, tiene direccion de envio."""

    def __init__(self, nombre: str, email: str, direccion: str):
        super().__init__(nombre, email)
        self.direccion: str = direccion

    def __str__(self) -> str:
        return f"[{self.id[:8]}] Cliente {self.nombre} ({self.email}) - {self.direccion}"


class Administrador(Usuario):
    """Usuario que gestiona la tienda."""

    def is_admin(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"[{self.id[:8]}] Admin {self.nombre} ({self.email})"
