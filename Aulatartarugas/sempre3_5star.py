import turtle
jn = turtle.Screen()         # Configurar a janela e seus atributos
jn.bgcolor("lightgreen")
jn.title("Tess & Alex")

teca = turtle.Turtle()       # Criar e configurar alguns atributos de Teca
teca.color("hotpink")
teca.pensize(5)

joana = turtle.Turtle()       # Criar Joana


for i in range(5):
 joana.forward(144)             # Fazer Joana desenhar um quadrado
 joana.left(144)


jn.mainloop()
