from util import Util
from colorama import Fore, Back, Style, init
from recuperar_senha import Recuperacao_Senha
import maskpass

init(autoreset=False)

class Auth:
    def __init__(self):
        self.usuarios = []
        self.usuario_logado = {'nome': '', 'curso': '', 'email': ''}

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
        curso = str(input('\nInsira as iniciais do seu curso (BSI, BCC, LC): ').strip().upper())
        if curso.isdigit() or curso == '':
            Util.erro_txt('Seu curso está vázio ou não contém caracteres alfabéticos!')
            Util.pausa(5)
            return
        if curso == ('BSI' or 'SI'):
            curso = 'Bacharelado em Sistemas de Informação'
        elif curso == ('BCC' or 'CC'):
            curso = 'Bacharelado em Ciências da Computação'
        elif curso == 'LC':
            curso = 'Licenciatura em Computação'
        else:
            Util.erro_txt('Curso indisponível, selecione um válido!')
            Util.pausa(3)
            return
        email = str(input('\nInsira o seu e-mail institucional: ').strip().lower())
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
        senha = maskpass.askpass('\nInsira uma senha forte: ').strip()
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
        senha_confirm = maskpass.askpass('\nInsira a senha novamente para confirmar: ').strip()
        if senha_confirm != senha:
            Util.erro_txt('Erro: A senha inserida não corresponde à adicionada anteriormente!')
            Util.pausa(3)
            return

        self.usuarios.append({'nome': nome, 'curso': curso, 'email': email, 'senha': senha})

        Util.txt_certo('\nCadastro realizado com sucesso!')
        Util.continuar()

    def login(self, menu_inicial):
        rec = Recuperacao_Senha()
        Util.limpar_tela()
        Util.cabecalho('Menu Login')
        print('Insira uma das opções para prosseguir:')
        Util.txt_opcao('1', 'Login')
        Util.txt_opcao('2', 'Recuperar Senha')
        Util.txt_opcao('0', 'Voltar ao Menu Inicial')

        try:
            opcao_login = int(input('\nInsira a opção desejada: '))
        except ValueError:
            Util.erro_txt('O valor inserido não é um número inteiro, tente novamente!')
            Util.pausa(3)
            return menu_inicial()

        if opcao_login == 1:

            rest_senha = 0
            cont = 3
            
            while rest_senha != '1':
                Util.limpar_tela()
                Util.cabecalho('Menu Login')
                if cont < 1:
                        Util.txt_aviso('A quantidade de tentativas de login superou o limite de 3 chances, tente novamente mais tarde!')
                        Util.pausa(5)
                        Util.limpar_tela()
                        rest_senha = int(input('Deseja ir para a área de recuperação de senha? (1 - S/0 - N): ').strip().lower())
                        if rest_senha == 1:
                            rec.recuperar_senha(self.usuarios, menu_inicial)
                            return
                        elif rest_senha == 0:
                            print('Voltando ao menu inicial...')
                            Util.pausa(3)
                            return menu_inicial()
                usuario_email = str(input('Insira o e-mail: ').strip().lower())
                senha_user = maskpass.askpass('Insira a senha: ').strip()
                for usuario in self.usuarios:
                    if usuario_email == usuario['email'] and senha_user == usuario['senha']:
                        print('Bem-vindo, {}'.format(usuario['nome']))
                        self.usuario_logado['nome'] = usuario['nome']
                        self.usuario_logado['curso'] = usuario['curso']
                        self.usuario_logado['email'] = usuario['email']
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
            rec.recuperar_senha(self.usuarios, menu_inicial)

        elif opcao_login == 0:
            Util.limpar_tela()
            print('Voltando ao Menu Inicial...')
            Util.pausa(3)
            return menu_inicial()
        else:
            Util.erro_txt('O valor inserido não corresponde a nenhuma das opções listadas!')
            Util.pausa(3)
            return
        
    def configuracoes(self, menu_inicial):
        Util.cabecalho('Configurações')
        Util.txt_opcao('\n1', 'Deletar conta')
        Util.txt_opcao('0', 'Voltar ao Menu Principal')

        try:
            opcao = int(input('Insira a opção desejada: '))

        except ValueError:
            Util.erro_txt('O valor inserido não é um número, tente novamente!')
            Util.pausa(3)
            return

        if opcao == 1:
            print('Acessando Deletar Conta')
            Util.pausa(2)
            self.deletar_conta(menu_inicial)

        elif opcao == 0:
            Util.txt_aviso('Retornando ao Menu Principal')
            Util.pausa(2)
            return

    def deletar_conta(self, menu_inicial):
        Util.cabecalho('Exclusão de conta')
        for conta in self.usuarios:
            if self.usuario_logado['email'] == conta['email']:
                print('nome: {}'.format(conta['nome']))
                print('curso: {}'.format(conta['curso']))
                print('e-mail: {}'.format(conta['email']))
                print('senha: {}'.format(maskpass.advpass(conta['senha'])))
                user_conta = conta
                break
        if not user_conta:
            Util.erro_txt('Conta não encontrada')
            Util.pausa(3)
            return
        
        deletar = str(input('Você deseja deletar sua conta? (s/n): ').strip().lower())
        
        if deletar == 's':
            senha = maskpass.askpass('Insira sua senha para deletar a conta: ').strip()
            if senha == user_conta['senha']:
                self.usuarios.remove(user_conta)
                Util.txt_certo('Conta deletada com sucesso!')
                Util.pausa(2)
                Util.txt_aviso('Retornando ao Menu Inicial')
                Util.pausa(2)
                return menu_inicial()
            else:
                Util.erro_txt('Senha incorreta')
                Util.pausa(2)
                return
        
        elif deletar == 'n':
            Util.txt_aviso('Voltando ao Menu Principal')
            Util.pausa(3)
            return
        