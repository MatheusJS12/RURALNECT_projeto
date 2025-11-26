from util import Util
from colorama import Fore, Back, Style, init
import videoaulas
import esqueci_minhasenha
import informaçoes
from auth import Auth
import login
import visualizar_usuarios
import info_ruralnect
from links_gerais import Links

init(autoreset=True)

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
        print(Style.BRIGHT + '1 - ' + Style.NORMAL + Fore.YELLOW + 'Cadastro') 
        print(Style.BRIGHT + '2 - ' + Style.NORMAL + Fore.YELLOW + 'Login') 
        print(Style.BRIGHT + '3 - ' + Style.NORMAL + Fore.YELLOW + 'O que é a plataforma RURALNECT?') 
        print(Style.BRIGHT + '4 - ' + Style.NORMAL + Fore.YELLOW + 'Visualizar o cadastro') 
        print(Style.BRIGHT + '0 - ' + Style.NORMAL + Fore.YELLOW + 'Sair do Sistema\n') 

        try:
            opcao = int(input('Insira a opção desejada: '))
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
    elif opcao == 4:
        Util.limpar_tela()
        print('Acessando a área de visualização de informações...')
        Util.pausa(2)
        visualizar_usuarios.visualizar(user.usuarios)

    elif opcao == 0:
        Util.limpar_tela()
        print('Saindo do sistema...')
        Util.pausa(3)
        quit()
    else:
        Util.limpar_tela()
        print('A opção inserida é inválida!')
            

def menu_principal(usuario_logado):
    # Tela após o login!
    while True:
        Util.limpar_tela()
        Util.cabecalho('Menu Principal')
        print('usuário: {}'.format(usuario_logado['nome']))
        print('curso: {}'.format(usuario_logado['curso']))
        print('\nSelecione uma das opções abaixo para avançar:')
        print(Style.BRIGHT + '1 - ' + Style.NORMAL + Fore.YELLOW + 'Fórum de perguntas e respostas') 
        print(Style.BRIGHT + '2 - ' + Style.NORMAL + Fore.YELLOW + 'Lista de questões')
        print(Style.BRIGHT + '3 - ' + Style.NORMAL + Fore.YELLOW + 'Área de videoaulas') 
        print(Style.BRIGHT + '4 - ' + Style.NORMAL + Fore.YELLOW + 'Área de informações') 
        print(Style.BRIGHT + '5 - ' + Style.NORMAL + Fore.YELLOW + 'Links gerais UFRPE') 
        print(Style.BRIGHT + '6 - ' + Style.NORMAL + Fore.YELLOW + 'Área bibliográfica')
        print(Style.BRIGHT + '0 - ' + Style.NORMAL + Fore.YELLOW + 'Deslogar') 
        try:
            op1 = int(input('Insira a opção desejada: '))
            condicionais2(op1)
        except ValueError:
            print('O valor inserido não é um número, tente novamente!')
            return
def condicionais2(op1):
    if op1 == 1:
        Util.limpar_tela()
        print('Acessando fórum...')
        Util.pausa(3)
        # Área do Fórum
    elif op1 == 2:
        Util.limpar_tela()
        print('Acessando Lista de questões...')
        Util.pausa(3)
        # Área da lista
    elif op1 == 3:
        Util.limpar_tela()
        print('Acessando área de vídeoaulas...')
        Util.pausa(3)
        videoaulas.area_videoaulas(user.usuario_logado)
    elif op1 == 4:
        Util.limpar_tela()
        print('Acssando área de informações...')
        Util.pausa(3)
        informaçoes.area_informacoes(user.usuario_logado)
    elif op1 == 5:
        Util.limpar_tela()
        print('Acessando área de links gerais...')
        Util.pausa(3)
        user1 = Links()
        user1.links_gerais(menu_principal, user.usuario_logado)
    elif op1 == 0:
        Util.limpar_tela()
        print('Deslogando...')
        Util.pausa(3)
        menu_inicial()
    else:
        Util.erro_txt('A opção inserida é inválida!')


menu_inicial()