# 🛡️ Manejo de Excepciones en Python

Este repositorio contiene un script educativo que demuestra cómo implementar el **Manejo de Excepciones** en Python. 
En esta clase obvservamos como crear nuestros propios mensajes de errores para que asi cualquier persona que quiera introducir datos en nuestro
programa, pueda verificar de que se trata el error mas comun que le esta sucediendo.

Es una guía práctica para aprender a controlar errores y evitar que los programas colapsen (crasheen) cuando el usuario ingresa datos inesperados o se realizan operaciones inválidas.

El código utiliza la estructura completa de control de errores de Python: bloques `try`, `except`, `else` y `finally`.

## 🚀 Características

* **Bloque `try`:** Contiene el código "riesgoso" que interactúa con el usuario (solicitar números y realizar una división).
* **Captura de Errores Específicos (`except`):** * Maneja `ValueError` para evitar que el programa falle si el usuario escribe texto o símbolos en lugar de números enteros.
  * Maneja `ZeroDivisionError` para prevenir errores lógicos al intentar dividir entre cero.
* **Bloque `else`:** Ejecuta código (imprimir el resultado) única y exclusivamente si el bloque `try` fue exitoso sin arrojar ninguna excepción.
* **Bloque `finally`:** Garantiza la ejecución de un mensaje final, asegurando que esta línea se corra sin importar si hubo un error o si la operación fue un éxito.

## 🧠 Conceptos de Programación Aplicados

Este código es una excelente demostración de:
* **Robustez del Software:** Cómo anticipar y manejar los posibles errores del usuario para crear aplicaciones estables.
* **Validación de Entradas (Input Validation):** Uso de conversiones de tipo (`int()`) dentro de bloques seguros para filtrar información.
* **Flujo de Control Avanzado:** Uso estructurado de las palabras reservadas de Python para dictar el camino de ejecución del script según diferentes escenarios.
