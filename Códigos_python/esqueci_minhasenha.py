import smtplib
import email.message
from util import limpar_tela
from time import sleep

limpar_tela()
destinatario = str(input('Digite o email cadastrado: '))

sleep(5)
limpar_tela()
def esqueci_minhasenha():
    if  len(destinatario) <= 0:
        print('\033[31mA área está vazia, favor preencher\033[m\n')
        limpar_tela()
        sleep(5)
        return 
    else:
        print('\033[32mEmail cadastrado, iremos enviar um email para a redefiniçao da senha\033[m\n')
        limpar_tela()
        sleep(5)

while True:
    corpo_email = """
    <p>Olá, Usuário,</p>
    <p>Recebemos uma solicitação para redefinir a senha da sua conta na RURALNECT.</p>
    <p>Para completar o processo e criar uma nova senha, por favor, utilize o código ou siga as instruções fornecidas no sistema</p>
    <p>Se você não solicitou esta alteração, por favor, ignore este e-mail. A sua senha atual permanecerá inalterada e a sua conta continuará segura.</p>
    <p>Se tiver alguma dificuldade ou precisar de ajuda, entre em contato com nossa equipe de suporte.</p>
    <p>Atenciosamente,</p>
    <p> Equipe RURALNECT.</p>
    """

    msg = email.message.Message()
    msg['Subject'] = 'Solicitação de redefinição de senha'
    msg['From'] = 'ruralnect@gmail.com'
    msg['To'] = destinatario
    password = 'jnpjsxkcbwvkiqyf'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('\033[32mEmail enviado com sucesso!\033[33\n')
    break 


    