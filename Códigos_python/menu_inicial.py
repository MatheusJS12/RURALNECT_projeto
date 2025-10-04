from os import system
from time import sleep

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

    opcao = int(input('Insira a opção desejada: '))
    condicionais_menu(opcao)

def condicionais_menu(opcao):
    if opcao == 1:
        system('cls')
        print(('Acessando a área de Cadastro...'))
        sleep(2)
        system('cls')
        cadastro()
    elif opcao == 2:
        system('cls')
        print('Acessando a área de Login...')
        sleep(2)
        # Adicionar a função login.
    elif opcao == 3:
        system('cls')
        print('Preparando para exibir informações...')
        sleep(3)
        # Adicionar a função "ruralnect"
    elif opcao == 0:
        system('cls')
        print('Saindo do sistema...')
        sleep(3)
        quit()
    else:
        system('cls')
        print('A opção inserida é inválida!')
def cadastro():
    print('=-' * 50)
    print('{:^105}'.format('\033[34mMenu Cadastro\033[m'))
    print('=-' * 50)
    nome = str(input('\nInsira o seu nome completo: ').strip().upper())
    if nome.isdigit() or nome == '':
        print('Seu nome está vázio ou não contém caracteres alfabéticos!')
        return

    curso = str(input('Insira as iniciais do seu curso: ').strip())
    email = str(input('Insira o seu e-mail institucional: ').strip())
    if 'ufrpe.br' not in email:
        system('cls')
        print('\033[31mAdicione um e-mail institucional válido!\033[m\n')
        return
    senha = str(input('Insira uma senha forte: ').strip())

    print(nome)
    print(curso)
    print(email)
    print(senha)



menu_inicial()