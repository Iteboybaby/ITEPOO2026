# 🎓 Sistema de Registro de Estudiantes (POO en Python)

Este es un proyecto sencillo y educativo escrito en Python que demuestra los fundamentos de la Programación Orientada a Objetos (POO). 

El script define una clase `Estudiante` que permite instanciar objetos con datos personales, registrar sus calificaciones y calcular promedios de forma dinámica.

## 🚀 Características

* **Creación de perfiles:** Inicializa estudiantes con nombre, edad y carrera.
* **Registro de calificaciones:** Permite añadir múltiples calificaciones a una lista interna del objeto.
* **Cálculo de promedios:** Evalúa la lista de calificaciones y devuelve el promedio exacto, incluyendo validaciones para evitar errores matemáticos (división por cero).
* **Formateo de información:** Utiliza métodos mágicos de Python (`__str__`) para devolver una presentación legible de los datos del estudiante.

## 🧠 Conceptos de Programación Aplicados

Este código sirve como un excelente ejemplo práctico de:
* **Clases y Objetos:** Estructuración de datos y comportamientos.
* **Constructores (`__init__`):** Inicialización de atributos de instancia.
* **Métodos de Instancia:** Funciones que operan sobre los datos específicos de cada objeto (`self`).
* **Manejo de Listas:** Almacenamiento y manipulación de datos dinámicos.
* **F-Strings:** Formateo moderno y eficiente de cadenas de texto en Python.

## 💻 Uso e Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
   ```
2. Asegúrate de tener Python 3.x instalado.
3. Ejecuta el archivo principal desde tu terminal:
   ```bash
   python main.py
   ```

## 📋 Ejemplo de Código

```python
estudiante1 = Estudiante("Pako", 30, "Ing. en Sistemas")

# Agregar calificaciones
estudiante1.agregar_calificacion(75)
estudiante1.agregar_calificacion(90)

# Mostrar resultados
print(estudiante1) # Salida: Hola, soy Pako, tengo 30 años y estudio Ing. en Sistemas
print(f"El promedio es: {estudiante1.calcular_promedio()}") # Salida: El promedio es: 82.5
```
