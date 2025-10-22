from util import limpar_tela

def info_rural(texto_recortado):
    limpar_tela()
    print('=-' * 50)
    print('{:^105}'.format('\033[34mO que é a plataforma RURALNECT?\033[m'))
    print('=-' * 50)
    contador = 0
    texto_junto = ' '.join(texto_recortado)
    for i in texto_junto:
        print(i, end='')
        if len(i) == 1:
            contador = contador + 1
        if contador % 100 == 0:
            print('-\n')
    input('\n\nPressione Enter para continuar...')