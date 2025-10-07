from os import system
from time import sleep

# No código estão algumas sequências de escape que têm a função de colorir o terminal. Por exemplo: \033[33m (transforma o texto em amarelo)

usuarios = {'nome': '',
            'email': '',
            'curso': '',
            'senha': ''}

def menu_inicial():
    while True:
        system('cls')
        print('=-' * 50)
        print('{:^105}'.format('\033[34mMenu Inicial\033[m'))
        print('=-' * 50)
        print('\nBem-vindo à RURALNECT!')
        print('\nSelecione uma das opções abaixo para avançar:')
        print('\n\033[1m1\033[m - \033[33mCadastro\033[m') 
        print('\033[1m2\033[m - \033[33mLogin (inacessível)\033[m') 
        print('\033[1m3\033[m - \033[33mO que é a plataforma RURALNECT?\033[m')
        print('\033[1m4\033[m - \033[33mVisualizar o cadastro\033[m')
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
    elif opcao == 4:
        system('cls')
        print('Acessando a área de visualização de informações...')
        sleep(2)
        visualizar(usuarios)

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
    curso = str(input('Insira as iniciais do seu curso: ').strip().upper())
    email = str(input('Insira o seu e-mail institucional: ').strip().lower())
    if '@ufrpe.br' not in email:
        system('cls')
        print('\033[31mAdicione um e-mail institucional válido!\033[m\n')
        return
    senha = str(input('Insira uma senha forte: ').strip())
    senha_tam = len(senha)
    if senha_tam < 6:
        print('A senha não apresenta quantidade mínima de caracteres!')
        sleep(3)
        return
    elif ' ' in senha:
        print('A sua senha possui espaços, remova-os!')
        return
    usuarios['senha'] = senha
    usuarios['curso'] = curso
    usuarios['email'] = email
    usuarios['nome'] = nome
    
    input('Pressione Enter para continuar...')
    

def visualizar(usuarios):
    print('Nome: {}'.format(usuarios['nome']))
    if usuarios['nome'] == '':
        print('Nome está vazio!')
        return
    print('Curso: {}'.format(usuarios['curso']))
    print('e-mail: {}'.format(usuarios['email']))
    print('senha: {}'.format(usuarios['senha']))

    input('Pressione Enter para continuar!')

    system('cls')

menu_inicial()