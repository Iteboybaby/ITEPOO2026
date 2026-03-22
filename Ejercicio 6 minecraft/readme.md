
# 🟩 Sistema de Mobs de Minecraft (Abstracción en Python)

Este repositorio contiene un script educativo en Python que modela criaturas (mobs) de Minecraft para demostrar el concepto de **Abstracción** utilizando Clases Base Abstractas (ABC).

El código central define una clase abstracta `Mob` que actúa como una plantilla estricta. Obliga a cualquier subclase derivada (como `Creeper`, `Enderman`, `Vaca` o `Zombie`) 
a implementar sus propios sonidos, comportamientos y estilos de movimiento específicos, garantizando una estructura consistente y sin errores en toda la lógica del juego.

## 🚀 Características

* **Clase Base Abstracta (`Mob`):** Establece atributos estándar (nombre, vida) y un método concreto (`presentarse()`) que muestra las estadísticas formateadas para cualquier mob en este juego.
* **Contratos Estrictos (Interfaces):** Usa el decorador `@abstractmethod` para garantizar que cada nuevo mob creado en el futuro incluya obligatoriamente un sonido, un comportamiento y un tipo de movimiento.
* **Indicaciones de Tipo (Type Hinting):** Implementa el tipado moderno de Python (ej. `-> str`, `vida: int`) para hacer que el código sea mucho más legible y fácil de depurar.
* **Implementaciones Concretas:** Incluye cuatro subclases distintas y completamente funcionales que cumplen con el contrato abstracto, cada una a su manera única y claro para implementar mas a futuro.

## 🧠 Conceptos de Programación Aplicados

Este proyecto es una demostración perfecta de:
* **Abstracción:** Ocultar detalles complejos de fondo y enfocarse solo en las características esenciales de un objeto.
* **Diseño de Interfaces:** Crear reglas que las clases hijas deben seguir, previniendo la falta de métodos y estandarizando el código.
* **Polimorfismo:** Permitir que un solo método concreto (`presentarse()`) llame dinámicamente a los métodos abstractos únicos de la subclase que se esté utilizando en ese momento.
