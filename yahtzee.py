from random import random, randint  # Importa la función random para generar números aleatorios
from tabulate import tabulate  # Importa la función tabulate para mostrar datos en forma de tabla
from collections import Counter  # Importa Counter para contar elementos en una lista
import math  # Importa el módulo math para operaciones matemáticas

def main():
    # Inicialización de las tablas para cada jugador con sus categorías y puntuaciones
    tabla_jugador1 = [["Sección", "uno", "dos", "tres", "cuatro", "cinco", "seis", "3 of a\nKind",
                      "4 of a\nKind", "Full\nHouse", "Small\nStr8", "Large\nStr8", "Yahtzee", "Chance"],
                     ["Puntuación\nActual", *[0]*13], ["Puntaje\nPara Agregar",
                                                    *[0]*13], ["Terminado", *["No"]*13],
                     ["63 to Bonus", 0], ["Puntaje Total", 0]]
    
    tabla_jugador2 = [["Sección", "uno", "dos", "tres", "cuatro", "cinco", "seis", "3 of a\nKind",
                      "4 of a\nKind", "Full\nHouse", "Small\nStr8", "Large\nStr8", "Yahtzee", "Chance"],
                     ["Puntuación\nActual", *[0]*13], ["Puntaje\nPara Agregar",
                                                    *[0]*13], ["Terminado", *["No"]*13],
                     ["63 to Bonus", 0], ["Puntaje Total", 0]]

    juego(tabla_jugador1, tabla_jugador2)

def tirada_nueva(tabla, dados):
    tiradas = 1
    while tiradas <= 3:  # Realiza hasta 3 tiradas
        print(f"Tirada {tiradas}: {dados}")  # Muestra los dados de la tirada actual
        tabla = puntuar_tirada(tabla, dados)  # Calcula la puntuación de la tirada
        mostrar_tabla(tabla)  # Muestra la tabla actualizada
        print(tabulate([["Tirada " + str(tiradas)]], tablefmt="grid"))  # Muestra la tirada actual en formato de tabla
        print(mostrar_dados(dados))  # Muestra los dados en formato de tabla
        if tiradas == 3 or len(set(dados)) == 1 and tabla[3][12] == "Sí":  # Termina la tirada si se han realizado 3 tiradas o todos los dados son iguales y Yahtzee está marcado
            return tabla
        while True:
            otra_vez = input("\n¿Quieres volver a tirar? S/N: ").lower()  # Pregunta si se quiere tirar de nuevo
            if otra_vez in ["s", "n", "si", "no"]:  # Verifica la respuesta
                break
        if otra_vez == "s" or otra_vez == "si":  # Si se quiere tirar de nuevo
            tabla[2] = ["Puntaje\nPor Agregar", *[0]*13]  # Reinicia los puntajes por agregar
            seleccionar = input(
                "\nSelecciona los Dados a Volver a Tirar.\nEjemplo: 1 2 3 4 5 \n").split(" ")  # Pide seleccionar los dados a volver a tirar
            for i in seleccionar:  # Para cada dado seleccionado
                idx = int(i) - 1  # Obtiene el índice correspondiente
                dados[idx] = math.ceil(random() * 6)  # Genera un nuevo número aleatorio para ese dado
            print(mostrar_dados(dados))  # Muestra los dados actualizados
            tiradas += 1  # Incrementa el número de tiradas
        else:
            break
    return tabla

def mostrar_dados(dados):
    d6 = ["1", "2", "3", "4", "5", "6"]  # Lista de números del 1 al 6
    return tabulate([[d6[i-1] for i in dados]], tablefmt="grid")  # Retorna los dados en formato de tabla

def puntuar_tirada(tabla, dados):
    for i in range(1, 14):  # Para cada categoría del juego
        if i <= 6:  # Categorías del 1 al 6
            for j in range(5):  # Para cada dado
                if dados[j] == i:  # Si el dado tiene el número de la categoría
                    tabla[2][i] += dados[j]  # Agrega el valor del dado al puntaje por agregar
        elif i == 7 or i == 8:  # 3 of a Kind o 4 of a Kind
            for j in range(1, 7):  # Para cada número posible
                
                if dados.count(j) >= i-4:  # Si el dado actual aparece al menos i-4 veces en la tirada
                    tabla[2][i] += sum(dados)  # Suma todos los dados al puntaje por agregar
        elif i == 9:  # Full House
            valores_tirada = list(Counter(dados).values())  # Cuenta la frecuencia de cada dado
            if valores_tirada == [2, 3] or valores_tirada == [3, 2]:  # Si hay 2 dados iguales y 3 dados iguales
                tabla[2][i] += 25  # Agrega 25 al puntaje por agregar
        elif i == 10:  # Small Straight
            smstr1 = [1, 2, 3, 4]
            smstr2 = [2, 3, 4, 5]
            smstr3 = [3, 4, 5, 6]
            if any([all(num in dados for num in smstr1),  # Si hay una escalera corta en la tirada
                    all(num in dados for num in smstr2),
                    all(num in dados for num in smstr3)]):
                tabla[2][i] += 30  # Agrega 30 al puntaje por agregar
        elif i == 11:  # Large Straight
            dados_ordenados = sorted(dados)  # Ordena los dados
            if dados_ordenados == [1, 2, 3, 4, 5] or dados_ordenados == [2, 3, 4, 5, 6]:  # Si hay una escalera larga en la tirada
                tabla[2][i] += 40  # Agrega 40 al puntaje por agregar
        elif i == 12:  # Yahtzee
            if len(set(dados)) == 1:  # Si todos los dados son iguales
                if tabla[3][i] == "No":  # Si Yahtzee no está marcado como hecho antes
                    tabla[2][i] += 50  # Agrega 50 al puntaje por agregar
                else:  # Si Yahtzee ya está marcado como hecho antes
                    return bono(tabla, dados)  # Aplica el bono correspondiente
        else:  # Chance
            tabla[2][i] += sum(dados)  # Agrega la suma de todos los dados al puntaje por agregar
    return tabla

