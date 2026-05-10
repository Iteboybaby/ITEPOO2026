🏆 Sistema de Gestión de Torneo (POO)
Este repositorio contiene una implementación robusta en Python para la gestión de usuarios en un entorno de torneo. El proyecto se centra en demostrar los pilares fundamentales de la Programación Orientada a Objetos (POO), tales como la herencia, el encapsulamiento y la especialización de clases.

📝 Descripción del Proyecto
El sistema está diseñado para modelar el comportamiento de diferentes tipos de participantes. Utiliza una arquitectura jerárquica donde una clase base define el comportamiento común, mientras que las clases derivadas añaden funcionalidades específicas según el rol del usuario.

🧬 Jerarquía de Clases
La estructura se divide en tres niveles principales:

Jugador (Clase Base):

Función: Actúa como el molde general para cualquier usuario.

Atributos: Almacena datos esenciales como el nombre, número de control y nivel de habilidad.

Competidor (Clase Hija):

Especialización: Usuarios activos que participan en el torneo.

Atributos extra: Gestión de pertenencia a un equipo.

Lógica: Implementa métodos para la gestión dinámica de puntos (ganar_puntos / perder_puntos).

Polimorfismo: Sobrescribe mostrar_perfil() utilizando super() para extender la funcionalidad base.

Observador (Clase Hija):

Especialización: Usuarios dedicados al análisis y visualización de partidas.

Lógica: Incluye un contador interno mediante el método ver_partida().
