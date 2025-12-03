from util import Util
from colorama import Fore, Back, Style, init

init(autoreset=False)

class Forum:
    def __init__(self):
        self.perguntas = []

    def pergunta_resposta(self, menu_principal, usuario_logado):
        while True:
            Util.limpar_tela()
            Util.cabecalho('Fórum')
            print('\nInsira uma das opções abaixo:\n')
            Util.txt_opcao('1', 'Fazer pergunta')
            Util.txt_opcao('2', 'Postar resposta')
            Util.txt_opcao('3', 'Visualizar perguntas e respostas')
            Util.txt_opcao('0', 'Voltar ao Menu Principal\n')
            try:
                opcao = int(input('Insira a opção desejada: '))
                self.condicionais(opcao, menu_principal, usuario_logado)
                
            except ValueError:
                Util.erro_txt('O valor inserido não é um número inteiro, tente novamente!')
                Util.pausa(3)
                return
            
    def condicionais(self, opcao, menu_principal, usuario_logado):
        Util.limpar_tela()
        if opcao == 1:
            Util.cabecalho('Área de perguntas')

            perguntar = str(input('Deseja fazer uma pergunta? (s/n)\n').strip().lower())
            if perguntar == 's':
                Util.limpar_tela()
                Util.cabecalho('Área de perguntas')

                pergunta = str(input(Fore.LIGHTCYAN_EX + 'Pergunta (deve conter, no mínimo, 10 caracteres e, no máximo, 500): ' + Fore.RESET).strip().capitalize())
                
                if not pergunta:
                    Util.erro_txt('O campo está vazio, preencha-o!')
                    Util.pausa(3)
                    return
                
                if len(pergunta) < 10 or len(pergunta) > 500:
                    Util.erro_txt('Sua pergunta ou não atinge a quantidade mínima de caracteres ou ultrapassa o limite!')
                    Util.pausa(3)
                    return
                
                if not any(char.isalpha() for char in pergunta):
                    Util.erro_txt('Sua pergunta precisa conter caracteres alfabéticos!')
                    Util.pausa(3)
                    return
                
                self.perguntas.append({'pergunta': pergunta, 'respostas': []})

                Util.txt_certo('Pergunta cadastrada com sucesso!')
                Util.continuar()
                
            elif perguntar == 'n':
                Util.txt_aviso('Voltando para o Menu Pruncipal!')
                Util.pausa(3)
                return menu_principal(usuario_logado)
            
            else:
                Util.erro_txt('A opção escolhida é inexistente!')
                Util.pausa(3)
                return #menu_principal()
            
        elif opcao == 2:
            Util.cabecalho('Área de respostas')

            responder = str(input('Deseja responder a uma pergunta? (s/n)\n').strip().lower())

            if responder == 's':
                Util.limpar_tela()
                if not self.perguntas:
                    Util.erro_txt('Não há perguntas!')
                    Util.pausa(3)
                    return
                for i, item in enumerate(self.perguntas):
                    print(Fore.LIGHTYELLOW_EX + '{}. {}'.format(i + 1, item['pergunta']))
                    for resp in item['respostas']:
                        if not item['respostas']:
                            Util.erro_txt('Esta pergunta ainda não foi respondida!')
                        else:
                            print('     — {}'.format(resp))
                    try:
                        esc_pergunta = int(input(Fore.LIGHTYELLOW_EX + '\nInsira o valor da questão que deseja responder: ' + Fore.RESET))

                    except ValueError:
                        Util.erro_txt('O valor inserido não é um número, tente novamente!')
                        return
                    
                    resposta = str(input('Insira a sua resposta, contendo entre 10 e 500 caraacteres: ').strip().capitalize())

                    if not resposta:
                        Util.erro_txt('O campo está vazio, preencha-o!')
                        Util.pausa(3)
                        return
                    
                    if len(resposta) < 10 or len(resposta) > 500:
                        Util.erro_txt('Sua pergunta ou não atinge a quantidade mínima de caracteres ou ultrapassa o limite!')
                        Util.pausa(3)
                        return
                    
                    if not any(char.isalpha() for char in resposta):
                        Util.erro_txt('Sua pergunta precisa conter caracteres alfabéticos!')
                        Util.pausa(3)
                        return
                    
                    self.perguntas[esc_pergunta - 1]['respostas'].append(resposta)

                    Util.txt_certo('Resposta cadastrada com sucesso!')
                    Util.continuar()
                

            elif responder == 'n':
                Util.txt_aviso('Voltando para a seleção de opção')
                Util.pausa(3)
                return 
            
            else:
                Util.erro_txt('A opção escolhida é inexistente!')
                Util.pausa(3)
                return
            
        elif opcao == 3:
            Util.cabecalho('Perguntas e Respostas')
            if not self.perguntas:
                Util.erro_txt('Não há perguntas!')
                Util.pausa(3)
                return
            for i, item in enumerate(self.perguntas):
                    print(Fore.LIGHTYELLOW_EX + '{} - {}'.format(i + 1, item['pergunta']))
                    for resp in item['respostas']:
                        if not item['respostas']:
                            Util.erro_txt('Esta pergunta ainda não foi respondida!')
                        else:
                            print('     — {}'.format(resp))
            Util.continuar()
        
        elif opcao == 0:
            Util.txt_aviso('Retornando ao Menu Principal')
            Util.pausa(3)
            return menu_principal(usuario_logado)

