from util import Util
import recuperar_senha

def login(usuarios, menu_inicial, usuario_logado):
    Util.limpar_tela()
    Util.cabecalho('Menu Login')
    print('Insira uma das opções para prosseguir:\n\033[1m1\033[m - \033[33mLogin\033[m\n\033[1m2\033[m - \033[33mRecuperar Senha\033[m\n\033[1m0\033[m - \033[33mVoltar para o Menu Principal\033[m\n')
    opcao_login = int(input('Insira a opção desejada: '))

    if opcao_login == 1:

        rest_senha = 0
        cont = 3
        
        while rest_senha != '1':
            Util.limpar_tela()
            Util.cabecalho('Menu Login')
            usuario_email = str(input('Insira o e-mail: ').strip().lower())
            senha_user = str(input('Insira a senha: ').strip())
            for usuario in usuarios:
                if cont == 0:
                    Util.txt_aviso('A quantidade de tentativas de login superou o limite de 3 chances, tente novamente mais tarde!')
                    Util.pausa(5)
                    Util.limpar_tela()
                    rest_senha = int(input('Deseja ir para a área de recuperação de senha? (1 - S/0 - N): ').strip().lower())
                    if rest_senha == 1:
                        recuperar_senha.recuperar_senha(usuarios, menu_inicial)
                        return
                    elif rest_senha == 0:
                        print('Voltando ao menu inicial...')
                        Util.pausa(3)
                        return
                if usuario_email == usuario['email'] and senha_user == usuario['senha']:
                    print('Bem-vindo, {}'.format(usuario['nome']))
                    usuario_logado['nome'] = usuario['nome']
                    usuario_logado['curso'] = usuario['curso']
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
        recuperar_senha.recuperar_senha(usuarios, menu_inicial)

    elif opcao_login == 0:
        Util.limpar_tela()
        print('Voltando ao Menu Inicial...')
        Util.pausa(3)
        return menu_inicial()
    else:
        Util.erro_txt('O valor inserido não corresponde a nenhuma das opções listadas!')
        Util.pausa(3)
        return