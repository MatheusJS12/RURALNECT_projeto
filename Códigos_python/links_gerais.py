from util import Util
from colorama import Fore, Back, Style, init

init(autoreset=True)

class Links:
    def __init__(self):
        self.redes_sociais_instagram = [{"nome": "UFRPE (institucional)", "link": "https://www.instagram.com/ufrpe/"},
    {"nome": "PRPG - Pró-Reitoria de Pós-Graduação", "link": "https://www.instagram.com/prpg.ufrpe/"},
    {"nome": "UAEADTEC - Educação a Distância / Tecnologia", "link": "https://www.instagram.com/uaeadtecufrpe/"},
    {"nome": "Ouvidoria UFRPE", "link": "https://www.instagram.com/ouvidoria.ufrpe/"},
    {"nome": "PROGEPE - Pró-Reitoria de Gestão de Pessoas", "link": "https://www.instagram.com/progepeufrpe/"},
    {"nome": "UABJ - Unidade Acadêmica de Belo Jardim", "link": "https://www.instagram.com/uabj.ufrpe/"},
    {"nome": "UAST - Unidade Acadêmica de Serra Talhada", "link": "https://www.instagram.com/uast.ufrpe/"},
    {"nome": "UACSA - Unidade Acadêmica do Cabo de Santo Agostinho", "link": "https://www.instagram.com/uacsaufrpe/"},
    {"nome": "PROGESTIRU - Restaurante Universitário (perfil oficial)", "link": "https://www.instagram.com/progestiru/"},
    ]
        self.sites_oficiais_ufrpe = [
    {"nome": "UFRPE (institucional)", "link": "https://www.ufrpe.br"},
    {"nome": "UFRPE Digital", "link": "https://digital.ufrpe.br"},
    {"nome": "UFRPE ID", "link": "https://id.digital.ufrpe.br/login"},
    {"nome": "Portal de Ajuda UFRPE", "link": "https://ajuda.ufrpe.br"},
    {"nome": "SIGAA / SIGS", "link": "https://sigs.ufrpe.br"},
    {"nome": "Repositório Arandu", "link": "https://arandu.ufrpe.br"},
    {"nome": "Portal NUPESQ", "link": "https://nupesq.ufrpe.br"},
    {"nome": "Portal de Seleção", "link": "https://selecao.ufrpe.br"},
    {"nome": "Página do Ingressante", "link": "https://ingressante.ufrpe.br"},
    {"nome": "Central de Serviços Digitais", "link": "https://servicosdigitais.ufrpe.br"}
]
        self.sites_independentes_funcionando = [
    {
        "nome": "BSI UFRPE (Sistemas de Informação)",
        "link": "https://sites.google.com/view/bsi-ufrpe/home"
    },
    {
        "nome": "Administração UAST (blog estudantil)",
        "link": "https://admufrpeuast.wordpress.com"
    }
]


    def links_gerais(self, menu_principal, usuario_logado):
        while True:
            Util.limpar_tela()
            Util.cabecalho('Links Gerais')
            print('\nInsira uma das opções de links abaixo:\n')
            Util.txt_opcao('1', 'Redes sociais')
            Util.txt_opcao('2', 'Sites Oficiais')
            Util.txt_opcao('3', 'Sites independentes (feitos por estudantes)')
            Util.txt_opcao('0', 'Voltar ao Menu Principal\n')
            try:
                opcao = int(input('Insira a opção desejada: '))
                self.condicionais(opcao, menu_principal, usuario_logado)
                
            except ValueError:
                Util.erro_txt('O valor inserido não é um número inteiro, tente novamente!')
                Util.pausa(3)
                return self.links_gerais(menu_principal, usuario_logado)
            
    def condicionais(self, opcao, menu_principal, usuario_logado):
        Util.limpar_tela()
        if opcao == 1:
            Util.area_links(self.redes_sociais_instagram, lambda: self.links_gerais(menu_principal, usuario_logado))

        elif opcao == 2:
            Util.area_links(self.sites_oficiais_ufrpe, lambda: self.links_gerais(menu_principal, usuario_logado))

        elif opcao == 3:
            Util.area_links(self.sites_independentes_funcionando, lambda: self.links_gerais(menu_principal, usuario_logado))

        elif opcao == 0:
            Util.txt_aviso('Voltando ao Menu Principal')
            Util.pausa(3)
            return menu_principal(usuario_logado)