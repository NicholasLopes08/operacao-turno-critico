from auxiliares import buscar_pedido, buscar_entregador, contar_pedidos_ativos

def alterar_status_pedido():
    print("\n--- ALTERAR STATUS DO PEDIDO ---")

    id_pedido = input("ID do pedido: ").strip().upper()
    pedido = buscar_pedido(id_pedido)

    if pedido == None:
        print("Pedido nao encontrado.")
        return

    print("Novo status: Pendente, Em Rota, Entregue ou Cancelado")
    novo_status = input("Novo status: ").strip()

    if novo_status != "Pendente" and novo_status != "Em Rota" and novo_status != "Entregue" and novo_status != "Cancelado":
        print("Status invalido.")
        return

    if pedido["status"] == "Entregue" and novo_status == "Pendente":
        print("Erro: Pedido entregue nao pode voltar para Pendente.")
        return

    pedido["status"] = novo_status
    print("Status atualizado com sucesso!")

def cancelar_pedido():
    print("\n--- CANCELAR PEDIDO ---")

    id_pedido = input("ID do pedido: ").strip().upper()
    pedido = buscar_pedido(id_pedido)

    if pedido == None:
        print("Pedido nao encontrado.")
        return

    pedido["status"] = "Cancelado"
    print("Pedido cancelado com sucesso!")

def associar_entregador_pedido():
    print("\n--- ASSOCIAR ENTREGADOR AO PEDIDO ---")

    id_pedido = input("ID do pedido: ").strip().upper()
    pedido = buscar_pedido(id_pedido)

    if pedido == None:
        print("Pedido nao encontrado.")
        return

    if pedido["status"] == "Cancelado":
        print("Erro: Pedido cancelado nao pode ser associado a entregador.")
        return

    id_entregador = input("ID do entregador: ").strip()
    entregador = buscar_entregador(id_entregador)

    if entregador == None:
        print("Entregador nao encontrado.")
        return

    if entregador["disponibilidade"] != "disponivel":
        print("Erro: Entregador indisponivel.")
        return

    ativos = contar_pedidos_ativos(entregador)
    if ativos >= 3:
        print("Erro: Entregador ja possui 3 pedidos ativos.")
        return

    pedido["id_entregador"] = id_entregador
    pedido["status"] = "Em Rota"

    ja_esta_na_lista = False
    for id_na_lista in entregador["pedidos_associados"]:
        if id_na_lista == id_pedido:
            ja_esta_na_lista = True

    if ja_esta_na_lista == False:
        entregador["pedidos_associados"].append(id_pedido)

    print("Entregador associado. Pedido em rota!")

def remover_entregador_pedido():
    print("\n--- REMOVER ENTREGADOR DO PEDIDO ---")

    id_pedido = input("ID do pedido: ").strip().upper()
    pedido = buscar_pedido(id_pedido)

    if pedido == None:
        print("Pedido nao encontrado.")
        return

    if pedido["id_entregador"] == "":
        print("Pedido nao possui entregador associado.")
        return

    id_entregador = pedido["id_entregador"]
    entregador = buscar_entregador(id_entregador)

    pedido["id_entregador"] = ""
    pedido["status"] = "Pendente"

    if entregador != None:
        nova_lista = []
        for id_na_lista in entregador["pedidos_associados"]:
            if id_na_lista != id_pedido:
                nova_lista.append(id_na_lista)
        entregador["pedidos_associados"] = nova_lista

    print("Entregador removido. Pedido voltou para Pendente.")

def menu_atualizacao_pedidos():
    opcao = ""
    while opcao != "0":
        print("\n--- ATUALIZACAO DE PEDIDOS ---")
        print("1 - Alterar status")
        print("2 - Cancelar pedido")
        print("3 - Associar entregador")
        print("4 - Remover entregador")
        print("0 - Voltar")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            alterar_status_pedido()
        elif opcao == "2":
            cancelar_pedido()
        elif opcao == "3":
            associar_entregador_pedido()
        elif opcao == "4":
            remover_entregador_pedido()
        elif opcao == "0":
            print("Voltando ao menu principal...")
        else:
            print("Opcao invalida.")
