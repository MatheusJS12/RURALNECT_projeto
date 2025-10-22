from util import limpar_tela
from time import sleep
import recuperar_senha

def login(usuarios, menu_inicial, usuario_logado):
    print('=-' * 50)
    print('{:^105}'.format('\033[34mMenu Login\033[m'))
    print('=-' * 50)
    print('Insira uma das opções para prosseguir:\n\033[1m1\033[m - \033[33mLogin\033[m\n\033[1m2\033[m - \033[33mRecuperar Senha\033[m\n\033[1m0\033[m - \033[33mVoltar para o Menu Principal\033[m\n')
    opcao_login = int(input('Insira a opção desejada: '))

    if opcao_login == 1:

        rest_senha = 0
        cont = 3
        
        while rest_senha != '1':
            usuario_email = str(input('Insira o e-mail: ').strip().lower())
            senha_user = str(input('Insira a senha: ').strip())
            for usuario in usuarios:
                if cont == 0:
                    print('A quantidade de tentativas de login superou o limite de 3 chances, tente novamente mais tarde!')
                    sleep(5)
                    limpar_tela()
                    rest_senha = int(input('Deseja ir para a área de recuperação de senha? (1 - S/0 - N): ').strip().lower())
                    if rest_senha == 1:
                        recuperar_senha.recuperar_senha(usuarios, menu_inicial)
                        return
                    elif rest_senha == 0:
                        print('Voltando ao menu inicial...')
                        sleep(3)
                        return
                if usuario_email == usuario['email'] and senha_user == usuario['senha']:
                    print('Bem-vindo, {}'.format(usuario['nome']))
                    usuario_logado['nome'] = usuario['nome']
                    usuario_logado['curso'] = usuario['curso']
                    return
                elif usuario_email == usuario['email'] and senha_user != usuario['senha'] or usuario_email != usuario['email'] and senha_user == usuario['senha'] or usuario_email != usuario['email'] and senha_user != usuario['senha']:
                    print('Login não-sucedido, tente novamente!')
                    cont = cont - 1
                    print('chances restantes {}'.format(cont))
                
            sleep(5)
            limpar_tela()
    elif opcao_login == 2:
        limpar_tela()
        print('Redirecionando para a recuperação de senha...')
        sleep(3)
        recuperar_senha.recuperar_senha(usuarios, menu_inicial)
    else:
        print('\033[31mO valor inserido não corresponde a nenhuma das opções listadas!\033[m')
        sleep(3)
        return