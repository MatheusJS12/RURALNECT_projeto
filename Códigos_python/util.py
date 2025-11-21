from os import system, name
from time import sleep
from colorama import Fore, Back, Style, init
import webbrowser
import emoji

init(autoreset=True)

class Util:

    def limpar_tela():
        system('cls' if name == 'nt' else 'clear')

    def pausa(tempo):
        sleep(tempo)

    def redirecionador(link):
        webbrowser.open(link)

    def cabecalho(titulo):
        print('=-' * 50)
        print(Fore.YELLOW + '{:^100}'.format(titulo))
        print('=-' * 50)

    def erro_txt(texto):
        print(Fore.LIGHTRED_EX + '{}'.format(texto))

    def txt_certo(texto):
        print(emoji.emojize(Fore.GREEN + '{}:marca_de_seleção_branca:'.format(texto), language='pt'))
    
    def txt_aviso(texto):
        print(emoji.emojize(Fore.LIGHTYELLOW_EX + ':aviso:{}:aviso:'.format(texto), language='pt'))

    def continuar():
        input(Fore.YELLOW + '\nPressione ENTER para continuar' + Fore.RESET)

    def videoaula(assunto, professor, link, sinopse):
        Util.limpar_tela()
        print('Assunto: ' + Fore.YELLOW + '{}\n'.format(assunto))
        print('Professor(a): ' + Fore.YELLOW + '{}\n'.format(professor))
        print('Link do conteúdo: ' + Fore.YELLOW + '{}\n'.format(link))
        print('Sinopse: ' + Fore.YELLOW + '{}\n'.format(sinopse))
        acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
        if acessar == 1:
            Util.redirecionador(link)
        elif acessar == 0:
            Util.limpar_tela()
            return
        else:
            print('A opção escolhida é inexistente!')
            return