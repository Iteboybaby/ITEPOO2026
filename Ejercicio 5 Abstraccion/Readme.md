# 🧩 Abstracción en Python (Clases y Métodos Abstractos)

Este repositorio contiene un ejemplo claro y conciso de cómo implementar la **Abstracción** en Python utilizando el módulo `abc` (Abstract Base Classes). 

El código demuestra cómo crear una clase plantilla o "contrato" (`Animal`) que no puede ser instanciada directamente, sino que obliga a sus subclases
(`Perro` y `Gato`) a implementar comportamientos específicos, garantizando una estructura uniforme en todo el programa.

## 🚀 Características

* **Módulo `abc`:** Uso de la librería estándar de Python para habilitar la creación de clases abstractas.
* **Clases Abstractas:** Definición de una clase base `Animal` que sirve exclusivamente como molde para otras clases.
* **Métodos Abstractos:** Uso del decorador `@abstractmethod` para forzar a las subclases a escribir su propia versión del método `hablar()`.
* **Clases Concretas:** Implementación de las clases `Perro` y `Gato` que cumplen con el contrato de la clase padre y definen exactamente cómo "hablan".

## 🧠 Conceptos de Programación Aplicados

Este código es fundamental para entender:
* **Abstracción:** Ocultar los detalles de implementación y definir solo la funcionalidad esencial (el *qué* debe hacer, no el *cómo*).
* **Interfaces / Contratos:** Cómo asegurar que cualquier nueva clase hija (ej. `Vaca`, `Pato`) incluya obligatoriamente ciertos métodos para evitar errores a futuro.
* **Decoradores en Python:** Uso del símbolo `@` para modificar o establecer reglas en el comportamiento de un método.


   ```

