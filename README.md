# Tienda Online

**Autor:** Marcos Laso García

## Descripción

Aplicación en Python que modela una tienda online sencilla con programación orientada a objetos. Gestiona:

- **Productos:** genéricos, electrónicos (con meses de garantía) y de ropa (con talla y color), con control de stock.
- **Usuarios:** clientes (con dirección postal) y administradores.
- **Pedidos:** asociados a un cliente, con varias líneas de producto y cálculo del total.

La lógica de negocio está centralizada en la clase `TiendaService`, que registra usuarios, gestiona el inventario y crea pedidos comprobando que el cliente existe y que hay stock suficiente.

La primera versión se ejecuta en consola. El proyecto evolucionará en las siguientes prácticas (API REST con FastAPI y despliegue con Docker).

## Estructura

```text
Tienda_online/
├── models/
│   ├── __init__.py
│   ├── Producto.py
│   ├── Usuario.py
│   └── Pedido.py
├── Services/
│   ├── __init__.py
│   └── Tienda_service.py
└── main.py
```

## Ejecución

Requiere Python 3.10 o superior. No usa librerías externas.

```bash
cd Tienda_online
python main.py
```

`main.py` registra varios clientes y un administrador, añade productos de distintas categorías, simula pedidos y muestra el histórico de un cliente y el stock actualizado.

## Flujo de trabajo con Git

- `main`: rama principal con el código estable.
- `feature/<nombre>`: una rama por funcionalidad, que se integra en `main` mediante Pull Request.
