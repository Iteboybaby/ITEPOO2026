class Mascota:
    def __init__(self, nombre: str, tipo: str, edad: int, nivelFelicidad: int):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.nivelFelicidad = nivelFelicidad

    def alimentar(self):
        """Aumenta la felicidad en 10 (máx 100)"""
        self.nivelFelicidad += 10
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100

    def jugar(self):
        """Aumenta la felicidad en 20 (máx 100)"""
        self.nivelFelicidad += 20
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100

    def mostrarEstado(self) -> str:
        return f"Mascota: {self.nombre} ({self.tipo}) - Felicidad: {self.nivelFelicidad}%"

    def esFeliz(self) -> bool:
        """Retorna True si la felicidad > 70"""
        return self.nivelFelicidad > 70

# --- Prueba de funcionamiento ---
mi_mascota = Mascota("Max", "Gato", 2, 60)

print(mi_mascota.mostrarEstado()) # Estado inicial
mi_mascota.jugar()                # Sube a 80
print(f"¿Es feliz?: {mi_mascota.esFeliz()}") 
print(mi_mascota.mostrarEstado()) # Estado final