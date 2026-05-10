Ejercicio 8: Sistema de Torneo (POO)
Este repositorio contiene una implementación en Python de un sistema de gestión para un torneo, enfocándose en los pilares de la Programación Orientada a Objetos (POO), específicamente en la herencia y la especialización de clases.



📝 Descripción
El sistema modela diferentes tipos de usuarios que interactúan en un torneo. 
A través de una clase base Jugador, se derivan especializaciones para manejar las acciones específicas de quienes compiten y de quienes observan.

Jerarquía de Clases:
Jugador (Clase Base): Contiene los atributos generales y compartidos (nombre, número de control y nivel).

Competidor (Clase Hija): Hereda de Jugador. Añade el atributo de equipo y métodos para el manejo de puntaje (ganar_puntos, perder_puntos). 
Sobrescribe el método mostrar_perfil() para incluir su información específica usando super().

Observador (Clase Hija): Hereda de Jugador. 
Permite llevar un registro del número de encuentros presenciados mediante el método ver_partida().