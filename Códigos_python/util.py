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
        print(emoji.emojize(Fore.LIGHTRED_EX + '{}:xis:'.format(texto), language='pt'))

    def txt_certo(texto):
        print(emoji.emojize(Fore.GREEN + '{}:marca_de_seleção_branca:'.format(texto), language='pt'))
    
    def txt_aviso(texto):
        print(emoji.emojize(Fore.LIGHTYELLOW_EX + '{}:aviso:'.format(texto), language='pt'))

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
        
    def validacao_nome(nome):
        nome_tam = len(nome)
        if nome_tam < 10:
            Util.erro_txt('Nome completo com caracteres insuficientes')
            Util.pausa(5)
            return False
        if nome.isdigit() or nome == '':
            Util.erro_txt('Seu nome está vázio ou não contém caracteres alfabéticos!')
            Util.pausa(5)
            return False
        return True
        
    def validacao_curso(curso):
        if curso.isdigit() or curso == '':
            Util.erro_txt('Seu curso está vázio ou não contém caracteres alfabéticos!')
            Util.pausa(5)
            return False
        if curso == 'BSI' or 'SI':
            return 'Bacharelado em Sistemas de Informação'
        elif curso == 'CC' or 'BCC':
            return 'Bacharelado em Ciências da Computação'
        elif curso == 'LC':
            return 'Licenciatura em Computação'
        return True

    def validacao_email(email, usuarios):
        if not email.endswith('@ufrpe.br'):
            Util.limpar_tela()
            Util.erro_txt('Adicione um e-mail institucional válido!')
            Util.pausa(5)
            return False
        for usuario in usuarios:
            if email == usuario['email']:
                Util.erro_txt('Este e-mail já está cadastrado!')
                Util.pausa(5)
                return False
        return True
    
    def validacao_senha(senha):
        senha_tam = len(senha)
        if senha_tam < 6 or senha_tam > 20:
            Util.erro_txt('A senha não possui a quantidade mínima de 6 caracteres ou excedeu a quantidade máxima de 20!')
            Util.pausa(5)
            return False
        if not any(chr.isnumeric() for chr in senha):
            Util.erro_txt('Sua senha não possui pelo menos um número')
            Util.pausa(5)
            return False
        if not any(chr.isupper() for chr in senha):
            Util.erro_txt('Sua senha não possui pelo menos uma letra maiúscula')
            Util.pausa(5)
            return False
        elif ' ' in senha:
            Util.erro_txt('A sua senha possui espaços, remova-os!')
            Util.pausa(5)
            return False
        return True
    
    def info_rural(texto_recortado):
        Util.limpar_tela()
        Util.cabecalho('O que é a plataforma RURALNECT?')
        contador = 0
        texto_junto = ' '.join(texto_recortado)
        for letra in texto_junto:
            print(letra, end='')
            contador = contador + 1
            if contador % 100 == 0:
                print('-\n')
        Util.continuar()

    def txt_opcao(num, txt):
        print(Style.BRIGHT + '{} - '.format(num) + Style.NORMAL + Fore.YELLOW + '{}'.format(txt))

    def area_links(dicionario, menu):
        Util.cabecalho('Redes Sociais')
        print(Fore.LIGHTCYAN_EX + '\nInstagram')
        print('=' * 70)
        for i, item in enumerate(dicionario):
            print('{}.'.format(i + 1))
            print('nome: ' + Fore.LIGHTYELLOW_EX + '{}'.format(item['nome']))
            print('link: ' + Fore.LIGHTYELLOW_EX + '{}'.format(item['link']))
            print('=' * 70)
            
        redirecionar = str(input('Deseja ser redirecionado para algum link? (s/n)').strip().lower())
        if redirecionar == 's':
            try:
                opcao1 = int(input('Insira o valor correspondente ao link que deseja acessar: ').strip())
            except ValueError:
                Util.erro_txt('O valor inserido não é um número inteiro, tente novamente!')
                Util.pausa(3)
                return menu()
            Util.redirecionador(dicionario[opcao1 - 1]['link'])

        elif redirecionar == 'n':
            Util.txt_aviso('Voltando para a área de links gerais')
            Util.pausa(3)
            return menu()
        else:
            Util.erro_txt('A opção escolhida é inexistente!')
            Util.pausa(3)
            return menu()