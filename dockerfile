# Imagen base ligera con Python
FROM python:3.12-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el código de la tienda
COPY Tienda_online/ .

# Al arrancar el contenedor se ejecuta la tienda en consola
CMD ["python", "main.py"]
