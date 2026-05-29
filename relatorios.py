from dados import pedidos, entregadores
from auxiliares import buscar_pedido

def relatorio_total_pedidos():
    print("\n--- TOTAL DE PEDIDOS ---")
    print("Total:", len(pedidos))

def relatorio_pedidos_por_status():
    print("\n--- PEDIDOS POR STATUS ---")

    pendente = 0
    em_rota = 0
    entregue = 0
    cancelado = 0

    for pedido in pedidos:
        if pedido["status"] == "Pendente":
            pendente = pendente + 1
        elif pedido["status"] == "Em Rota":
            em_rota = em_rota + 1
        elif pedido["status"] == "Entregue":
            entregue = entregue + 1
        elif pedido["status"] == "Cancelado":
            cancelado = cancelado + 1

    print("Pendente:", pendente)
    print("Em Rota:", em_rota)
    print("Entregue:", entregue)
    print("Cancelado:", cancelado)

def relatorio_prioridade_alta():
    print("\n--- PEDIDOS COM PRIORIDADE ALTA ---")
    encontrou = False

    for pedido in pedidos:
        if pedido["prioridade"] == "Alta":
            encontrou = True
            print(pedido["id"], "-", pedido["status"], "-", pedido["nome_cliente"])

    if encontrou == False:
        print("Nenhum pedido com prioridade alta.")

def relatorio_mais_entregas():
    print("\n--- ENTREGADOR COM MAIS ENTREGAS ---")

    if len(entregadores) == 0:
        print("Nenhum entregador cadastrado.")
        return

    maior = -1
    id_melhor = ""
    nome_melhor = ""

    for entregador in entregadores:
        entregas = 0

        for id_pedido in entregador["pedidos_associados"]:
            pedido = buscar_pedido(id_pedido)
            if pedido != None:
                if pedido["status"] == "Entregue":
                    entregas = entregas + 1

        if entregas > maior:
            maior = entregas
            id_melhor = entregador["id"]
            nome_melhor = entregador["nome"]

    print("Entregador:", nome_melhor)
    print("ID:", id_melhor)
    print("Total de entregas:", maior)

def menu_relatorios():
    opcao = ""
    while opcao != "0":
        print("\n--- RELATORIOS OPERACIONAIS ---")
        print("1 - Total de pedidos")
        print("2 - Pedidos por status")
        print("3 - Pedidos com prioridade alta")
        print("4 - Entregador com mais entregas")
        print("0 - Voltar")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            relatorio_total_pedidos()
        elif opcao == "2":
            relatorio_pedidos_por_status()
        elif opcao == "3":
            relatorio_prioridade_alta()
        elif opcao == "4":
            relatorio_mais_entregas()
        elif opcao == "0":
            print("Voltando ao menu principal...")
        else:
            print("Opcao invalida.")
