# ⚔️ Sistema de Clases RPG: Aventureros (Herencia en Python)

Este proyecto es una simulación de un sistema de clases de un videojuego RPG o MMO especialmente en el personaje escrito en Python. 

Es un ejemplo perfecto para demostrar la **Herencia** y el **Polimorfismo** en la Programación Orientada a Objetos (POO).

El código central define una clase padre `Aventurero` que establece los atributos básicos (nombre y nivel) de cualquier personaje. A partir de ella, se derivan cuatro subclases especializadas (`Guerrero`, `Mago`, `Arquero` y `Tanque`)
que heredan estas características pero ejecutan sus habilidades de forma única.

## 🚀 Características

* **Clase Base `Aventurero`:** Centraliza la creación de personajes con su nivel y un método general para presentarse.
* **Especialización de Clases (Subclases):** Cuatro tipos de personajes distintos que reutilizan el código del constructor original.
* **Sobrescritura de Métodos (Polimorfismo):** Cada subclase modifica el método `usar_habilidad()` para reflejar su estilo de combate, ya sea lanzando hechizos, disparando flechas, atacando cuerpo a cuerpo o defendiendo al grupo.

## 🧠 Conceptos de Programación Aplicados

Este repositorio ilustra de forma práctica:
* **Herencia (Inheritance):** Cómo las clases hijas obtienen los atributos y métodos de la clase padre.
* **Polimorfismo:** Cómo el mismo llamado al método `usar_habilidad()` produce un resultado completamente diferente dependiendo de si el objeto es un Mago o un Tanque.
* **Diseño Modular:** Estructuración de código escalable (es muy fácil agregar una nueva clase, como `Asesino` o `Clérigo`, en el futuro).

