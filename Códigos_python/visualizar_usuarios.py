from util import Util

def visualizar(usuarios):
    Util.limpar_tela()
    if len(usuarios) <= 0:
        Util.erro_txt('Nenhum cadastro encontrado!')
        Util.pausa(5)
        return
    else:
        print('Nome: {}'.format(usuarios[len(usuarios) - 1]['nome']))
        print('\nCurso: {}'.format(usuarios[len(usuarios) - 1]['curso']))
        print('\ne-mail: {}'.format(usuarios[len(usuarios) - 1]['email']))
        print('\nsenha: {}'.format(usuarios[len(usuarios) - 1]['senha']))

        Util.continuar()

        Util.limpar_tela()