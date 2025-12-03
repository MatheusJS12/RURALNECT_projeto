from util import Util
from colorama import Fore, Back, Style, init
from videoaulas import Videoaulas
from informaçoes import Informacoes
from auth import Auth
import visualizar_usuarios
from links_gerais import Links
from forum import Forum
from area_questoes import Questoes
from bibliografia import Bibliografia

init(autoreset=False)

# No código estão algumas sequências de escape que têm a função de colorir o terminal. Por exemplo: \033[33m (transforma o texto em amarelo)


ruralnect_texto = {'texto': 'A RURALNECT é uma plataforma criada para integrar e facilitar o acesso às informações da Universidade Federal Rural de Pernambuco (UFRPE), além de promover a colaboração e o aprendizado entre os estudantes. Por meio do sistema, é possível encontrar fóruns de perguntas e respostas, videoaulas, listasde questões e outros recursos voltados ao desenvolvimento acadêmico e à troca de conhecimento. O projeto também visa tornar a experiência universitária mais interativa e envolvente, com futuras funcionalidades como gamificação e agendamento de cabines de estudo (sala 33, terceiro andar), incentivando o engajamento da comunidade. Em essência, a RURALNECT busca unir informação e educação, servindo como um ponto de conexão entre a universidade e seus estudantes.'}

texto_recortado = ruralnect_texto['texto'].split()

user = Auth()


def menu_inicial():
    while True:
        Util.limpar_tela()
        Util.cabecalho('Menu Inicial')
        print('\nBem-vindo à RURALNECT!')
        print('\nSelecione uma das opções abaixo para avançar:\n')
        Util.txt_opcao('1', 'Cadastro')
        Util.txt_opcao('2', 'Login')
        Util.txt_opcao('3', 'O que é a plataforma RURALNECT?')
        Util.txt_opcao('0', 'Sair do Sistema')


        try:
            opcao = int(input('\nInsira a opção desejada: '))
            condicionais_menu(opcao)
        except ValueError:
            Util.erro_txt('O valor inserido não é um número inteiro, tente novamente!')
            Util.pausa(5)


def condicionais_menu(opcao):
    if opcao == 1:
        Util.limpar_tela()
        print(('Acessando a área de Cadastro...'))
        Util.pausa(2)
        Util.limpar_tela()
        user.cadastro_usuario()

    elif opcao == 2:
        Util.limpar_tela()
        print('Acessando a área de Login...')
        Util.pausa(2)
        user.login(menu_inicial)
        menu_principal(user.usuario_logado)

    elif opcao == 3:
        Util.limpar_tela()
        print('Preparando para exibir informações...')
        Util.pausa(2)
        Util.info_rural(texto_recortado)

    elif opcao == 0:
        Util.limpar_tela()
        print('Saindo do sistema...')
        Util.pausa(3)
        quit()

    else:
        Util.limpar_tela()
        Util.erro_txt('A opção inserida é inválida!')
        Util.pausa(3)
            

def menu_principal(usuario_logado):
    # Tela após o login!
    while True:
        Util.limpar_tela()
        Util.cabecalho('Menu Principal')
        print('usuário: {}'.format(usuario_logado['nome']))
        print('curso: {}'.format(usuario_logado['curso']))
        print('\nSelecione uma das opções abaixo para avançar:')
        Util.txt_opcao('1', 'Fórum de perguntas e respostas')
        Util.txt_opcao('2', 'Lista de questões')
        Util.txt_opcao('3', 'Área de videoaulas')
        Util.txt_opcao('4', 'Área de informações')
        Util.txt_opcao('5', 'Links gerais UFRPE')
        Util.txt_opcao('6', 'Área bibliográfica')
        Util.txt_opcao('7', 'configurações (inoperante)')
        Util.txt_opcao('0', 'Deslogar')

        try:
            op1 = int(input('\nInsira a opção desejada: '))
            condicionais2(op1)
        except ValueError:
            Util.erro_txt('O valor inserido não é um número, tente novamente!')
            Util.pausa(3)
            continue
        
def condicionais2(op1):
    
    if op1 == 1:
        Util.limpar_tela()
        print('Acessando fórum...')
        Util.pausa(3)
        user1 = Forum()
        user1.pergunta_resposta(menu_principal, user.usuario_logado)

    elif op1 == 2:
        Util.limpar_tela()
        print('Acessando Lista de questões...')
        Util.pausa(3)
        user1 = Questoes()
        user1.escolher_questoes(menu_principal, user.usuario_logado)

    elif op1 == 3:
        Util.limpar_tela()
        print('Acessando área de vídeoaulas...')
        Util.pausa(3)
        vid = Videoaulas()
        vid.area_videoaulas(user.usuario_logado)

    elif op1 == 4:
        Util.limpar_tela()
        print('Acssando área de informações...')
        Util.pausa(3)
        info = Informacoes()
        info.area_informacoes(user.usuario_logado)

    elif op1 == 5:
        Util.limpar_tela()
        print('Acessando área de links gerais...')
        Util.pausa(3)
        user1 = Links()
        user1.links_gerais(menu_principal, user.usuario_logado)

    elif op1 == 6:
        Util.limpar_tela()
        print('Acessando área de conteúdos bibliográficos...')
        Util.pausa(3)
        user1 = Bibliografia()
        user1.area_conteudo_bibliografico(menu_principal, user.usuario_logado)
    
    elif op1 == 7:
        Util.limpar_tela()
        print('Acessando configurações...')
        Util.pausa(3)
        Util.erro_txt('O código ainda está sendo implementado!')
        Util.pausa(3)
        return


    elif op1 == 0:
        Util.limpar_tela()
        print('Deslogando...')
        Util.pausa(3)
        menu_inicial()

    else:
        Util.erro_txt('A opção inserida é inválida!')
        Util.pausa(3)
        return


menu_inicial()