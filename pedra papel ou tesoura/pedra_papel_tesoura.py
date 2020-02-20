from random import randint
from multithread import thread_vitoria, thread_empate, thread_perdeu ##Importando do script "multithread".

def jogo():
    while True:
        escolhas = ('pedra', 'papel', 'tesoura')
        pc_escolha = randint(0, 2)
        menu_jogo = int(input('Para jogar o jogo pressione (1) \nPara sair do jogo pressione (2)\nQuer jogar ou sair do jogo?: '))
        if menu_jogo == 1:
            jogador_escolha = int(input('0º:Pedra\n1º:Papel\n2ºTesoura\nSua escolha: ')) ##Escolha do úsuario em questão
            print('Sua escolha foi: {}'.format(escolhas[jogador_escolha]))
            print('Escolha do seu oponente: {}'.format(escolhas[pc_escolha]))
            if pc_escolha == 0: ##Em relação a escolha do computador
                if jogador_escolha == 0:
                    thread_empate()
                    print('Foi um empate')
                elif jogador_escolha == 1:
                    thread_vitoria()
                    print('Você ganhou')
                elif jogador_escolha == 2:
                    thread_perdeu()
                    print('Você perdeu')
                else:
                    print('Jogada invalida')
            elif pc_escolha == 1:
                if jogador_escolha == 0:
                    thread_perdeu()
                    print('Você você perdeu')
                elif jogador_escolha == 1:
                    thread_empate()
                    print('Empate')
                elif jogador_escolha == 2:
                    thread_vitoria()
                    print('Você ganhou')
            elif pc_escolha == 2:
                if jogador_escolha == 0:
                    thread_vitoria()
                    print('Você Ganhou')
                elif jogador_escolha == 1:
                    thread_perdeu()
                    print('Você perdeu')
                elif jogador_escolha == 2:
                    thread_empate()
                    print('Empate')
            else:
                print('Jogada Invalida') ##Ainda não achei um método para fazer esse else funcionar de maneira correta.
        elif menu_jogo == 2:
            exit()
        else:
            print('Opção invalida')
jogo()
