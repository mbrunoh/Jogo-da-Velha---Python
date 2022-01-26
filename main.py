from os import system
from random import randint
cor_vermelho = '\033[0;31m';
cor_vermelhoclaro = '\033[0;95m';
cor_azul = '\033[0;34m';
cor_azulclaro = '\033[0;96m';
cor_cinza = '\033[0;90m';
cor_amarelo = '\033[0;33m';
cor_ganhou = '\033[;7m';
cor_padrao = '\033[0;0m';
cor_f = '\033[m';
corplayer = [cor_azul, cor_vermelho]
vez = randint(0, 1);
velha = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '];
velha_mostrar = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '];
velhanum = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
cori = ['', '', '', '', '', '', '', '', ''];
corf = ['', '', '', '', '', '', '', '', ''];
jogadores = ['Player 1', 'Computador'];
operador = ['X', 'O'];
placar = [0, 0, 0];
dificuldade = 1;
dif = 'Fácil';
tipo = 0;
vitoria = 0;

def menu():
    system('clear');
    cabecalho()
    print('1 - Iniciar Jogo');
    print(f'2 - Mudar nome do(a) {cor_azul}{jogadores[0]}{cor_f}');
    print('3 - Mudar Dificuldade');
    print('4 - Resetar Placar');
    if dificuldade == 3:
        print(f'5 - Mudar nome do(a) {cor_vermelho}{jogadores[1]}{cor_f}');
    print('0 - Sair');
    print(41 * '~');
    print('Opção desejada:');
    opc = input();
    try:
        opc = int(opc);
    except ValueError:
        menu();
    else:
        opc = int(opc);
        if opc == 1:
            iniciar_jogo();
        elif opc == 2:
            cadastrar_nome1();
        elif opc == 3:
            sel_dificuldade();
        elif opc == 4:
            resetar_placar();
            menu();
        elif dificuldade == 3 and opc == 5:
            cadastrar_nome2();
        elif opc == 0:
            exit();
        else: menu();
def cabecalho():
    print(41 * '~');
    print(14*f'{cor_ganhou} {cor_f}'+f'{cor_ganhou}JOGO DA VELHA{cor_f}'+14*f'{cor_ganhou} {cor_f}');
    print(41 * '~');
    print(f'Jogador: {cor_azul}{jogadores[0]}{cor_f}');
    if dificuldade == 1:
        print(f'Dificuldade: {cor_azulclaro}{dif}{cor_f}')
    elif dificuldade == 2:
        print(f'Dificuldade: {cor_vermelhoclaro}{dif}{cor_f}')
    elif dificuldade == 3:
        print(f'Dificuldade: {cor_vermelho}{dif}{cor_f}')
    else:
        print(f'Dificuldade: {dif}')
    print(f'{cor_azul}{jogadores[0]}: {placar[0]}{cor_f} || {cor_vermelho}{jogadores[1]}: {placar[1]}{cor_f} || Empates: {placar[2]}');
    print(41 * '~');
def mostrar_tabela():
    y = 0;
    for i in velha:
        if velha[y] == ' ':
            velha_mostrar[y] = velhanum[y];
        else:
            velha_mostrar[y] = velha[y];
        y += 1;
    pintar();
    cabecalho()
    print(f'{cori[0]} {velha_mostrar[0]} {corf[0]}|{cori[1]} {velha_mostrar[1]} {corf[1]}|{cori[2]} {velha_mostrar[2]} {corf[2]}');
    print(f'{cori[3]} {velha_mostrar[3]} {corf[3]}|{cori[4]} {velha_mostrar[4]} {corf[4]}|{cori[5]} {velha_mostrar[5]} {corf[5]}');
    print(f'{cori[6]} {velha_mostrar[6]} {corf[6]}|{cori[7]} {velha_mostrar[7]} {corf[7]}|{cori[8]} {velha_mostrar[8]} {corf[8]}');
    print(12 * '~');
def iniciar_jogo():
    resetar();
    rodada();
def jogar_novamente():
    print('Deseja jogar novamente? (s/n)');
    opc = str(input());
    if opc == 'n' or opc == 'N':
        system('clear');
        menu();
    elif opc == 's' or opc == 'S':
        iniciar_jogo();
    else:
        verificar_vitoria();
