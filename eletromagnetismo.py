# Python 3.7
# by Jadson Marliere de Oliveira
# Este projeto possui fins academicos - Disciplina ELETROMAGNETISMO

def valores_fonte_test():

def calcula_modulo(posicoes):
    modulo_posicoes = pow((pow(posicoes[0], 2) + pow(posicoes[1], 2) + pow(posicoes[2], 2)), 1/2)

    return modulo_posicoes

def recebe_valores_usuario():
    qtd_cargas  = input('Digite a quantidade de cargas: ')
    lista_cargas = []
    lista_cartesiana = []
    lista_r = []

    n = 1
    print(' Digite primeiramente a carga de prova :')

    for elem in range(qtd_cargas):
        # recebe valor da carga
        lista_cargas.append(input('Digite a {} carga'.format(n)))

        # recebe coordenadas do espaco:
        lista_posicoes = []
        print('Se alguma posicoes')
        lista_posicoes.append('digite a posicao no eixo X: ')
        lista_posicoes.append('digite a posicao no eixo Y: ')
        lista_posicoes.append('digite a posicao no eixo Z: ')

        # adicona coodenadas no array de posicoes
        lista_cartesiana.append(lista_posicoes)

        n =+ 1
    for in range(qtd_cargas):
        lis

    return lista_cargas, lista_posicoes

def calcula_forca_resultante():
    lista_cargas, lista_posicoes = recebe_valores_usuario()

    lista_resposta = []
    # constante de permissividade
    e_const = 8.854 * pow(10, -12)
    k = 1 / (4 * 3.1415 * e_const)

    r12 =

    ans = 'Forca Resultante: {.2e} + {.2e} + {.2e} (N)'lista_resposta[]
def calcula_campo_eletrico():



def main_screen():