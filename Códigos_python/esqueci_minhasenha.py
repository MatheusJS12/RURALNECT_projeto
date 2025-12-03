import smtplib
import email.message
import secrets
from util import Util

# https://www.youtube.com/watch?v=N97q96BygUg
# Link do vídeo do código.

class Email_senha:
    def __init__(self):
        self.num_secreto = secrets.token_hex(3)

    def esqueci_minhasenha(self, usuarios, user, email_user):

        
        if  len(email_user) <= 0:
            Util.erro_txt('A área está vazia, favor preencher')
            Util.limpar_tela()
            Util.pausa(5)
            return 
        else:
            Util.txt_certo('Email cadastrado, iremos enviar um email para a redefiniçao da senha')
            Util.pausa(5)
            Util.limpar_tela()
            

        corpo_email = """
        <p>Olá, {},</p>
        <p>Recebemos uma solicitação para redefinir a senha da sua conta na RURALNECT.</p>
        <p>Para completar o processo e criar uma nova senha, por favor, utilize o código ou siga as instruções fornecidas no sistema</p>
        <b>{}</b>
        <p>Se você não solicitou esta alteração, por favor, ignore este e-mail. A sua senha atual permanecerá inalterada e a sua conta continuará segura.</p>
        <p>Se tiver alguma dificuldade ou precisar de ajuda, entre em contato com nossa equipe de suporte.</p>
        <p>Atenciosamente,</p>
        <p> Equipe RURALNECT.</p>
        """.format(user, self.num_secreto)

        msg = email.message.Message()
        msg['Subject'] = 'Solicitação de redefinição de senha'
        msg['From'] = 'ruralnect@gmail.com'
        msg['To'] = email_user
        password = 'jnpjsxkcbwvkiqyf'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        Util.txt_certo('Email enviado com sucesso!')
        Util.txt_aviso('Caso não encontre na caixa principal, verifique a caixa de spam.')