def bono(tabla, dados):
    if tabla[1][12] > 0:  # Si Yahtzee ya se ha marcado antes
        tabla[1][12] += 100  # Agrega 100 al puntaje actual de Yahtzee
    if tabla[3][dados[0]] == "No":  # Si la categoría Yahtzee no está marcada como hecha antes para ese número de dado
        tabla[2] = ["Puntaje\nPor Agregar", *[0]*13]  # Reinicia los puntajes por agregar
        tabla[2][dados[0]] = sum(dados)  # Agrega la suma de los dados al puntaje por agregar
    else:  # Si la categoría Yahtzee ya está marcada como hecha antes para ese número de dado
        tabla[2] = ["Puntaje\nPor Agregar", *[0]*8, 25, 30, 40, 50, sum(dados)]  # Actualiza los puntajes por agregar
    return tabla

def mostrar_tabla(tabla):
    print(tabulate(tabla[:4], tablefmt="grid"))  # Muestra la parte superior de la tabla
    print(tabulate(tabla[4:6], tablefmt="grid"))  # Muestra la parte inferior de la tabla

def juego(tabla_jugador1, tabla_jugador2):
    turno = 1  # Inicializa el turno
    bono_yahtzee_j1 = False  # Inicializa el bono Yahtzee para el jugador 1 como falso
    bono_yahtzee_j2 = False  # Inicializa el bono Yahtzee para el jugador 2 como falso
    while "No" in tabla_jugador1[3] or "No" in tabla_jugador2[3]:  # Mientras haya categorías no completadas en la tabla de algún jugador
        if turno % 2 != 0:  # Si es el turno del jugador 1
            print(f"Turno Jugador 1\n")
            dados = [randint(1, 6) for _ in range(5)]  # Genera 5 dados aleatorios
            tabla_jugador1 = tirada_nueva(tabla_jugador1, dados)  # Realiza una nueva tirada para el jugador 1
            tabla_jugador1 = actualizar_tabla(tabla_jugador1)  # Actualiza la tabla del jugador 1
            if tabla_jugador1[3][12] == "Sí" and not bono_yahtzee_j1:  # Si Yahtzee está marcado como hecho y el bono Yahtzee no se ha aplicado
                tabla_jugador1[1][12] += 100  # Aplica el bono Yahtzee
                bono_yahtzee_j1 = True  # Marca el bono Yahtzee como aplicado
            mostrar_tabla(tabla_jugador1)  # Muestra la tabla del jugador 1
        else:  # Si es el turno del jugador 2
            print(f"Turno Jugador 2\n")
            dados = [randint(1, 6) for _ in range(5)]  # Genera 5 dados aleatorios
            tabla_jugador2 = tirada_nueva(tabla_jugador2, dados)  # Realiza una nueva tirada para el jugador 2
            tabla_jugador2 = actualizar_tabla(tabla_jugador2)  # Actualiza la tabla del jugador 2
            if tabla_jugador2[3][12] == "Sí" and not bono_yahtzee_j2:  # Si Yahtzee está marcado como hecho y el bono Yahtzee no se ha aplicado
                tabla_jugador2[1][12] += 100  # Aplica el bono Yahtzee
                bono_yahtzee_j2 = True  # Marca el bono Yahtzee como aplicado
            mostrar_tabla(tabla_jugador2)  # Muestra la tabla del jugador 2
        turno += 1  # Incrementa el número de turnos
    print("Fin del Juego")  # Muestra el fin del juego
    print(f"Puntaje Final Jugador 1: {tabla_jugador1[5][1]}")  # Muestra el puntaje final del jugador 1
    print(f"Puntaje Final Jugador 2: {tabla_jugador2[5][1]}")  # Muestra el puntaje final del jugador 2

def actualizar_tabla(tabla):
    for i in range(1, 14):  # Para cada categoría del juego
        if tabla[3][i] == "No":  # Si la categoría no está marcada como hecha
            if tabla[2][i] != 0:  # Si hay puntaje por agregar en la categoría
                while True:
                    print(f"Marca 'sí' si deseas seleccionar esta opción, de lo contrario, marca 'no' para ver otras opciones..")
                    opcion = input(f"¿Deseas agregar el puntaje {tabla[2][i]} a la categoría {tabla[0][i]}? S/N: ").lower()  # Pregunta si se quiere agregar el puntaje a la categoría
                    if opcion in ["s", "n", "si", "no"]:  # Verifica la respuesta
                        break
                if opcion == "s" or opcion == "si":  # Si se quiere agregar el puntaje
                    tabla[1][i] += tabla[2][i]  # Agrega el puntaje actual al puntaje por agregar
                    tabla[4][1] += tabla[2][i]  # Actualiza el puntaje total
                    tabla[3][i] = "Sí"  # Marca la categoría como hecha
                    if i <= 6:  # Si la categoría está en la sección superior
                        tabla[4][1] += tabla[2][i]  # Actualiza el puntaje total en la sección superior
                    tabla[2] = ["Puntaje\nPor Agregar", *[0]*13]  # Reinicia los puntajes por agregar
                    break
    return tabla

if __name__ == "__main__":
    main()  # Ejecuta la función principal
