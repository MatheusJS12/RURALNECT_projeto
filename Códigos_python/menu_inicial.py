from os import system

# No código estão algumas sequências de escape que têm a função de colorir o terminal. Por exemplo: \033[33m (transforma o texto em amarelo)

def menu_inicial():
    system('cls')
    print('=-' * 50)
    print('{:^105}'.format('\033[34mMenu Inicial\033[m'))
    print('=-' * 50)
    print('\nBem-vindo à RURALNECT!')
    print('\nSelecione uma das opções abaixo para avançar:')
    print('\n\033[1m1\033[m - \033[33mCadastro\033[m') 
    print('\033[1m2\033[m - \033[33mLogin (inacessível)\033[m') 
    print('\033[1m3\033[m - \033[33mO que é a plataforma RURALNECT?\033[m') 
    print('\033[1m0\033[m - \033[33mSair do sistema\033[m\n')
    

menu_inicial()