def rodada():
    global vez
    system('clear');
    mostrar_tabela();
    if vez % 2 == 0:
        player1_jogada();
    elif dificuldade == 1:
        a_jogada();
    elif dificuldade == 2:
        ia_jogada();
    elif dificuldade == 3:
        player2_jogada();
    verificar_vitoria();
    vez = vez + 1;
    rodada();
def sel_dificuldade():
    global dificuldade
    global dif
    global jogadores
    system('clear');
    cabecalho();
    if placar[0] != 0 or placar[1] != 0 or placar[2] != 0:
        print('O placar será resetado! Deseja continuar? (s/n)')
        des = str(input());
    if (placar[0] != 0 or placar[1] != 0 or placar[2] != 0) and (des == 's' or des == 'S'):
        resetar_placar();
        sel_dificuldade();
    elif (placar[0] != 0 or placar[1] != 0 or placar[2] != 0) and (des != 's' or des != 'S'):
        menu();
    else:
        system('clear');
        cabecalho();
        print(f'1 - {cor_azulclaro}Fácil{cor_f}');
        print(f'2 - {cor_vermelhoclaro}Difícil{cor_f}');
        print(f'3 - {cor_vermelho}Multiplayer{cor_f}');
        print(12 * '~');
        print('Selecione a dificuldade:');
        opc = input();
        try:
            opc = int(opc);
        except ValueError:
            sel_dificuldade();
        else:
            opc = int(opc);
            if opc != dificuldade:
                if opc == 1:
                    dif = 'Facil';
                    jogadores[1] = 'Computador';
                    dificuldade = 1;
                elif opc == 2:
                    dif = 'Difícil';
                    jogadores[1] = 'Computador';
                    dificuldade = 2;
                elif opc == 3:
                    dif = 'Multiplayer';
                    if opc != dificuldade:
                        jogadores[1] = 'Player 2';
                    dificuldade = 3;
                resetar_placar();
            if opc != dificuldade:
                resetar_placar();
            if opc == 1:
                dif = 'Facil';
                jogadores[1] = 'Computador';
                dificuldade = 1;
            elif opc == 2:
                dif = 'Difícil';
                jogadores[1] = 'Computador';
                dificuldade = 2;
            elif opc == 3:
                dif = 'Multiplayer';
                if opc != dificuldade:
                    jogadores[1] = 'Player 2';
                dificuldade = 3;
            else:
                sel_dificuldade();
            menu();
def pintar():
    global tipo
    global vez
    w = 0
    for i in velha_mostrar:
        if i == velhanum[w]:
            cori[w] = cor_cinza
            corf[w] = cor_f;
        w = w + 1;
    z = 0;
    for i in velha_mostrar:
        if i == 'X':
            cori[z] = cor_azul;
            corf[z] = cor_f;
        elif i == 'O':
            cori[z] = cor_vermelho;
            corf[z] = cor_f;
        z = z + 1;
    if vitoria == 1:
        x = cor_ganhou;
        xf = cor_f;
        if tipo == 1:
            cori[0] = x;
            cori[1] = x;
            cori[2] = x;
            corf[0] = xf;
            corf[1] = xf;
            corf[2] = xf;
        elif tipo == 2:
            cori[3] = x;
            cori[4] = x;
            cori[5] = x;
            corf[3] = xf;
            corf[4] = xf;
            corf[5] = xf;
        elif tipo == 3:
            cori[6] = x;
            cori[7] = x;
            cori[8] = x;
            corf[6] = xf;
            corf[7] = xf;
            corf[8] = xf;
        elif tipo == 4:
            cori[0] = x;
            cori[3] = x;
            cori[6] = x;
            corf[0] = xf;
            corf[3] = xf;
            corf[6] = xf;
        elif tipo == 5:
            cori[1] = x;
            cori[4] = x;
            cori[7] = x;
            corf[1] = xf;
            corf[4] = xf;
            corf[7] = xf;
        elif tipo == 6:
            cori[2] = x;
            cori[5] = x;
            cori[8] = x;
            corf[2] = xf;
            corf[5] = xf;
            corf[8] = xf;
        elif tipo == 7:
            cori[0] = x;
            cori[4] = x;
            cori[8] = x;
            corf[0] = xf;
            corf[4] = xf;
            corf[8] = xf;
        elif tipo == 8:
            cori[2] = x;
            cori[4] = x;
            cori[6] = x;
            corf[2] = xf;
            corf[4] = xf;
            corf[6] = xf;
