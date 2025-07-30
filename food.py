from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()    # Inicializa como uma Turtle
        self.shape('circle')     # Define o formato como um círculo
        self.penup()             # Levanta o "lápis" (Não deixa rastro)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)    # Diminui o tamanho do círculo
        self.color('blue')     # Cor da comida (azul)
        self.speed('fastest')    # Cria a comida rapidamente
        self.refresh()     # Posiciona a primeira comida em um local aleatório

    def refresh(self): # Gera nova posição aleatória para a comida na tela
        random_x = random.randint(-280, 280)   # Eixo X aleatório dentro da tela
        random_y = random.randint(-280, 280)   # Eixo Y aleatório dentro da tela
        self.goto(random_x, random_y)          # Movea comida para a nova posição
