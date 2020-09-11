# Python 3.7
# by Jadson Marliere de Oliveira
# Este projeto possui fins academicos - Disciplina ELETROMAGNETISMO

# precisa de instalar o pacote numpy
import numpy as np

def valores_fonte_test():
    # As cargas devem estar em notacao cientifica
    q1 = 10 * pow(10, -9)
    q2 = 2 * pow(10, -9)
    q3 = 3 * pow(10, -9)

    posicoes_q1 = [2, 2, 8]
    posicoes_q2 = [2, -3, 5]
    posicoes_q3 = [-2, 5, 8]

    lista_cargas = np.array([q1, q2, q3])
    lista_posicoes = np.array([posicoes_q1, posicoes_q2, posicoes_q3])

    return lista_cargas, lista_posicoes

def calcula_modulo(posicoes):
    modulo_posicoes = pow((pow(posicoes[0], 2) + pow(posicoes[1], 2) + pow(posicoes[2], 2)), 1/2)

    return modulo_posicoes

def recebe_valores_usuario():
    qtd_cargas  = input('Digite a quantidade de cargas: ')
    lista_cargas = []
    lista_cartesiana = []

    n = 1
    print(' Digite primeiramente a carga de prova :')

    for elem in range(qtd_cargas):
        # recebe valor da carga
        lista_cargas.append(input('Digite a {} carga'.format(n)))

        # recebe coordenadas do espaco:
        lista_posicoes = []
        print('Adicione apenas as magnitudes de ax + ay + az, espaco(x, y, z): ')
        lista_posicoes.append('digite a posicao no eixo X: ')
        lista_posicoes.append('digite a posicao no eixo Y: ')
        lista_posicoes.append('digite a posicao no eixo Z: ')

        # adicona coodenadas no array de posicoes
        lista_cartesiana.append(lista_posicoes)

        n += 1

    return lista_cargas, lista_cartesiana

def calcula_forca_resultante():
    lista_cargas, lista_cartesiana = valores_fonte_test()
    lista_r = []
    lista_resposta = []

    # constante de permissividade
    e_const = 8.854 * pow(10, -12)
    k = 1 / (4 * 3.1415 * e_const)

    # faz o subcalculo de r
    n = 1
    for sub_list in range(len(lista_cartesiana)-1):
        lista_r.append((lista_cartesiana[0] - lista_cartesiana[n]))
        n += 1

    print(lista_r)
    ans = 'Forca Resultante: {.2e} + {.2e} + {.2e} (N)'.format(lista_resposta)
    print(ans)

    return ans


# def calcula_campo_eletrico():


def main_screen():

    print('1 - Calculo F Resultante: ')


main_screen()
calcula_forca_resultante()