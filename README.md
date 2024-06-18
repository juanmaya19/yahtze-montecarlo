# Yahtzee Game

## Descripción
El juego de Yahtzee es una aplicación de consola que simula el famoso juego de dados Yahtzee. Permite a dos jugadores competir para obtener el puntaje más alto al completar diferentes categorías con combinaciones específicas de números en los dados.

## Preparación del Juego

### Inicio del Juego:
- El juego se realiza entre dos jugadores.
- Cada jugador tiene una tabla con diferentes categorías y puntajes que deben completar a lo largo de las rondas.

### Categorías y Puntuación:
- Uno a Seis: Suma de los dados con el número correspondiente.
- 3 of a Kind: Tres dados iguales. Puntaje igual a la suma de todos los dados.
- 4 of a Kind: Cuatro dados iguales. Puntaje igual a la suma de todos los dados.
- Full House: Tres dados iguales y dos dados iguales. Puntaje fijo de 25 puntos.
- Small Straight: Cuatro dados consecutivos. Puntaje fijo de 30 puntos.
- Large Straight: Cinco dados consecutivos. Puntaje fijo de 40 puntos.
- Yahtzee: Cinco dados iguales. Puntaje fijo de 50 puntos.
- Chance: Suma de todos los dados. Puede usarse como comodín.

## Cómo Jugar

### Turno de Juego:
- En cada turno, el jugador lanza cinco dados.
- Después de cada lanzamiento, el jugador decide qué dados guardar y cuáles volver a lanzar.
- Se pueden hacer hasta tres lanzamientos en un turno.

### Selección de Categoría:
- Al final de cada turno, el jugador debe seleccionar la categoría en la que desea colocar su puntaje.
- El puntaje se suma automáticamente a la tabla del jugador.

### Reglas Especiales:
- Yahtzee: Obtén cinco dados iguales para ganar un bono de 100 puntos adicionales.
- Full House: Consigue tres dados iguales y dos dados iguales para obtener 25 puntos fijos.
- Escaleras: Hay dos tipos de escaleras: Small Straight (30 puntos) y Large Straight (40 puntos).
- 3 of a Kind y 4 of a Kind: Obtén tres dados iguales o cuatro dados iguales para sumar el puntaje correspondiente.

### Fin del Juego:
- El juego consta de 13 rondas, una para cada categoría.
- Al completar todas las categorías, se suman los puntajes de cada jugador.
- El jugador con el puntaje total más alto al final de las 13 rondas gana el juego.

## Instrucciones de Uso

### Inicio del Juego:
- Ejecuta el programa para iniciar el juego.
- Selecciona el número de jugadores (2 en este caso).
- Comienza la partida y sigue las instrucciones en pantalla.

### Desarrollo del Juego:
- En cada turno, lanza los dados y elige qué dados guardar y cuáles volver a lanzar.
- Selecciona la categoría en la que deseas colocar tu puntaje al finalizar cada tirada.

### Finalización del Juego:
- Al completar todas las rondas, se calcula el puntaje total de cada jugador.
- El juego muestra al jugador con el puntaje más alto como ganador.

## Notas Adicionales
- La tabla de puntajes se actualiza automáticamente después de cada turno.
- El juego proporciona información detallada sobre las categorías y puntajes en todo momento.
- Puedes consultar las reglas en cualquier momento durante el juego.
