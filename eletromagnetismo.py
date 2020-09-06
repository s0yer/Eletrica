# Python 3.7
# by Jadson Marliere de Oliveira
# Este projeto tem fins academicos

def valores_fonte_test():

def recebe_valores_usuario():
    qtd_cargas  = input('Digite a quantidade de cargas')
    lista_cargas = []
    n = 1
    print(' Digite primeiramente a carga de prova :')
    for elem in range(qtd_cargas):
        lista_cargas.append(input('Digite a {} carga'.format(n)))
        n =+ 1

    return lista_cargas

def calcula_forca_resultante():
    lista_cargas = recebe_valores_usuario()
    # constante de permissividade
    e_const = 8.854 * pow(10, -12)
    k = 1 / (4 * 3.1415 * e_const)

def calcula_campo_eletrico():

def main_screen():