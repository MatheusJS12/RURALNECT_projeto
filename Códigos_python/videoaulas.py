from util import Util

def area_videoaulas(usuario_logado):
    # TALVEZ, QUANDO FOR ADICIONAR UMA OPÇÃO PARA O DOCENTE ADICIONAR CONTEÚDO, PODE SER NECESSÁRIO CRIAR OUTRA ABA PARA CONTEÚDOS DIVERSOS, VISTO QUE SERIA "COMPLICADO" ADICIONAR TODO O CONTEÚDO JÁ ADICIONADO. EX.: CONTEÚDO - PROFESSORES.
    if usuario_logado['curso'] == 'Bacharelado em Sistemas de Informação':
        print('=' * 70)
        print('{:^70}'.format('Cadeiras - BSI'))
        print('=' * 70)
        print('1 - Fundamentos de matemática para Sistemas de Informação 1\n2 - Introdução à Administraçao\n3 - Princípios de Programação\n4 - Sustentabilidade em Sistemas de Informação\n5 - Projeto Interdisciplinar para Sistemas de informação 1 ')
        print('=' * 70)
        opcao = int(input('\nInsira a cadeira desejada: '))
        Util.limpar_tela()

        if opcao == 1:
            print('=' * 50)
            print('{:^50}'.format('Assuntos - BSI'))
            print('=' * 50)
            print('\n1 - Grafos\n2 - Otimização\n3 - Conjunto\n')
            opcao_assunto = int(input('Insira o valor correspondente ao assunto desejado: '))

            if opcao_assunto == 1:
                Util.videoaula(
                    'Grafos',
                    'Silvana Bocanegra',
                    'http://google.com/file/d/1zlnRfu0M4DiMeBp8HKbsR9C_tqZyxiuA/view?usp=drive_link',
                    'Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.'
                )

            if opcao_assunto == 2:
                Util.videoaula(
                    'Otimização',
                    'Silvana Bocanegra',
                    'https://drive.google.com/drive/folders/1KaX1MMiOasWdkzzjbKUe_oYV9bnZVhL4?usp=sharing',
                    'Nesta coletânea do assunto de Otimização, são abordados seus fundamentos e aplicações.'
                )

            if opcao_assunto == 3:
                Util.videoaula(
                    'Conjuntos',
                    'Silvana Bocanegra',
                    'https://www.youtube.com/watch?v=y2V3A4SMs74&authuser=4',
                    'Conteúdo introdutório sobre Teoria dos Conjuntos.'
                )

        elif opcao == 2:
            print('=' * 50)
            print('{:^50}'.format('Assuntos - BSI'))
            print('=' * 50)
            print('\n1 - Conceitos Iniciais\n2 - Ambiente Externo\n3 - Tomada de Decisão Administrativa\n4 - Ética e Responsabilidade Empresarial\n')
            opcao_assunto = int(input('Insira o valor correspondente ao assunto desejado: '))

            if opcao_assunto == 1:
                Util.videoaula(
                    'Conceitos Iniciais',
                    'Daniel Lins',
                    'https://drive.google.com/file/d/1e-5Ap2mRwA7-vKisHdFNmLYTR471M2H_/view',
                    'Conteúdo introdutório de Administração com foco em conceitos fundamentais.'
                )

            if opcao_assunto == 2:
                Util.videoaula(
                    'Ambiente Externo',
                    'Daniel Lins',
                    'https://www.youtube.com/watch?v=bS_I2xpFzFU&feature=youtu.be',
                    'Aula sobre fatores externos que influenciam o funcionamento das organizações.'
                )

            if opcao_assunto == 3:
                Util.videoaula(
                    'Tomada de Decisão Administrativa',
                    'Daniel Lins',
                    'https://www.youtube.com/watch?v=G0QXXaj9554',
                    'Materiais sobre modelos de decisão dentro da Administração.'
                )

            if opcao_assunto == 4:
                Util.videoaula(
                    'Ética e Responsabilidade Empresarial',
                    'Daniel Lins',
                    'https://drive.google.com/file/d/1OdZvXYFu0HWFQb5pAA1v7VHWvqe7e5fd/view',
                    'Estudo sobre ética corporativa e responsabilidade social.'
                )

        elif opcao == 3:
            print('=' * 50)
            print('{:^50}'.format('Assuntos - BSI'))
            print('=' * 50)
            print('\n1 - Representações de um algoritmo\n2 - Lógica de Programação\n3 - Introdução ao Python\n')
            opcao_assunto = int(input('Insira o valor correspondente ao assunto desejado: '))

            if opcao_assunto == 1:
                Util.videoaula(
                    'Representações de um Algoritmo',
                    'Iuri Sônego Cardoso',
                    'https://www.youtube.com/watch?v=Wt7Pv9kjdWk&t=18s',
                    'Introdução às diversas formas de representar algoritmos.'
                )

            if opcao_assunto == 2:
                Util.videoaula(
                    'Lógica de Programação',
                    'Gustavo Guanabara',
                    'https://www.youtube.com/watch?v=8mei6uVttho&list=PLHz_AreHm4dmSj0MHol_aoNYCSGFqvfXV',
                    'Curso introdutório de lógica de programação.'
                )

            if opcao_assunto == 3:
                Util.videoaula(
                    'Introdução ao Python',
                    'Gustavo Guanabara',
                    'https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0',
                    'Introdução à linguagem Python.'
                )

        elif opcao == 4:
            print('=' * 50)
            print('{:^50}'.format('Assuntos - BSI'))
            print('=' * 50)
            print('\n1 - Papel dos SIs na Sustentabilidade\n2 - Economia Digital e seus reflexos sustentáveis\n3 - Impactos Sociais das Tecnologias\n4 - Tecnologia e Meio Ambiente\n5 - TI Verde\n')
            opcao_assunto = int(input('Insira o valor correspondente ao assunto desejado: '))

            if opcao_assunto == 1:
                Util.videoaula(
                    'Papel dos SIs na Sustentabilidade',
                    'Iuri Sônego Cardoso',
                    'https://www.youtube.com/watch?v=Wt7Pv9kjdWk&t=18s',
                    'Discussão sobre o papel dos Sistemas de Informação na sustentabilidade.'
                )

            if opcao_assunto == 2:
                Util.videoaula(
                    'Economia Digital e Reflexos Sustentáveis',
                    'Fundação Dom Cabral',
                    'https://www.youtube.com/watch?v=v0MJbh6av5o',
                    'Impactos da economia digital na sustentabilidade.'
                )

            if opcao_assunto == 3:
                Util.videoaula(
                    'Impactos Sociais das Tecnologias',
                    'Romulo Bolivar',
                    'https://www.youtube.com/watch?v=2Z_UP9VsWl4',
                    'Análise dos impactos sociais gerados pelas tecnologias.'
                )

            if opcao_assunto == 4:
                Util.videoaula(
                    'Tecnologia e Meio Ambiente',
                    'Ruptura',
                    'https://www.youtube.com/watch?v=OT52nq0VDqo',
                    'Discussão sobre como as tecnologias influenciam o meio ambiente.'
                )

            if opcao_assunto == 5:
                Util.videoaula(
                    'TI Verde',
                    'Bóson Treinamentos',
                    'https://www.youtube.com/watch?v=8igyusXZ-5I',
                    'Conteúdo sobre práticas sustentáveis de Tecnologia da Informação.'
                )
