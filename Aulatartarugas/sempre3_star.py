import turtle
jn = turtle.Screen()         # Configurar a janela e seus atributos
jn.bgcolor("lightgreen")
jn.title("Tess & Alex")

teca = turtle.Turtle()       # Criar e configurar alguns atributos de Teca
teca.color("hotpink")
teca.pensize(5)

joana = turtle.Turtle()       # Criar Joana


for i in range(6):
 teca.forward(144)             # Fazer Teca desenhar um triângulo equilátero
 teca.left(144)
                               # Completar o triângulo

teca.right(144)              # Fazer Teca dar meia volta
teca.forward(144)             # Movê-la para longe da origem



for i in range(6):
    joana.forward(144)             # Fazer Joana desenhar um quadrado
    joana.left(144)

jn.mainloop()
