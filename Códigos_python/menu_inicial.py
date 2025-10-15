from os import system, name
from time import sleep
# No código estão algumas sequências de escape que têm a função de colorir o terminal. Por exemplo: \033[33m (transforma o texto em amarelo)

usuarios = []
usuario_logado = {'nome': '', 'curso': ''}

ruralnect_texto = {'texto': 'A RURALNECT é uma plataforma criada para integrar e facilitar o acesso às informações da Universidade Federal Rural de Pernambuco (UFRPE), além de promover a colaboração e o aprendizado entre os estudantes. Por meio do sistema, é possível encontrar fóruns de perguntas e respostas, videoaulas, listasde questões e outros recursos voltados ao desenvolvimento acadêmico e à troca de conhecimento. O projeto também visa tornar a experiência universitária mais interativa e envolvente, com futuras funcionalidades como gamificação e agendamento de cabines de estudo (sala 33, terceiro andar), incentivando o engajamento da comunidade. Em essência, a RURALNECT busca unir informação e educação, servindo como um ponto de conexão entre a universidade e seus estudantes.'}

texto_recortado = ruralnect_texto['texto'].split()


def menu_inicial():
    while True:
        limpar_tela()
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

        try:
            opcao = int(input('Insira a opção desejada: '))
            condicionais_menu(opcao)
        except ValueError:
            print('O valor inserido não é um número, tente novamente!')
            sleep(5)


def condicionais_menu(opcao):
    if opcao == 1:
        limpar_tela()
        print(('Acessando a área de Cadastro...'))
        sleep(2)
        limpar_tela()
        cadastro()
    elif opcao == 2:
        limpar_tela()
        print('Acessando a área de Login...')
        sleep(2)
        login(usuarios)
        menu_principal(usuario_logado)
    elif opcao == 3:
        limpar_tela()
        print('Preparando para exibir informações...')
        sleep(2)
        info_rural()
    elif opcao == 4:
        limpar_tela()
        print('Acessando a área de visualização de informações...')
        sleep(2)
        visualizar(usuarios)

    elif opcao == 0:
        limpar_tela()
        print('Saindo do sistema...')
        sleep(3)
        quit()
    else:
        limpar_tela()
        print('A opção inserida é inválida!')
def cadastro():
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
    for u in usuarios:
        if email == u['email']:
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
        return

    usuarios.append({'nome': nome, 'curso': curso, 'email': email, 'senha': senha})

    print('Cadastro realizado com sucesso!\n')
    input('Pressione Enter para continuar...')
    
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
def info_rural():
    print('=-' * 50)
    print('{:^105}'.format('\033[34mO que é a plataforma RURALNECT?\033[m'))
    print('=-' * 50)
    contador = 0
    texto_junto = ' '.join(texto_recortado)
    for i in texto_junto:
        print(i[0][0:100], end='')
        if len(i) == 1:
            contador = contador + 1
        if contador % 100 == 0:
            print('-\n')
    input('\n\nPressione Enter para continuar...')

def login(usuarios):
    print('=-' * 50)
    print('{:^105}'.format('\033[34mMenu Login\033[m'))
    print('=-' * 50)

    rest_senha = 0
    cont = 3
    
    while rest_senha != '1':
        usuario = str(input('Insira o e-mail: ').strip().lower())
        senha_user = str(input('Insira a senha: ').strip())
        for u in usuarios:
            if cont == 0:
                print('A quantidade de tentativas de login superou o limite de 3 chances, tente novamente mais tarde!')
                sleep(5)
                limpar_tela()
                rest_senha = int(input('Deseja ir para a área de recuperação de senha? (1 - S/0 - N)').strip().lower())
                if rest_senha == 1:
                    recuperar_senha(usuarios)
                elif rest_senha == 0:
                    print('Voltando ao menu inicial...')
                    sleep(3)
                    return
            if usuario == u['email'] and senha_user == u['senha']:
                print('Bem-vindo, {}'.format(u['nome']))
                usuario_logado['nome'] = u['nome']
                usuario_logado['curso'] = u['curso']
                return
            elif usuario == u['email'] and senha_user != u['senha'] or usuario != u['email'] and senha_user == u['senha'] or usuario != u['email'] and senha_user != u['senha']:
                print('Login não-sucedido, tente novamente!')
                print('chances restantes')
                cont = cont - 1
            
            print('E-mail e/ou senha incorretos, adicione novamente!')
        sleep(5)
def recuperar_senha(usuarios):
    limpar_tela()
    print('=-' * 50)
    print('{:^105}'.format('\033[34mRecuperação de senha\033[m'))
    print('=-' * 50)
    print('\nPara efetuar a recuperação de senha, você deverá inserir o e-mail e o código que será enviado!\n')
    email = str(input('Insira o e-mail: ').strip().lower())
    for u in usuarios:
        if email == u['email']:
            # Adicionar a parte do email
            print('Código enviado!')
            print('Caso não encontre na caixa principal, veja na caixa de spam.')

def menu_principal(usuario_logado):
    # Tela após o login!
    limpar_tela()
    print('=-' * 50)
    print('{:^105}'.format('\033[34mMenu Principal\033[m'))
    print('=-' * 50)
    print('usuário: {}'.format(usuario_logado['nome']))
    print('curso: {}'.format(usuario_logado['curso']))
    print('\nSelecione uma das opções abaixo para avançar:\n1 - Área de video-aulas\n2 - Área de informações\n3 - Em desenvolvimento\n4 - Em desenvolvimento\n5 - Em desenvolvimento\n')
    try:
        op1 = int(input('Insira a opção desejada: '))
    except ValueError:
        print('O valor inserido não é um número, tente novamente!')
        return

def limpar_tela():
    system('cls' if name == 'nt' else 'clear')

menu_inicial()