"""
EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que su

equipo lleva acumulados en el campeonato, para ello recibe cada semana la

información de la cantidad total de partidos, desde el inicio del campeonato, que

el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado

recibe un punto, por cada partido ganado tres puntos y por los perdidos cero

puntos.
"""

"""
EPS

Entrada por usuario
    partido_perdido
    partido_ganado
    partido_empatado

Proceso
    cálculo de partidos por puntos
    partido_perdido *+ 0
    partido_empatado *+ 1
    partido_ganado *+ 3

    total_puntos = partido_perdido + partido_empatado + partido_ganado

Salida
    Mostrar total_puntos 
"""

print("Ejercicio 3 - Puntos del Campeonato \n")

# Pido los datos al usuario Entrada

partido_perdido = int(input("\n Ingresá la cantidad de partidos perdidos: "))

partido_empatado = int(input("\n Ingresá la cantidad de partidos empatados: "))

partido_ganado = int(input("\n Ingresá la cantidad de partidos ganados: "))

# Proceso

partido_perdido *+ 0

partido_empatado *+ 1

partido_ganado *+ 3

total_puntos = partido_perdido + partido_empatado + partido_ganado

# Salida

print(f"La cantidad total de puntos es : {total_puntos}")