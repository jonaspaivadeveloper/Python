import time
t=time.localtime()
print(t)

def dia_semana(w):
    nome_dia=["segunda","terça","quarta","quinta","sexta","sabado","domingo"]

    return nome_dia[w]

def mes(m):
    nome_mes=["Janeiro","Fevereiro","março","abril","maio","junho","julho","agosto","setembro","agosto","setembro","outobro","novembro","dezembro"]

    return 
    nome_mes[m-1]

def mostrar_dia_hora():
    lt=time.localtime()
    print("\n\n*******\n")
    print("hoje e",dia_semana(lt.tm_wday),
    " ",
    lt.tm_mday,
    "de",mes(lt.tm_mon),
    "de",lt.tm_year,
    "e são as", lt.tm_hour,
    ":",lt.tm_min,
    "horas\n")

    print("********\n")

mostrar_dia_hora()
