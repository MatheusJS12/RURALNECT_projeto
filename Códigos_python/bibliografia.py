from util import Util
from colorama import Fore, Back, Style, init

init(autoreset=False)

class Bibliografia:
    def __init__(self):
        
        self.conteudos_bsi = [
            {
                'cadeira': 'Fundamentos Matemáticos para Sistemas de Informação',
                'conteudos': [
                    'https://www.dropbox.com/scl/fi/u0w10442k7jqk7oiw11ca/matematica-discreta-e-suas-aplicaoes_compress.pdf?rlkey=318swfqsiii7wtnbv3nl8plup&st=2h550a2a&dl=0', 
                ]
            },
            {
                'cadeira': 'Introdução à Administração',
                'conteudos': [
                    'https://www.dropbox.com/scl/fo/a3h7swy6fzp0e4fec7h8o/AOFbhdxD4XzxUiT6Ab4sbpM?rlkey=o996v7g154h8pfqg0x0u0mdiq&st=z9lx4iwu&dl=0'
                ]
            },
            {
                'cadeira': 'Princípios de Programação para Sistemas de Informação',
                'conteudos': [
                    'https://www.dropbox.com/scl/fo/c4f905gdrtck3c1wud12j/AK53A8D79lqIdJxWMYqJKT8?rlkey=c8w3f6kznfgyixltroh4hhdvh&st=a645icaq&dl=0'
                ] 
            }
        ]
        self.conteudos_bcc = [
            {
                'cadeira': 'adicionar algo',
                'conteudos': [

                ]
            }
        ]
        self.conteudos_lc = [
            {
                'cadeira': 'adicionar algo',
                'conteudos': []
            }
        ]
    def area_conteudo_bibliografico(self, menu_principal, usuario_logado):
        while True:
            Util.limpar_tela()
            Util.cabecalho('Área de conteúdo bibliográfico')
            if usuario_logado['curso'] == 'Bacharelado em Sistemas de Informação':
                self.bloco_conteudo_bibliografico(self.conteudos_bsi, menu_principal, usuario_logado)

            elif usuario_logado['curso'] == 'Bacharelado em Ciências da Computação':
                self.bloco_conteudo_bibliografico(self.conteudos_bcc, menu_principal, usuario_logado)

            elif usuario_logado['curso'] == 'Licenciatura em Computação':
                self.bloco_conteudo_bibliografico(self.conteudos_lc, menu_principal, usuario_logado)
            
    def bloco_conteudo_bibliografico(self, conteudinho, menu_principal, usuario_logado):
        for i, item in enumerate(conteudinho):
            Util.txt_opcao(i + 1, item["cadeira"])

        Util.txt_opcao('0', 'Menu Principal')
        try:
            opcao = int(input('\nDigite o número da cadeira: '))

        except ValueError:
            Util.erro_txt('O valor inserido não é um número inteiro, tente novamente!')
            Util.pausa(3)
            return

        if opcao == '':
            Util.erro_txt('O campo está vazio, digite a opção desejada')
            return
    
        Util.limpar_tela()
        if 1 <= opcao <= len(conteudinho):
            cadeira = conteudinho[opcao - 1]
            Util.cabecalho(cadeira["cadeira"])
            for u, conteudo in enumerate(cadeira['conteudos']):
                print('{}. {}'.format(u + 1, conteudo))

            redirecionador = str(input(Fore.LIGHTYELLOW_EX + '\nDeseja ser redirecionado para alguma conteúdo (s/n)?: ' + Fore.RESET).strip().lower())

            if redirecionador == 's':
                num_conteudo = int(input('Insira o número do conteúdo desejado: '))
                Util.redirecionador(cadeira['conteudos'][num_conteudo - 1])

            elif redirecionador == 'n':
                Util.txt_aviso('Voltando para a área bibliográfica')
                Util.pausa(3)
                return 
            
            else:
                Util.erro_txt('A opção escolhida é inexistente!')
                Util.pausa(3)
        elif opcao == 0:
            Util.txt_aviso('Retornando ao Menu Principal')
            Util.pausa(3)
            menu_principal(usuario_logado)
                                        
        else:
            Util.erro_txt('Insira uma opção válida')
            return