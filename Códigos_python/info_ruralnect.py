from util import Util

def info_rural(texto_recortado):
    Util.limpar_tela()
    Util.cabecalho('O que é a plataforma RURALNECT?')
    contador = 0
    texto_junto = ' '.join(texto_recortado)
    for i in texto_junto:
        print(i, end='')
        if len(i) == 1:
            contador = contador + 1
        if contador % 100 == 0:
            print('-\n')
    input('\n\nPressione Enter para continuar...')