from util import limpar_tela
from time import sleep
import videoaulas
import esqueci_minhasenha
import informaçoes
import cadastro
import login
import visualizar_usuarios
import info_ruralnect

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
        print('\033[1m2\033[m - \033[33mLogin\033[m') 
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
        cadastro.cadastro_usuario(usuarios)
    elif opcao == 2:
        limpar_tela()
        print('Acessando a área de Login...')
        sleep(2)
        login.login(usuarios, menu_inicial, usuario_logado)
        menu_principal(usuario_logado)
    elif opcao == 3:
        limpar_tela()
        print('Preparando para exibir informações...')
        sleep(2)
        info_ruralnect.info_rural(texto_recortado)
    elif opcao == 4:
        limpar_tela()
        print('Acessando a área de visualização de informações...')
        sleep(2)
        visualizar_usuarios.visualizar(usuarios)

    elif opcao == 0:
        limpar_tela()
        print('Saindo do sistema...')
        sleep(3)
        quit()
    else:
        limpar_tela()
        print('A opção inserida é inválida!')
            

def menu_principal(usuario_logado):
    # Tela após o login!
    while True:
        limpar_tela()
        print('=-' * 50)
        print('{:^105}'.format('\033[34mMenu Principal\033[m'))
        print('=-' * 50)
        print('usuário: {}'.format(usuario_logado['nome']))
        print('curso: {}'.format(usuario_logado['curso']))
        print('\nSelecione uma das opções abaixo para avançar:')
        print('\n\033[1m1\033[m - \033[33mFórum de perguntas e respostas\033[m') 
        print('\033[1m2\033[m - \033[33mLista de questões\033[m') 
        print('\033[1m3\033[m - \033[33mÁrea de videoaulas\033[m')
        print('\033[1m4\033[m - \033[33mÁrea de informações\033[m')
        print('\033[1m5\033[m - \033[33mLinks Gerais UFRPE\033[m\n')
        print('\033[1m6\033[m - \033[33mÁrea bibliográfica\033[m\n')
        print('\033[1m0\033[m - \033[33mDeslogar\033[m\n')
        try:
            op1 = int(input('Insira a opção desejada: '))
            condicionais2(op1)
        except ValueError:
            print('O valor inserido não é um número, tente novamente!')
            return
def condicionais2(op1):
    if op1 == 1:
        limpar_tela()
        print('Acessando fórum...')
        sleep(3)
        # Área do Fórum
    elif op1 == 2:
        limpar_tela()
        print('Acessando Lista de questões...')
        sleep(3)
        # Área da lista
    elif op1 == 3:
        limpar_tela()
        print('Acessando área de vídeoaulas...')
        sleep(3)
        videoaulas.area_videoaulas(usuario_logado)
    elif op1 == 4:
        limpar_tela()
        print('Acssando área de informações...')
        sleep(3)
        informaçoes.area_informacoes(usuario_logado)
    elif op1 == 5:
        limpar_tela()
        print('Acessando área de links gerais...')
        sleep(3)
    elif op1 == 0:
        limpar_tela()
        print('Deslogando...')
        sleep(3)
        menu_inicial()
    else:
        print('A opção inserida é inválida!')


menu_inicial()