def verificar_vitoria():
    global vitoria
    global placar
    global tipo
    global vez
    system('clear');
    if velha[0] != ' ' and velha[0] == velha[1] == velha[2]:
        vitoria = 1;
        tipo = 1;
    elif velha[3] != ' ' and velha[3] == velha[4] == velha[5]:
        vitoria = 1;
        tipo = 2;
    elif velha[6] != ' ' and velha[6] == velha[7] == velha[8]:
        vitoria = 1;
        tipo = 3;
    elif velha[0] != ' ' and velha[0] == velha[3] == velha[6]:
        vitoria = 1;
        tipo = 4;
    elif velha[1] != ' ' and velha[1] == velha[4] == velha[7]:
        vitoria = 1;
        tipo = 5;
    elif velha[2] != ' ' and velha[2] == velha[5] == velha[8]:
        vitoria = 1;
        tipo = 6;
    elif velha[0] != ' ' and velha[0] == velha[4] == velha[8]:
        vitoria = 1;
        tipo = 7;
    elif velha[2] != ' ' and velha[2] == velha[4] == velha[6]:
        vitoria = 1;
        tipo = 8;
    elif velha[0] != ' ' and velha[1] != ' ' and velha[2] != ' ' and velha[3] != ' ' and velha[4] != ' ' and velha[5] != ' ' and velha[6] != ' ' and velha[7] != ' ' and velha[8] != ' ':
        vitoria = 3;
    else: vitoria = 0;
    if vitoria == 1:
        if vez % 2 == 0:
            w = corplayer[vez % 2];
        elif vez % 2 == 1:
            w = corplayer[vez % 2];
        placar[vez % 2] += 1;
        mostrar_tabela();
        print(f'{w}{jogadores[vez % 2]}{cor_f} é o Vencedor!');
        jogar_novamente();
    elif vitoria == 3:
        mostrar_tabela();
        print('Empate! Deu Velha.');
        placar[2] += 1;
        jogar_novamente();
def player1_jogada():
    global velha
    global vez
    print(f'{corplayer[vez % 2]}{jogadores[vez % 2]} sua vez! Digite sua jogada{cor_f}:');
    x = input()
    try:
        x = int(x);
    except ValueError:
        player1_jogada();
    else:
        x = int(x);
        if x < 1 or x > 9:
            player1_jogada();
        elif velha[x-1] != ' ':
            player1_jogada();
        else:
            gravar_velha(x-1);
def player2_jogada():
    global velha
    global vez
    print(f'{corplayer[vez % 2]}{jogadores[vez % 2]} sua vez! Digite sua jogada{cor_f}:');
    x = input();
    try:
        x = int(x);
    except ValueError:
        player1_jogada();
    else:
        x = int(x);
        if x < 1 or x > 9:
            player1_jogada();
        elif velha[x - 1] != ' ':
            player1_jogada();
        else:
            gravar_velha(x-1);
def a_jogada():
    global velha
    global vez
    print(f'{corplayer[vez % 2]}Vez do {jogadores[1]}{cor_f}!');
    y = randint(0, 8);
    while velha[y] != ' ':
        y = randint(0, 8);
    gravar_velha(y);
