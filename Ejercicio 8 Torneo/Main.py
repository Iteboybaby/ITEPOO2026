from Competidor import Competidor
from Observador import Observador

def ejecutar_torneo():
    print("--- Competidor ---")
    c1 = Competidor("Maximus", "241991", "Leyenda", "Equipo 17")
    c1.mostrar_perfil()
    print()
    c1.ganar_puntos(100)
    c1.perder_puntos(10)

    print("\n--- Observador ---")
    o1 = Observador("Alexa", "210", "principiante")
    o1.ver_partida()
    o1.ver_partida()
    o1.mostrar_perfil()

if __name__ == "__main__":
    ejecutar_torneo()