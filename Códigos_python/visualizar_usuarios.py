from util import limpar_tela
from time import sleep

def visualizar(usuarios):
    if len(usuarios) <= 0:
        print('\033[31mNenhum cadastro encontrado!\033[m\n')
        sleep(5)
        return
    else:
        print('Nome: {}'.format(usuarios[len(usuarios) - 1]['nome']))
        if usuarios[len(usuarios) - 1]['nome'] == '':
            print('\033[31mNome está vazio!\033[m\n')
            sleep(5)
            return
        print('Curso: {}'.format(usuarios[len(usuarios) - 1]['curso']))
        print('e-mail: {}'.format(usuarios[len(usuarios) - 1]['email']))
        print('senha: {}'.format(usuarios[len(usuarios) - 1]['senha']))

        input('Pressione Enter para continuar!')

        limpar_tela()