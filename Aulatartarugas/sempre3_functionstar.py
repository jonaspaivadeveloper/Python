import turtle
jn = turtle.Screen()         # Configurar a janela e seus atributos
jn.bgcolor("lightgreen")
jn.title("Tess & Alex")

teca = turtle.Turtle()       # Criar e configurar alguns atributos de Teca
teca.color("hotpink")
teca.pensize(5)

joana = turtle.Turtle()       # Criar Joana

def star(x):
    for i in range(x):
        joana.forward(x)             
        joana.left(x)


star(100)
jn.mainloop()


