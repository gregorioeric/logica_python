energia = 100  # Energia inicial do personagem

while energia > 0:  # Enquanto a energia for maior que 0, o jogo continua
    print(f"\nEnergia atual: {energia}")

    # Escolha do jogador
    print("Escolha uma ação: ")
    print("1 - Correr (-20 de energia)")
    print("2 - Comer (+30 de energia)")
    print("3 - Descansar (+10 de energia)")
    print("4 - Lutar (-50 de energia)")
    print("5 - Sair")

    opcao = int(input("Digite o número da ação: "))

    if opcao == 1:
        energia -= 20  # Perde energia ao correr
        print("Você correu e gastou energia.")
    elif opcao == 2:
        energia += 30  # Ganha energia ao comer
        print("Você comeu e recuperou energia.")
    elif opcao == 3:
        energia += 10  # Ganha um pouco de energia ao descansar
        print("Você descansou e recuperou um pouco de energia.")
    elif opcao == 4:
        energia -= 50  # Perde muita energia ao lutar
        print("Você lutou e gastou muita energia!")
    elif opcao == 5:
        print("Você decidiu sair do jogo.")
        break  # Sai do loop e encerra o jogo
    else:
        print("Opção inválida, tente novamente.")

    # Impedir que a energia ultrapasse 100
    # if energia > 200:
    #     energia = 200

if energia <= 0:
    print("\nSua energia acabou! Fim de jogo.")
