# 🍽️ Sistema de Menú de Restaurante (Herencia en Python)

Este repositorio contiene un script educativo en Python que modela el menú de un restaurante.
Es un ejemplo excelente y fácil de entender sobre cómo aplicar la **Herencia** y el **Polimorfismo** en la Programación Orientada a Objetos (POO) 
para organizar información del mundo real.

El código base define una clase padre llamada `Platillo`, que contiene los atributos universales de cualquier elemento del menú (nombre y precio).
De ahí, se desprenden tres subclases especializadas (`Comida`, `Bebida` y `Postre`) que heredan esos datos pero clasifican el tipo de platillo a su manera.

## 🚀 Características

* **Clase Base `Platillo`:** Estructura central que inicializa el nombre y el precio, e incluye un método general para mostrar la información en formato de ticket.
* **Clasificación por Subclases:** Implementación de las clases `Comida`, `Bebida` y `Postre`, reutilizando eficientemente el constructor original sin duplicar código.
* **Polimorfismo en Acción:** Cada subclase sobrescribe el método `tipo()` para imprimir un mensaje personalizado dependiendo de la categoría del producto.

## 🧠 Conceptos de Programación Aplicados

Este proyecto es ideal para demostrar conocimientos en:
* **Abstracción:** Creación de un modelo general (`Platillo`) que sirve como plantilla.
* **Herencia (Inheritance):** Transmisión de atributos (`nombre`, `precio`) de la clase padre a las hijas.
* **Sobrescritura de Métodos:** Adaptación del comportamiento de una función heredada (`tipo()`) según el contexto de la subclase.

