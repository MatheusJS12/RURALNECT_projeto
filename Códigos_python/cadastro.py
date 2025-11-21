from util import Util

def cadastro_usuario(usuarios):
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
    curso = str(input('Insira as iniciais do seu curso: ').strip().upper())
    if curso.isdigit() or curso == '':
        Util.erro_txt('Seu curso está vázio ou não contém caracteres alfabéticos!')
        Util.pausa(5)
        return
    if curso == 'BSI' or 'SI':
        curso = 'Bacharelado em Sistemas de Informação'
    elif curso == 'CC' or 'BCC':
        curso = 'Bacharelado em Ciências da Computação'
    elif curso == 'LC':
        curso = 'Licenciatura em Computação'
    email = str(input('Insira o seu e-mail institucional: ').strip().lower())
    if not email.endswith('@ufrpe.br'):
        Util.limpar_tela()
        Util.erro_txt('Adicione um e-mail institucional válido!')
        Util.pausa(5)
        return
    for usuario in usuarios:
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

    usuarios.append({'nome': nome, 'curso': curso, 'email': email, 'senha': senha})

    Util.txt_certo('\nCadastro realizado com sucesso!')
    Util.continuar()
