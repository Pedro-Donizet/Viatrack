print("ola caro passageiro, nós da ViaTrak ficamos contente em atendelo."
      "\ncomo poderiamos te ajudar?")

op = int(input("\n1. Atrasos no trem"
                 "\n2. Super lotação"
                 "\n3. Problemas com passageiros"
                 "\n4. Venda Ilegal de produtos no vagão"
                 "\n5. Vagão sujo ou comprometido"
                 "\n6. Ótima velocidade"
                 "\n7. Ótima limpeza"
                 "\n8. Ótimo trabalho dos guardas"
                 "\n9. Ótimo conforto no vagão"
                 "\ninsira qual Feedback deseja realatar:"))
match op:
    case 1:
        print("\nObrigado pelo Feedback! Sentimos muito, resolveremos isso logo.")
    case 2:
        print("\nObrigado pelo Feedback! Sentimos muito, resolveremos isso logo")
    case 3:
        print("\nObrigado pelo Feedback! Fique longe!"
              "\nEm caso de extrema confusão saia ou troque de vagão, sua segurança em primeiro lugar")
    case 4:
        input("\nInsira em qual a proxima estação para que podemos assionar as autoridades: ")
        print("\nObrigado pelo Feedback! Sentimos muito, resolveremos isso logo")
    case 5:
        input("\ninsira o codigo do vagão que você esta para que podemos assionar a limpeza: ")
        print("\nObrigado pelo Feedback! Sentimos muito, resolveremos isso logo")
    case 6:
        print("\nFicamos feliz com sua satisfação!! Obirgado pelo Feedback!")
    case 7:
        print("\nFicamos feliz com sua satisfação!! Obirgado pelo Feedback!")
    case 8:
        print("\nFicamos feliz com sua satisfação!! Obirgado pelo Feedback!")
    case 9:
        print("\nFicamos feliz com sua satisfação!! Obirgado pelo Feedback!")
    case _:
        print("\nOpção inválida. Por favor, insira um número de 1 a 9.")

