from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Configuração da tela
screen = Screen()
screen.setup(width=600, height=600) # Tamanha da tela
screen.bgcolor('black') # Cor de fundo
screen.title('Meu jogo da Cobrinha / My Snake Game') # Título da janela    
screen.tracer(0) # Desativa a atualização automática da tela ( para usar manualmente com screen.update())

# Instanciando os objetos principais do jogo
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Definindo os controles da cobrinha
screen.listen() # Ativa escuta de eventos do teclado
screen.onkey(snake.up, 'Up')           # Tecla ↑
screen.onkey(snake.down, 'Down')       # Tecla ↓
screen.onkey(snake.left, 'Left')       # Tecla ←
screen.onkey(snake.right, 'Right')     # Tecla →

# Loop principal do jogo
game_is_on = True
while game_is_on:
    screen.update()     # Atualiza a tela manualmente
    time.sleep(0.1)     # Delay para controlar a velocidade da cobrinha
    snake.move()        # Move a cobrinha

    # Detecta se houve colisão com a comida
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detecta se houve colisão com o muro
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detecta se houve colisão com o próprio corpo
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
        
    
# Fecha a janela quando o jogo termina
screen.exitonclick()
