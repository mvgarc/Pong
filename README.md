# Pong
Juego de Pong con pygame

Inicialización de Pygame: Importa la biblioteca Pygame y realiza la inicialización necesaria.

Configuración de la Ventana: Configura la ventana del juego con un tamaño de 640x480 píxeles y un título "Pong".

Carga de Imágenes: Intenta cargar las imágenes "ball.png" y "bate.png". Si hay algún error durante la carga, muestra un mensaje de error, cierra Pygame y termina el programa.

Rectángulos y Velocidad: Define rectángulos para la pelota y el bate, así como la velocidad inicial de la pelota.

Bucle Principal del Juego: Inicia un bucle principal que controla la lógica del juego. Maneja eventos, como cerrar la ventana o presionar teclas. Mueve el bate, verifica colisiones y actualiza la posición de la pelota.

Dibujo en Pantalla: Dibuja el fondo y las imágenes en la ventana del juego.

Control de Velocidad: Utiliza pygame.time.Clock().tick(60) para controlar la velocidad del bucle y mantener una tasa de cuadros por segundo (FPS) de 60.

Cierre del Juego: Al salir del bucle principal, cierra Pygame.

Puedes copiar y pegar este código en el README de tu proyecto junto con las imágenes "ball.png" y "bate.png" en la misma carpeta que el script. Recuerda adaptar la explicación según las necesidades específicas de tu proyecto.
