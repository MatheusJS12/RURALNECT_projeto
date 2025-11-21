from util import Util
from colorama import Fore, Back, Style, init

init(autoreset=True)

def area_informacoes(usuario_logado):
      Util.limpar_tela()
      Util.cabecalho('Área de informações')
      print('\nQual tipo de informação você deseja acessar?\n')
      print(Style.BRIGHT + '1 - ' + Style.NORMAL + Fore.YELLOW + 'Informações gerais') 
      print(Style.BRIGHT + '2 - ' + Style.NORMAL + Fore.YELLOW + 'Informações dos cursos') 
      print(Style.BRIGHT + '0 - ' + Style.NORMAL + Fore.YELLOW + 'Voltar para o Menu Principal') 
      
      try:
         option = int(input('digite o tipo de informação desejada: '))
         tipo_de_informacao(option, usuario_logado)
      except ValueError:
         print('\033[31mO valor inserido não é um número, favor tente novamente\033[m\n')
         Util.pausa(3)
      Util.limpar_tela()

def tipo_de_informacao(option, usuario_logado):
   if option == 1:
      Util.limpar_tela()
      print('acessando área de informações gerais...')
      Util.pausa(3)
      Util.limpar_tela()
      print('=-' * 50)
      print('{:^105}'.format('\033[36mInformações Gerais\033[m'))
      print('=-' * 50)
      print('Sobre o que você gostaria de receber informações\n')
      print(Style.BRIGHT + '1 - ' + Style.NORMAL + Fore.YELLOW + 'Informações sobre o Restaurante Universitário') 
      print(Style.BRIGHT + '2 - ' + Style.NORMAL + Fore.YELLOW + 'Contatos') 
      opcao_geinfo = int(input('digite a opcao desejada: '))
      Util.limpar_tela()
      if opcao_geinfo == 1:
         Util.limpar_tela()
         print('\033[32mAqui estão as principais informações sobre o RU:\033[m\n')
         Util.pausa(5)
         print('O RU funciona de segunda à sexta, no almoço: 10:30 às 14:00; e no jantar: 16:30 às 19:00. \n\nPara realizar o cadastramento, é necessário apresentar os seguintes documentos: Documento com foto e o atestado de matrícula do período vigente\n\nPara mais informações, ligue para esse número: 3320-6196\n')
         input('Pressione Enter para continuar...')
         Util.limpar_tela()
         return 
      elif opcao_geinfo == 2:
         Util.limpar_tela()
         print('\033[32mAqui estão o contatos da Universidade Rural de Pernambuco:\033[m\n')
         Util.pausa(5)
         print('REITORIA:\n telefone:(81)3320-6001.\n E-mail: reitoria@ufrpe.br\n\n GABINETE DA REITORIA:\n E-mail: gabinete.reitoria@ufrpe.br\n\n VICE-REITORIA:\n telefone: (81)3320-6023\n\n PROGESTI:\n telefone: (81) 3320-6091\n E-mail: secretaria.progest@ufrpe.br OU assiste.social.progest@ufrpe.br \n\n DRCA:\n telefones: (81)3320-6081 OU (81)3320-6080\n E-mail: secretaria.drca@ufrpe.br')
         input('Pressione Enter para continuar...')
         Util.limpar_tela()
         return
      else:
           print('\033[31mO valor inserido não é válido, favor tente novamente\033[m\n')
           Util.pausa(3)
           return
   elif option == 2:
      curso_info = usuario_logado['curso']
      if curso_info == 'Bacharelado em Sistemas de Informação':
         #COLOCAR COMO ESTÁ EM INFORMAÇÕES GERAIS
         print('Opções:\n1 - informações básicas do curso\n2 - matriz curricular\n3 - ementas e programas\n4 - projeto pedagógico\n5 - repositório de disciplinas\n6 - atividades complementares\n')
         opcao_infocurso = int(input('Insira a opção desejada: '))
         Util.limpar_tela()
         if opcao_infocurso == 1:
            print('Curso: Bacharelado em Sistemas de Informação (BSI) - SEDE RECIFE\n\nDuração Média: 10 semestres (5 anos)\n\nTurno: Manhã (presencial - verificar edital)\n\nFoco: Desenvolvimento e Gestão de Sistemas de Informação, Banco de Dados e Redes.\n\nContato (Coordenação): coordenacao.bsi@ufrpe.br / (81) 3320-6491')
            input('Pressione Enter para continuar...')
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
            print('Opção inválida, selecione outra!')
            return
      elif curso_info == 'Bacharelado em Ciências da Computação':
          Util.limpar_tela()
          print('Curso: Bacharelado em Ciência da Computação (BCC) - SEDE RECIFE\n\nDuração Média: 9 semestres\n\nCarga Horária: 3.210 horas\n\nTurno: Vespertino (tarde)\n\nFoco: Fundamentos teóricos e práticos da computação, desenvolvimento de software, pesquisa e solução de problemas complexos.\n\nContato (Coordenação): coordenacao.bcc@ufrpe.br / (81) 3320-5439')
          Util.pausa(10)
          Util.limpar_tela()
          return
      elif curso_info == 'Licenciatura em Computação':
         Util.limpar_tela()
         print('Curso: Licenciatura em Computação (LC) - SEDE RECIFE\n\nDuração Média: 9 semestres\n\nTurno: Noturno\n\nFoco: Formação de professores para atuar na educação básica e não escolar, unindo conhecimentos de Computação e Pedagogia.\n\nContato (Coordenação): coordenacao.lc@ufrpe.br / (81) 3320-5441')
         Util.pausa(10)
         Util.limpar_tela()
         return
      else:
         Util.limpar_tela()
         print('\033[31mO valor inserido não é válido, favor tente novamente\033[m\n')
         Util.pausa (3)
         return
   elif option == 0: 
      Util.limpar_tela()
      print('Voltando para o menu principal...')
      Util.pausa(3)
      return
   else:
      Util.limpar_tela()
      print('\033[31mO valor inserido não é válido, favor tente novamente\033[m\n')
      Util.pausa(5)