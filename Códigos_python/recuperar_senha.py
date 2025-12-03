from util import Util
from esqueci_minhasenha import Email_senha
import socket
import maskpass

class Recuperacao_Senha:
    def __init__(self):
        pass
    def recuperar_senha(self, usuarios, menu_inicial):
        email_obj = Email_senha()
        cont = 0
        Util.limpar_tela()
        Util.cabecalho('Recuperação de Senha')
        print('\nPara efetuar a recuperação de senha, você deverá inserir o e-mail e o código que será enviado!\n')
        email_user = str(input('Insira o e-mail: ').strip().lower())
        for usuario in usuarios:
            if email_user == usuario['email']:
                user = usuario['nome']
                try:
                    email_obj.esqueci_minhasenha(usuarios, user, email_user)

                except socket.gaierror:
                    Util.erro_txt('E-mail não enviado: Usuário sem internet')
                    Util.continuar()
                    return menu_inicial()
                codigo_rec = maskpass.askpass('Insira o código recebido no e-mail: ').strip()
                if codigo_rec == email_obj.num_secreto:
                    while cont < 1:
                        nova_senha = maskpass.askpass('Insira uma nova senha: ').strip()
                        novasenha_tam = len(nova_senha)
                        if novasenha_tam < 6 or novasenha_tam > 20:
                            Util.erro_txt('A senha não possui a quantidade mínima de 6 caracteres ou excedeu a quantidade máxima de 20!')
                            Util.pausa(5)
                            return menu_inicial()
                        if not any(chr.isnumeric() for chr in nova_senha):
                            Util.erro_txt('Sua senha não possui pelo menos um número')
                            Util.pausa(5)
                            return menu_inicial()
                        if not any(chr.isupper() for chr in nova_senha):
                            Util.erro_txt('Sua senha não possui letra maiúscula!')
                            Util.pausa(5)
                            return menu_inicial()
                        elif ' ' in nova_senha:
                            Util.erro_txt('A sua senha possui espaços, remova-os!\n')
                            Util.pausa(5)
                            return menu_inicial()
                        conf_novasenha = maskpass.askpass('Confirme sua nova senha: ').strip()
                        if conf_novasenha == nova_senha:
                            usuario['senha'] = nova_senha
                            cont = cont + 1
                            menu_inicial()
                        else:
                            cont = 0
                else:
                    Util.erro_txt('O código inserido não corresponde ao enviado para o email')
                    Util.pausa(3)
                    return menu_inicial()
