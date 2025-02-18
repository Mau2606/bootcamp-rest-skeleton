FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para algunas bibliotecas

# Copiar el archivo de dependencias (si tienes un requirements.txt)
# Si no tienes requirements.txt, puedes agregar la instalación directamente en la siguiente línea

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "app.py" ]
