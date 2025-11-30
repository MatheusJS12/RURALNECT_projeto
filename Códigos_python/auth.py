from util import Util
from colorama import Fore, Back, Style, init
import recuperar_senha

init(autoreset=True)

class Auth:
    def __init__(self):
        self.usuarios = []
        self.usuario_logado = {'nome': '', 'curso': ''}

    def cadastro_usuario(self):
        Util.cabecalho('Menu Cadastro')
        nome = str(input('\nInsira o seu nome completo: ').strip().upper())
        nome_tam = len(nome)
        if nome_tam < 10:
            Util.erro_txt('Nome completo com caracteres insuficientes')
            Util.pausa(5)
            return
        if nome.isdigit() or nome == '':
            Util.erro_txt('Seu nome está vázio ou não contém caracteres alfabéticos!')
            Util.pausa(5)
            return
        curso = str(input('Insira as iniciais do seu curso (BSI, BCC, LC): ').strip().upper())
        if curso.isdigit() or curso == '':
            Util.erro_txt('Seu curso está vázio ou não contém caracteres alfabéticos!')
            Util.pausa(5)
            return
        if curso == ('BSI' or 'SI'):
            curso = 'Bacharelado em Sistemas de Informação'
        elif curso == ('CC' or 'BCC'):
            curso = 'Bacharelado em Ciências da Computação'
        elif curso == 'LC':
            curso = 'Licenciatura em Computação'
        email = str(input('Insira o seu e-mail institucional: ').strip().lower())
        if not email.endswith('@ufrpe.br'):
            Util.limpar_tela()
            Util.erro_txt('Adicione um e-mail institucional válido!')
            Util.pausa(5)
            return
        for usuario in self.usuarios:
            if email == usuario['email']:
                Util.erro_txt('Este e-mail já está cadastrado!')
                Util.pausa(5)
                return
        senha = str(input('Insira uma senha forte: ').strip())
        senha_tam = len(senha)
        if senha_tam < 6 or senha_tam > 20:
            Util.erro_txt('A senha não possui a quantidade mínima de 6 caracteres ou excedeu a quantidade máxima de 20!')
            Util.pausa(5)
            return
        if not any(chr.isnumeric() for chr in senha):
            Util.erro_txt('Sua senha não possui pelo menos um número')
            Util.pausa(5)
            return
        if not any(chr.isupper() for chr in senha):
            Util.erro_txt('Sua senha não possui pelo menos uma letra maiúscula')
            Util.pausa(5)
            return
        elif ' ' in senha:
            Util.erro_txt('A sua senha possui espaços, remova-os!')
            Util.pausa(5)
            return
        senha_confirm = str(input('Insira a senha novamente para confirmar: ').strip())
        if senha_confirm != senha:
            Util.erro_txt('Erro: A senha inserida não corresponde à adicionada anteriormente!')
            Util.pausa(3)
            return

        self.usuarios.append({'nome': nome, 'curso': curso, 'email': email, 'senha': senha})

        Util.txt_certo('\nCadastro realizado com sucesso!')
        Util.continuar()

    def login(self, menu_inicial):
        Util.limpar_tela()
        Util.cabecalho('Menu Login')
        print('Insira uma das opções para prosseguir:')
        Util.txt_opcao('1', 'Login')
        Util.txt_opcao('2', 'Recuperar Senha')
        Util.txt_opcao('0', 'Voltar ao Menu Principal')

        try:
            opcao_login = int(input('Insira a opção desejada: '))
        except ValueError:
            Util.erro_txt('O valor inserido não é um número inteiro, tente novamente!')
            Util.pausa(3)
            return

        if opcao_login == 1:

            rest_senha = 0
            cont = 3
            
            while rest_senha != '1':
                Util.limpar_tela()
                Util.cabecalho('Menu Login')
                usuario_email = str(input('Insira o e-mail: ').strip().lower())
                senha_user = str(input('Insira a senha: ').strip())
                for usuario in self.usuarios:
                    if cont == 0:
                        Util.txt_aviso('A quantidade de tentativas de login superou o limite de 3 chances, tente novamente mais tarde!')
                        Util.pausa(5)
                        Util.limpar_tela()
                        rest_senha = int(input('Deseja ir para a área de recuperação de senha? (1 - S/0 - N): ').strip().lower())
                        if rest_senha == 1:
                            recuperar_senha.recuperar_senha(self.usuarios, menu_inicial)
                            return
                        elif rest_senha == 0:
                            print('Voltando ao menu inicial...')
                            Util.pausa(3)
                            return
                    if usuario_email == usuario['email'] and senha_user == usuario['senha']:
                        print('Bem-vindo, {}'.format(usuario['nome']))
                        self.usuario_logado['nome'] = usuario['nome']
                        self.usuario_logado['curso'] = usuario['curso']
                        return
                    elif usuario_email == usuario['email'] and senha_user != usuario['senha'] or usuario_email != usuario['email'] and senha_user == usuario['senha'] or usuario_email != usuario['email'] and senha_user != usuario['senha']:
                        Util.erro_txt('Login não-sucedido, tente novamente!')
                        cont = cont - 1
                        print('chances restantes {}'.format(cont))
                    
                Util.pausa(5)
                Util.limpar_tela()
        elif opcao_login == 2:
            Util.limpar_tela()
            print('Redirecionando para a recuperação de senha...')
            Util.pausa(3)
            recuperar_senha.recuperar_senha(self.usuarios, menu_inicial)

        elif opcao_login == 0:
            Util.limpar_tela()
            print('Voltando ao Menu Inicial...')
            Util.pausa(3)
            return menu_inicial()
        else:
            Util.erro_txt('O valor inserido não corresponde a nenhuma das opções listadas!')
            Util.pausa(3)
            return