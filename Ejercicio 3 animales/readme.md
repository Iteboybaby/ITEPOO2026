# 🐾 Sistema de Animales (Herencia en Python)

Este es un proyecto educativo en Python diseñado para ilustrar dos de los pilares más importantes de la Programación Orientada a Objetos (POO): **La Herencia** y el **Polimorfismo**.

El código define una clase padre `Animal` con atributos genéricos, y dos clases hijas (`Perro` y `Gato`) que heredan estas características pero personalizan su comportamiento específico.

## 🚀 Características

* **Clase Base (Padre):** Estructura central `Animal` que inicializa el nombre y la edad, e incluye métodos generales como `describir()`.
* **Clases Derivadas (Hijas):** Implementación de las clases `Perro` y `Gato` que heredan y reutilizan el código de la clase base sin necesidad de volver a escribir los constructores.
* **Sobrescritura de Métodos:** Las clases hijas modifican el método `hablar()` para emitir el sonido correspondiente ("Guau!" o "Miau!"), adaptando la función a su propio contexto.

## 🧠 Conceptos de Programación Aplicados

Este repositorio es ideal para comprender de forma práctica:
* **Herencia (Inheritance):** Creación de nuevas clases basadas en clases ya existentes para compartir atributos (`nombre`, `edad`).
* **Polimorfismo:** Capacidad de diferentes objetos de responder de manera distinta al mismo llamado de método (`hablar()`).
* **Reutilización de Código:** Mantenimiento de un código limpio (DRY - Don't Repeat Yourself) centralizando la lógica común en la superclase.

