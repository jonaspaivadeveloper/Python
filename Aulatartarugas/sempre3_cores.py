import turtle
jn = turtle.Screen()         # Configurar a janela e seus atributos
#jn.bgcolor("lightgreen")
jn.title("Tess & Alex")

teca = turtle.Turtle()  
Color=input('Digite uma cor: ')
jn.bgcolor(Color)

teca.color("red")
teca.pensize(5)


joana = turtle.Turtle()       # Criar Joana

teca.forward(80)             # Fazer Teca desenhar um triângulo equilátero
teca.left(120)
teca.forward(80)
teca.left(120)
teca.forward(80)
teca.left(120)               # Completar o triângulo

teca.right(180)              # Fazer Teca dar meia volta
teca.forward(80)             # Movê-la para longe da origem

cores = ["yellow", "red", "purple", "blue"]
for i in range(4):
    joana.color(cores[i])
    joana.forward(50)
    joana.left(90)

jn.mainloop()

