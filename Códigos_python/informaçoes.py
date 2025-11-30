from util import Util
from colorama import Fore, Back, Style, init

init(autoreset=False)

def area_informacoes(usuario_logado):
      Util.limpar_tela()
      Util.cabecalho('Área de informações')
      print('\nQual tipo de informação você deseja acessar?\n')
      Util.txt_opcao('1', 'Informações gerais') 
      Util.txt_opcao('2', 'Informações dos cursos') 
      Util.txt_opcao('0', 'Voltar para o Menu Principal')
      
      try:
         opcao = int(input('digite o tipo de informação desejada: '))
         tipo_de_informacao(opcao, usuario_logado)
      except ValueError:
         Util.erro_txt('O valor inserido não é um número inteiro, tente novamente!')
         Util.pausa(3)
         return
      Util.limpar_tela()

def tipo_de_informacao(opcao, usuario_logado):
   if opcao == 1:
      Util.limpar_tela()
      print('acessando área de informações gerais...')
      Util.pausa(3)
      Util.limpar_tela()
      Util.cabecalho('Informações Gerais')
      print('Sobre o que você gostaria de receber informações:\n')
      Util.txt_opcao('1', 'Informações sobre o Restaurante Universitário')
      Util.txt_opcao('2', 'Contatos')
      try:
         opcao_info_geral = int(input('digite a opcao desejada: '))
      except ValueError:
         Util.erro_txt('O valor inserido não é um número, tente novamente!')
         Util.pausa(3)
         return
      Util.limpar_tela()
      if opcao_info_geral == 1:
         Util.limpar_tela()
         print(Fore.LIGHTYELLOW_EX + 'Aqui estão as principais informações sobre o RU:\n')
         Util.pausa(3)
         print('O RU funciona de segunda à sexta, no almoço: 10:30 às 14:00; e no jantar: 16:30 às 19:00. \n\nPara realizar o cadastramento, é necessário apresentar os seguintes documentos: Documento com foto e o atestado de matrícula do período vigente\n\nPara mais informações, ligue para esse número: 3320-6196\n')
         Util.continuar()
         Util.limpar_tela()
         return 
      elif opcao_info_geral == 2:
         Util.limpar_tela()
         print(Fore.LIGHTYELLOW_EX + 'Aqui estão o contatos da Universidade Rural de Pernambuco:\n')
         Util.pausa(3)
         print('REITORIA:\n telefone:(81)3320-6001.\n E-mail: reitoria@ufrpe.br\n\n GABINETE DA REITORIA:\n E-mail: gabinete.reitoria@ufrpe.br\n\n VICE-REITORIA:\n telefone: (81)3320-6023\n\n PROGESTI:\n telefone: (81) 3320-6091\n E-mail: secretaria.progest@ufrpe.br OU assiste.social.progest@ufrpe.br \n\n DRCA:\n telefones: (81)3320-6081 OU (81)3320-6080\n E-mail: secretaria.drca@ufrpe.br')
         Util.continuar()
         Util.limpar_tela()
         return
      else:
         Util.erro_txt('A opção inserida é inválida!')
         Util.pausa(3)
         return
   elif opcao == 2:
      curso_info = usuario_logado['curso']
      if curso_info == 'Bacharelado em Sistemas de Informação':
         #COLOCAR COMO ESTÁ EM INFORMAÇÕES GERAIS
         print('Opções:')
         Util.txt_opcao('1', 'informações básicas do curso')
         Util.txt_opcao('2', 'matriz curricular')
         Util.txt_opcao('3', 'ementas e programas')
         Util.txt_opcao('4', 'projeto pedagógico')
         Util.txt_opcao('5', 'repositório de disciplinas')
         Util.txt_opcao('6', 'atividades complementares')

         opcao_infocurso = int(input('Insira a opção desejada: '))
         Util.limpar_tela()
         if opcao_infocurso == 1:
            print('Curso: Bacharelado em Sistemas de Informação (BSI) - SEDE RECIFE\n\nDuração Média: 10 semestres (5 anos)\n\nTurno: Manhã (presencial - verificar edital)\n\nFoco: Desenvolvimento e Gestão de Sistemas de Informação, Banco de Dados e Redes.\n\nContato (Coordenação): coordenacao.bsi@ufrpe.br / (81) 3320-6491')
            Util.continuar()
            Util.limpar_tela()
            return
         elif opcao_infocurso == 2:
            print('redirecionando para a matriz curricular...')
            Util.pausa(3)
            Util.redirecionador('https://sites.google.com/view/bsi-ufrpe/contato/matriz-curricular?authuser=0')
            return
         elif opcao_infocurso == 3:
            print('Redirecionando para as ementas e programas...')
            Util.pausa(3)
            Util.redirecionador('https://sites.google.com/view/bsi-ufrpe/contato/ementas-e-programas?authuser=0')
            return
         elif opcao_infocurso == 4:
            print('Redirecionando para o projeto pedagógico...')
            Util.pausa(3)
            Util.redirecionador('https://www.dropbox.com/scl/fi/08te5vnvdl3e8ayormshb/PPC-BSI-v.3.pdf?rlkey=l6nwtpsl0a5pqjm1vh82thn3k&e=1&dl=0')
            return
         elif opcao_infocurso == 5:
            print('Redirecionando para o repositório de disciplinas...')
            Util.pausa(3)
            Util.redirecionador('https://sites.google.com/view/bsi-ufrpe/contato/reposit%C3%B3rio-de-disciplinas?authuser=0')
            return
         elif opcao_infocurso == 6:
            print('Redirecionando para as atividades complementares...')
            Util.pausa(3)
            Util.redirecionador('https://sites.google.com/view/bsi-ufrpe/contato/atividades-complementares?authuser=0')
            return
         else:
            print('Opção inválida, selecione outra!') #trocar
            return
      elif curso_info == 'Bacharelado em Ciências da Computação':
          Util.limpar_tela()
          print('Curso: Bacharelado em Ciência da Computação (BCC) - SEDE RECIFE\n\nDuração Média: 9 semestres\n\nCarga Horária: 3.210 horas\n\nTurno: Vespertino (tarde)\n\nFoco: Fundamentos teóricos e práticos da computação, desenvolvimento de software, pesquisa e solução de problemas complexos.\n\nContato (Coordenação): coordenacao.bcc@ufrpe.br / (81) 3320-5439')
          Util.continuar()
          Util.limpar_tela()
          return
      elif curso_info == 'Licenciatura em Computação':
         Util.limpar_tela()
         print('Curso: Licenciatura em Computação (LC) - SEDE RECIFE\n\nDuração Média: 9 semestres\n\nTurno: Noturno\n\nFoco: Formação de professores para atuar na educação básica e não escolar, unindo conhecimentos de Computação e Pedagogia.\n\nContato (Coordenação): coordenacao.lc@ufrpe.br / (81) 3320-5441')
         Util.continuar()
         Util.limpar_tela()
         return
      else:
         Util.limpar_tela()
         Util.erro_txt('A opção inserida é inválida!')
         Util.pausa (3)
         return
   elif opcao == 0: 
      Util.limpar_tela()
      print('Voltando para o menu principal...')
      Util.pausa(3)
      return
   else:
      Util.limpar_tela()
      Util.erro_txt('A opção inserida é inválida!')
      Util.pausa(3)