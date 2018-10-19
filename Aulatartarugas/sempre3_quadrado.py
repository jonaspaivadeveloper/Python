import turtle
jn = turtle.Screen()         # Configurar a janela e seus atributos
jn.bgcolor("lightgreen")
jn.title("Tess & Alex")

teca = turtle.Turtle()       # Criar e configurar alguns atributos de Teca
teca.color("hotpink")
teca.pensize(5)

joana = turtle.Turtle()       # Criar Joana

teca.forward(90)             # Fazer Teca desenhar um triângulo equilátero
teca.left(90)
teca.forward(90)
teca.left(90)
teca.forward(90)
teca.left(90)                # Completar o triângulo

teca.right(180)              # Fazer Teca dar meia volta
teca.forward(80)             # Movê-la para longe da origem

joana.forward(50)             # Fazer Joana desenhar um quadrado
joana.left(90)
joana.forward(50)
joana.left(90)
joana.forward(50)
joana.left(90)
joana.forward(50)
joana.left(90)

jn.mainloop()
