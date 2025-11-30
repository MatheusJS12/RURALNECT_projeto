from util import Util
from colorama import Fore, Back, Style, init

init(autoreset=True)

class Questoes:
    def __init__(self):
        self.lista_perguntas_bsi = [{
            'cadeira': 'Fundamentos Matemáticos para Sistemas de Informação',
            'listas de questões': [{
                'assunto': 'grafo',
                'link':'https://forms.gle/BwoDbQMZriv7No1w6'
        }]
        }]
        self.lista_perguntas_bcc = [{
            'cadeira': 'adicionar algo',
            'listas de questões': []
        }]
        self.lista_perguntas_lc = [{
            'cadeira': 'adicionar algo',
            'listas de questões': []
        }]
    
    def escolher_questoes(self, menu_principal, usuario_logado):
        Util.limpar_tela()
        Util.cabecalho('Listas de Questões')
        # if not self.nome_da_lista:
        print('Selecione uma das opções a seguir:')
        for i, lista in enumerate(self.lista_perguntas_bsi):
            Util.txt_opcao(i + 1, lista['cadeira'])
        Util.txt_opcao('0', 'Menu Principal')
        
        try:
            lista_selecao = int(input(Fore.LIGHTYELLOW_EX + '\nInsira o valor da lista desejada: ' + Fore.RESET))
            cadeira = self.lista_perguntas_bsi[lista_selecao - 1]
            if lista_selecao == 0:
                Util.txt_aviso('Retornando ao Menu Principal')
                Util.pausa(3)
                return menu_principal(usuario_logado)
            elif lista_selecao < 0 or lista_selecao > len(self.lista_perguntas_bsi):
                Util.erro_txt('Opção inválida!')
                Util.pausa(3)
                return

        except ValueError:
            Util.erro_txt('O valor inserido não é um número inteiro, tente novamente!')
            Util.pausa(3)
            return
        
        Util.limpar_tela()
        Util.cabecalho(cadeira['cadeira'])
        print('')
        print('=' * 70)
        for u, questao in enumerate(cadeira['listas de questões']):
            print(Fore.LIGHTYELLOW_EX + '{}'.format(u + 1) + Fore.RESET + '.')
            print('Assunto: ' + Fore.LIGHTYELLOW_EX + '{}'.format(questao['assunto'] + Fore.RESET))
            print('link: ' + Fore.LIGHTYELLOW_EX + '{}'.format(questao['link'] + Fore.RESET))
            print('=' * 70)
        
        redirecionador = str(input(Fore.LIGHTYELLOW_EX + '\nDeseja ser redirecionado para alguma conteúdo (s/n)?: ' + Fore.RESET).strip().lower())

        if redirecionador == 's':
            num_conteudo = int(input('Insira o número da lista desejadada: '))
            Util.redirecionador(cadeira['listas de questões'][num_conteudo - 1]['link'])

        elif redirecionador == 'n':
            Util.txt_aviso('Voltando para a escolha da cadeira')
            Util.pausa(3)
            return
        
        else:
            Util.erro_txt('A opção escolhida é inexistente!')
            Util.pausa(3)
            return