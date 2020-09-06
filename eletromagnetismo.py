# Python 3.7
# by Jadson Marliere de Oliveira
# Este projeto possui fins academicos - Disciplina ELETROMAGNETISMO

def valores_fonte_test():

def recebe_valores_usuario():
    qtd_cargas  = input('Digite a quantidade de cargas')
    lista_cargas = []
    lista_cartesiana = []
    n = 1
    print(' Digite primeiramente a carga de prova :')
    for elem in range(qtd_cargas):
        lista_cargas.append(input('Digite a {} carga'.format(n)))
        lista_cartesiana.append('digite a posicao espacial da carga no formato: xyz (sem espaco) ex: para p1(5,-3,4) ->5-35')
        n =+ 1

    return lista_cargas

def calcula_forca_resultante():
    lista_cargas = recebe_valores_usuario()
    # constante de permissividade
    e_const = 8.854 * pow(10, -12)
    k = 1 / (4 * 3.1415 * e_const)

def calcula_campo_eletrico():

def main_screen():