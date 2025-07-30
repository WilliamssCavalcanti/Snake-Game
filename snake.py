from turtle import Turtle

# Posições inicias dos 3 segmentos da cobrinha
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Distância que cada segmento se move a cada passo
MOVE_DISTANCE = 20

# Ângulos para as direções que a cobrinha vai se mover
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []     # Lista para armazenar os segmentos da cobrinha
        self.create_snake()    # Cria os 3 segmentos iniciais
        self.head = self.segments[0]     # Define o primeiro segmento como a "cabeça"

    def create_snake(self):   # Cria a cobrinha com os segmentos nas posições iniciais
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    
    def add_segment(self, position): # Adiciona um novo segmento da cobrinha na posição informada
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment) 
    
    def reset(self): # Reinicia a cobra quando há colisão
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self): # Adiciona um novo segmento no fina lda cobrinha( (ao comer a comida)
        self.add_segment(self.segments[-1].position())
    
    def move(self):   # Move a cobrinha faezndo cada segmento seguir o anterior.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Os métodos abaixo controlam a direção da cabeça da cobrinha
    
    def up(self):   # Vira para cima se não estiver indo para baixo
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self): # Vira para baixo se não estiver indo para a cima
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self): # Vira para a esquerda se não estiver indo para a direita
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self): # VIra para a direita se não estiver indo para a esquerda
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