def ia_jogada():
    global velha
    global vez
    print(f'{corplayer[vez % 2]}Vez do {jogadores[1]}{cor_f}!');

    if velha[1] == 'O' and velha[1] == velha[2] and velha[0] == ' ':
        gravar_velha(0);
    elif velha[3] == 'O' and velha[3] == velha[6] and velha[0] == ' ':
        gravar_velha(0);
    elif velha[4] == 'O' and velha[4] == velha[8] and velha[0] == ' ':
        gravar_velha(0);
    elif velha[0] == 'O' and velha[0] == velha[2] and velha[1] == ' ':
        gravar_velha(1);
    elif velha[4] == 'O' and velha[4] == velha[7] and velha[1] == ' ':
        gravar_velha(1);
    elif velha[0] == 'O' and velha[0] == velha[1] and velha[2] == ' ':
        gravar_velha(2);
    elif velha[5] == 'O' and velha[5] == velha[8] and velha[2] == ' ':
        gravar_velha(2);
    elif velha[6] == 'O' and velha[6] == velha[4] and velha[2] == ' ':
        gravar_velha(2);
    elif velha[4] == 'O' and velha[4] == velha[5] and velha[3] == ' ':
        gravar_velha(3);
    elif velha[0] == 'O' and velha[0] == velha[6] and velha[3] == ' ':
        gravar_velha(3);
    elif velha[3] == 'O' and velha[3] == velha[5] and velha[4] == ' ':
        gravar_velha(4);
    elif velha[1] == 'O' and velha[1] == velha[7] and velha[4] == ' ':
        gravar_velha(4);
    elif velha[0] == 'O' and velha[0] == velha[8] and velha[4] == ' ':
        gravar_velha(4);
    elif velha[6] == 'O' and velha[6] == velha[2] and velha[4] == ' ':
        gravar_velha(4);
    elif velha[2] == 'O' and velha[2] == velha[8] and velha[5] == ' ':
        gravar_velha(5);
    elif velha[3] == 'O' and velha[3] == velha[4] and velha[5] == ' ':
        gravar_velha(5);
    elif velha[0] == 'O' and velha[0] == velha[3] and velha[6] == ' ':
        gravar_velha(6);
    elif velha[7] == 'O' and velha[7] == velha[8] and velha[6] == ' ':
        gravar_velha(6);
    elif velha[4] == 'O' and velha[4] == velha[2] and velha[6] == ' ':
        gravar_velha(6);
    elif velha[1] == 'O' and velha[1] == velha[4] and velha[7] == ' ':
        gravar_velha(7);
    elif velha[6] == 'O' and velha[6] == velha[8] and velha[7] == ' ':
        gravar_velha(7);
    elif velha[2] == 'O' and velha[2] == velha[5] and velha[8] == ' ':
        gravar_velha(8);
    elif velha[6] == 'O' and velha[6] == velha[7] and velha[8] == ' ':
        gravar_velha(8);
    elif velha[0] == 'O' and velha[0] == velha[4] and velha[8] == ' ':
        gravar_velha(8);
    elif velha[1] != ' ' and velha[1] == velha[2] and velha[0] == ' ':
        gravar_velha(0);
    elif velha[3] != ' ' and velha[3] == velha[6] and velha[0] == ' ':
        gravar_velha(0);
    elif velha[4] != ' ' and velha[4] == velha[8] and velha[0] == ' ':
        gravar_velha(0);
    elif velha[0] != ' ' and velha[0] == velha[2] and velha[1] == ' ':
        gravar_velha(1);
    elif velha[4] != ' ' and velha[4] == velha[7] and velha[1] == ' ':
        gravar_velha(1);
    elif velha[0] != ' ' and velha[0] == velha[1] and velha[2] == ' ':
        gravar_velha(2);
    elif velha[5] != ' ' and velha[5] == velha[8] and velha[2] == ' ':
        gravar_velha(2);
    elif velha[6] != ' ' and velha[6] == velha[4] and velha[2] == ' ':
        gravar_velha(2);
    elif velha[4] != ' ' and velha[4] == velha[5] and velha[3] == ' ':
        gravar_velha(3);
    elif velha[0] != ' ' and velha[0] == velha[6] and velha[3] == ' ':
        gravar_velha(3);
    elif velha[3] != ' ' and velha[3] == velha[5] and velha[4] == ' ':
        gravar_velha(4);
    elif velha[1] != ' ' and velha[1] == velha[7] and velha[4] == ' ':
        gravar_velha(4);
    elif velha[0] != ' ' and velha[0] == velha[8] and velha[4] == ' ':
        gravar_velha(4);
    elif velha[6] != ' ' and velha[6] == velha[2] and velha[4] == ' ':
        gravar_velha(4);
    elif velha[2] != ' ' and velha[2] == velha[8] and velha[5] == ' ':
        gravar_velha(5);
    elif velha[3] != ' ' and velha[3] == velha[4] and velha[5] == ' ':
        gravar_velha(5);
    elif velha[0] != ' ' and velha[0] == velha[3] and velha[6] == ' ':
        gravar_velha(6);
    elif velha[7] != ' ' and velha[7] == velha[8] and velha[6] == ' ':
        gravar_velha(6);
    elif velha[4] != ' ' and velha[4] == velha[2] and velha[6] == ' ':
        gravar_velha(6);
    elif velha[1] != ' ' and velha[1] == velha[4] and velha[7] == ' ':
        gravar_velha(7);
    elif velha[6] != ' ' and velha[6] == velha[8] and velha[7] == ' ':
        gravar_velha(7);
    elif velha[2] != ' ' and velha[2] == velha[5] and velha[8] == ' ':
        gravar_velha(8);
    elif velha[6] != ' ' and velha[6] == velha[7] and velha[8] == ' ':
        gravar_velha(8);
    elif velha[0] != ' ' and velha[0] == velha[4] and velha[8] == ' ':
        gravar_velha(8);
    elif velha[4] == 'O' and velha[0] == 'O' and velha[3] == ' ':
        gravar_velha(3);
    elif velha[4] == 'O' and velha[0] == 'O' and velha[1] == ' ':
        gravar_velha(1);
    elif velha[4] == 'O' and velha[6] == 'O' and velha[3] == ' ':
        gravar_velha(3);
    elif velha[4] == 'O' and velha[6] == 'O' and velha[7] == ' ':
        gravar_velha(7);
    elif velha[4] == 'O' and velha[8] == 'O' and velha[7] == ' ':
        gravar_velha(7);
    elif velha[4] == 'O' and velha[8] == 'O' and velha[5] == ' ':
        gravar_velha(5);
    elif velha[4] == 'O' and velha[2] == 'O' and velha[5] == ' ':
        gravar_velha(5);
    elif velha[4] == 'O' and velha[2] == 'O' and velha[1] == ' ':
        gravar_velha(1);
    elif velha[4] == ' ':
        gravar_velha(4);
    elif velha[0] == 'X' or velha[2] == 'X' or velha[6] == 'X' or velha[8] == 'X':
        if velha[1] == ' ':
            gravar_velha(1);
        elif velha[3] == ' ':
            gravar_velha(3);
        elif velha[5] == ' ':
            gravar_velha(5);
        elif velha[7] == ' ':
            gravar_velha(7);
    elif velha[0] == ' ':
        gravar_velha(0);
    elif velha[2] == ' ':
        gravar_velha(2);
    elif velha[6] == ' ':
        gravar_velha(6);
    elif velha[8] == ' ':
        gravar_velha(8);
    else:
        y = randint(0, 8);
        while velha[y] != ' ':
            y = randint(0, 8);
        if velha[y] == ' ':
            gravar_velha(y);
        else: ia_jogada();
def resetar():
    system('clear');
    global velha
    global jogadores
    global vez
    global cori
    global corf
    global vitoria
    global jogadores
    vitoria = 0;
    vez = randint(1, 2);
    for i in cori:
        i = cor_padrao;
    cori = ['', '', '', '', '', '', '', '', ''];
    corf = ['', '', '', '', '', '', '', '', ''];
    velha = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '];
def cadastrar_nome1():
    global jogadores
    system('clear');
    cabecalho();
    print('Digite seu nome Player 1:');
    jogadores[0] = str(input());
    menu();
def cadastrar_nome2():
    global jogadores
    system('clear');
    cabecalho();
    print('Digite seu nome Player 2:');
    jogadores[1] = str(input());
    menu();
def resetar_placar():
    global placar;
    system('clear');
    cabecalho();
    placar = [0, 0, 0];
def gravar_velha(x):
    velha[x] = operador[vez % 2];

menu();