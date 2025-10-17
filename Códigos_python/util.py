from os import system, name


def limpar_tela():
    system('cls' if name == 'nt' else 'clear')