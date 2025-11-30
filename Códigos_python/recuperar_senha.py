from util import Util
import esqueci_minhasenha
import socket

def recuperar_senha(usuarios, menu_inicial):
    cont = 0
    Util.limpar_tela()
    Util.cabecalho('Recuperação de Senha')
    print('\nPara efetuar a recuperação de senha, você deverá inserir o e-mail e o código que será enviado!\n')
    email_user = str(input('Insira o e-mail: ').strip().lower())
    for usuario in usuarios:
        if email_user == usuario['email']:
            user = usuario['nome']
            try:
                esqueci_minhasenha.esqueci_minhasenha(usuarios, user, email_user)

            except socket.gaierror:
                Util.erro_txt('E-mail não enviado: Usuário sem internet')
                Util.continuar()
                return menu_inicial()
            codigo_rec = str(input('Insira o código recebido no e-mail: '))
            if codigo_rec == esqueci_minhasenha.num_secreto:
                while cont < 1:
                    nova_senha = str(input('Insira uma nova senha: ').strip())
                    novasenha_tam = len(nova_senha)
                    if novasenha_tam < 6 or novasenha_tam > 20:
                        Util.erro_txt('A senha não possui a quantidade mínima de 6 caracteres ou excedeu a quantidade máxima de 20!')
                        Util.pausa(5)
                        return
                    if not any(chr.isnumeric() for chr in nova_senha):
                        Util.erro_txt('Sua senha não possui pelo menos um número')
                        Util.pausa(5)
                        return
                    if not any(chr.isupper() for chr in nova_senha):
                        Util.erro_txt('Sua senha não possui letra maiúscula!')
                        Util.pausa(5)
                        return
                    elif ' ' in nova_senha:
                        Util.erro_txt('A sua senha possui espaços, remova-os!\n')
                        Util.pausa(5)
                        return
                    conf_novasenha = str(input('Confirme sua nova senha: ').strip())
                    if conf_novasenha == nova_senha:
                        usuario['senha'] = nova_senha
                        cont = cont + 1
                        menu_inicial()
                    else:
                        cont = 0
            else:
                Util.erro_txt('O código inserido não corresponde ao enviado para o email')
                Util.pausa(3)
                menu_inicial()
