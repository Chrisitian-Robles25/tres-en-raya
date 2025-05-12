# Tres en Raya - Neon Edition

Este proyecto es una implementación del clásico juego "Tres en Raya" (también conocido como "Tic Tac Toe") con un diseño de neón. El juego permite a dos jugadores competir entre sí en un tablero de 3x3.

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- **assets/sounds/click.wav**: Este archivo de sonido se reproduce cuando un jugador hace clic en una casilla del tablero.
- **assets/sounds/win.wav**: Este archivo de sonido se reproduce cuando un jugador gana la partida.
- **assets/sounds/draw.wav**: Este archivo de sonido se reproduce cuando la partida termina en empate.
- **utils/game_logic.py**: Este archivo contiene la lógica del juego, incluyendo la función `check_winner`, que determina si hay un ganador o si la partida ha terminado en empate.
- **main.py**: Este archivo es el punto de entrada de la aplicación. Inicializa Pygame, configura la ventana del juego, gestiona el bucle principal del juego, dibuja el tablero y maneja la entrada del usuario.

## Instrucciones para Ejecutar el Juego

1. Asegúrate de tener Python y Pygame instalados en tu sistema.
2. Clona o descarga este repositorio en tu máquina local.
3. Navega a la carpeta del proyecto.
4. Ejecuta el archivo `main.py` con el siguiente comando:

   ```
   python main.py
   ```

5. Disfruta del juego y compite con tus amigos.

## Notas

- El juego es para dos jugadores, donde uno juega con "X" y el otro con "O".
- Los sonidos se reproducen en momentos clave del juego para mejorar la experiencia del usuario.
- Asegúrate de que los archivos de sonido estén en la carpeta correcta para que el juego funcione correctamente.