from util import limpar_tela, webbrowser

def area_videoaulas(usuario_logado):
    # TALVEZ, QUANDO FOR ADICIONAR UMA OPÇÃO PARA O DOCENTE ADICIONAR CONTEÚDO, PODE SER NECESSÁRIO CRIAR OUTRA ABA PARA CONTEÚDOS DIVERSOS, VISTO QUE SERIA "COMPLICADO" ADICIONAR TODO O CONTEÚDO JÁ ADICIONADO. EX.: CONTEÚDO - PROFESSORES.
    if usuario_logado['curso'] == 'Bacharelado em Sistemas de Informação':
        print('=' * 70)
        print('{:^70}'.format('Cadeiras - BSI'))
        print('=' * 70)
        print('1 - Fundamentos de matemática para Sistemas de Informação 1\n2 - Introdução à Administraçao\n3 - Princípios de Programação\n4 - Sustentabilidade em Sistemas de Informação\n5 - Projeto Interdisciplinar para Sistemas de informação 1 ')
        print('=' * 70)
        opcao = int(input('\nInsira a cadeira desejada: '))
        limpar_tela()
        if opcao == 1:
            print('=' * 50)
            print('{:^50}'.format('Assuntos - BSI'))
            print('=' * 50)
            print('\n1 - Grafos\n2 - Otimização\n3 - Conjunto\n')
            opcao_assunto = int(input('Insira o valor correspondente ao assunto desejado: '))
            if opcao_assunto == 1:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mGrafos\033[m'))
                print('Professor(a): {}\n'.format('\033[33mSilvana Bocanegra\033[m'))
                print('Link do conteúdo: \033[33mhttps://drive.google.com/file/d/1zlnRfu0M4DiMeBp8HKbsR9C_tqZyxiuA/view?usp=drive_link\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://drive.google.com/file/d/1zlnRfu0M4DiMeBp8HKbsR9C_tqZyxiuA/view?usp=drive_link')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
            if opcao_assunto == 2:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mOtimização\033[m'))
                print('Professor(a): {}\n'.format('\033[33mSilvana Bocanegra\033[m'))
                print('Link do conteúdo: \033[33mhttps://drive.google.com/drive/folders/1KaX1MMiOasWdkzzjbKUe_oYV9bnZVhL4?usp=sharing\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://drive.google.com/drive/folders/1KaX1MMiOasWdkzzjbKUe_oYV9bnZVhL4?usp=sharing')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
            if opcao_assunto == 3:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mConjuntos\033[m'))
                print('Professor(a): {}\n'.format('\033[33mSilvana Bocanegra\033[m'))
                print('Link do conteúdo: \033[33mhttps://www.youtube.com/watch?v=y2V3A4SMs74&authuser=4\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=y2V3A4SMs74&authuser=4')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
        if opcao == 2:
            print('=' * 50)
            print('{:^50}'.format('Assuntos - BSI'))
            print('=' * 50)
            print('\n1 - Conceitos Iniciais\n2 - Ambiente Externo\n3 - Tomada de Decisão Administrativa\n4 - Ética e Responsabilidade Empresarial\n')
            opcao_assunto = int(input('Insira o valor correspondente ao assunto desejado: '))
            if opcao_assunto == 1:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mConceitos Iniciais\033[m'))
                print('Professor(a): {}\n'.format('\033[33mDaniel Lins\033[m'))
                print('Link do conteúdo: \033[33mhttps://drive.google.com/file/d/1e-5Ap2mRwA7-vKisHdFNmLYTR471M2H_/view\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://drive.google.com/file/d/1e-5Ap2mRwA7-vKisHdFNmLYTR471M2H_/view')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
            if opcao_assunto == 2:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mAmbiente Externo\033[m'))
                print('Professor(a): {}\n'.format('\033[33mDaniel Lins\033[m'))
                print('Link do conteúdo: \033[33mhttps://www.youtube.com/watch?v=bS_I2xpFzFU&feature=youtu.be\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=bS_I2xpFzFU&feature=youtu.be')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
            if opcao_assunto == 3:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mTomada de Decisão Administrativa\033[m'))
                print('Professor(a): {}\n'.format('\033[33mDaniel Lins\033[m'))
                print('Link do conteúdo: \033[33mhttps://www.youtube.com/watch?v=G0QXXaj9554\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=G0QXXaj9554')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
            if opcao_assunto == 4:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mÉtica e Responsabilidade Empresarial\033[m'))
                print('Professor(a): {}\n'.format('\033[33mDaniel Lins\033[m'))
                print('Link do conteúdo: \033[33mhttps://drive.google.com/file/d/1OdZvXYFu0HWFQb5pAA1v7VHWvqe7e5fd/view\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://drive.google.com/file/d/1OdZvXYFu0HWFQb5pAA1v7VHWvqe7e5fd/view')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
        if opcao == 3:
            print('=' * 50)
            print('{:^50}'.format('Assuntos - BSI'))
            print('=' * 50)
            print('\n1 - Representações de um algoritmo\n2 - Lógica de Programação\n3 - Introdução ao Python\n')
            opcao_assunto = int(input('Insira o valor correspondente ao assunto desejado: '))
            if opcao_assunto == 1:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mRepresentações de um algoritmo\033[m'))
                print('Professor(a): {}\n'.format('\033[33mIuri Sônego Cardoso\033[m'))
                print('Link do conteúdo: \033[33mhttps://www.youtube.com/watch?v=Wt7Pv9kjdWk&t=18s\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=Wt7Pv9kjdWk&t=18s')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
            if opcao_assunto == 2:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mLógica de Programação\033[m'))
                print('Professor(a): {}\n'.format('\033[33mGustavo Guanabara (Curso em Vídeo)\033[m'))
                print('Link do conteúdo: \033[33mhttps://www.youtube.com/watch?v=8mei6uVttho&list=PLHz_AreHm4dmSj0MHol_aoNYCSGFqvfXV\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=8mei6uVttho&list=PLHz_AreHm4dmSj0MHol_aoNYCSGFqvfXV')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
            if opcao_assunto == 3:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mIntrodução ao Python\033[m'))
                print('Professor(a): {}\n'.format('\033[33mGustavo Guanabara (Curso em Vídeo)\033[m'))
                print('Link do conteúdo: \033[33mhttps://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
        if opcao == 4:
            print('=' * 50)
            print('{:^50}'.format('Assuntos - BSI'))
            print('=' * 50)
            print('\n1 - Papel dos SIs na Sustentabilidade\n2 - Economia Digital e seus reflexos sustentáveis\n3 - Impactos Sociais das Tecnologias\n4 - Tecnologia e Meio Ambiente\n5 - TI Verde\n')
            opcao_assunto = int(input('Insira o valor correspondente ao assunto desejado: '))
            if opcao_assunto == 1:
                limpar_tela()
                # A adicionar
                print('Assunto: {}\n'.format('\033[33mPapel dos SIs na Sustentabilidade\033[m'))
                print('Professor(a): {}\n'.format('\033[33mIuri Sônego Cardoso\033[m'))
                print('Link do conteúdo: \033[33mhttps://www.youtube.com/watch?v=Wt7Pv9kjdWk&t=18s\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=Wt7Pv9kjdWk&t=18s')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
            if opcao_assunto == 2:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mEconomia Digital e seus reflexos sustentáveis\033[m'))
                print('Professor(a): {}\n'.format('\033[33mFundação Dom Cabral\033[m'))
                print('Link do conteúdo: \033[33mhttps://www.youtube.com/watch?v=v0MJbh6av5o\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=v0MJbh6av5o')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
            if opcao_assunto == 3:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mImpactos Sociais das Tecnologias\033[m'))
                print('Professor(a): {}\n'.format('\033[33mRomulo Bolivar\033[m'))
                print('Link do conteúdo: \033[33mhttps://www.youtube.com/watch?v=2Z_UP9VsWl4\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=2Z_UP9VsWl4')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
            if opcao_assunto == 4:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mTecnologia e Meio Ambiente\033[m'))
                print('Professor(a): {}\n'.format('\033[33mRuptura\033[m'))
                print('Link do conteúdo: \033[33mhttps://www.youtube.com/watch?v=OT52nq0VDqo\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=OT52nq0VDqo')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
            if opcao_assunto == 5:
                limpar_tela()
                print('Assunto: {}\n'.format('\033[33mTI Verde\033[m'))
                print('Professor(a): {}\n'.format('\033[33mBóson Treinamentos\033[m'))
                print('Link do conteúdo: \033[33mhttps://www.youtube.com/watch?v=8igyusXZ-5I\033[m\n')
                print('Sinopse: {}'.format('Nesta coletânea do assunto de Grafos, são abordados o conceito de Grafo, Tipos de grafos, sua utilizade na área de TI, dentre outras coisas.\n'))
                acessar = int(input('Quer ser redirecionado para o vídeo? (1 - Sim/ 0 - Não)'))
                if acessar == 1:
                    webbrowser.open('https://www.youtube.com/watch?v=8igyusXZ-5I')
                elif acessar == 0:
                    limpar_tela()
                    return
                else:
                    print('A opção escolhida é inexistente!')
                    return
            
