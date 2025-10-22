from util import limpar_tela
from time import sleep


def cadastro_usuario(usuarios):
    print('=-' * 50)
    print('{:^105}'.format('\033[34mMenu Cadastro\033[m'))
    print('=-' * 50)
    nome = str(input('\nInsira o seu nome completo: ').strip().upper())
    nome_tam = len(nome)
    if nome_tam < 10:
        print('Nome completo com caracteres insuficientes')
        sleep(5)
        return
    if nome.isdigit() or nome == '':
       print('\033[31mSeu nome está vázio ou não contém caracteres alfabéticos!\033[m\n')
       sleep(5)
       return
    curso = str(input('Insira as iniciais do seu curso: ').strip().upper())
    if curso.isdigit() or curso == '':
        print('\033[31mSeu curso está vázio ou não contém caracteres alfabéticos!\033[m\n')
        sleep(5)
        return
    if curso == 'BSI' or 'SI':
        curso = 'Bacharelado em Sistemas de Informação'
    elif curso == 'CC' or 'BCC':
        curso = 'Bacharelado em Ciências da Computação'
    elif curso == 'LC':
        curso = 'Licenciatura em Computação'
    email = str(input('Insira o seu e-mail institucional: ').strip().lower())
    if '@ufrpe.br' not in email:
        limpar_tela()
        print('\033[31mAdicione um e-mail institucional válido!\033[m\n')
        sleep(5)
        return
    for usuario in usuarios:
        if email == usuario['email']:
            print('\033[31mEste e-mail já está cadastrado!\033[m\n')
            sleep(5)
            return
    senha = str(input('Insira uma senha forte: ').strip())
    senha_tam = len(senha)
    if senha_tam < 6 or senha_tam > 20:
        print('\033[31mA senha não possui a quantidade mínima de 6 caracteres ou excedeu a quantidade máxima de 20!\033[m\n')
        sleep(5)
        return
    if not any(chr.isnumeric() for chr in senha):
        print('Sua senha não possui pelo menos um número')
        sleep(5)
        return
    if not any(chr.isupper() for chr in senha):
        print('Sua senha não possui pelo menos uma letra maiúscula')
        sleep(5)
        return
    elif ' ' in senha:
        print('\033[31mA sua senha possui espaços, remova-os!\033[m\n')
        sleep(5)
        return
    senha_confirm = str(input('Insira a senha novamente para confirmar: ').strip())
    if senha_confirm != senha:
        print('Erro: A senha inserida não corresponde à adicionada anteriormente!')
        sleep(3)
        return

    usuarios.append({'nome': nome, 'curso': curso, 'email': email, 'senha': senha})

    print('\033[32mCadastro realizado com sucesso!\033[m\n')
    input('Pressione Enter para continuar...')
