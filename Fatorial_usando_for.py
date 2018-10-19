def main():
    '''
    Programa que lê um número inteiro n >= 0 e imprime n!
    '''

    print("Cálculo do fatorial de um número\n")

    # leia o valor de n
    n = int(input("Digite um número inteiro não-negativo: "))

    # inicialização da variável que armazena os fatoriais
    n_fat = 1

    # calcule n!
    for i in range(2,n+1):
        n_fat = n_fat * i 

    print("%d! = %d" %(n, n_fat))     
        

main()
