from dados import pedidos, entregadores
from auxiliares import buscar_pedido, buscar_entregador

def listar_pedidos_pendentes():
    print("\n--- PEDIDOS PENDENTES ---")
    encontrou = False

    for pedido in pedidos:
        if pedido["status"] == "Pendente":
            encontrou = True
            print(pedido["id"], "-", pedido["nome_cliente"], "-", pedido["prioridade"])

    if encontrou == False:
        print("Nenhum pedido pendente.")

def listar_pedidos_entregues():
    print("\n--- PEDIDOS ENTREGUES ---")
    encontrou = False

    for pedido in pedidos:
        if pedido["status"] == "Entregue":
            encontrou = True
            print(pedido["id"], "-", pedido["nome_cliente"])

    if encontrou == False:
        print("Nenhum pedido entregue.")

def buscar_pedido_por_id():
    print("\n--- BUSCAR PEDIDO ---")

    id_pedido = input("ID do pedido: ").strip().upper()
    pedido = buscar_pedido(id_pedido)

    if pedido == None:
        print("Pedido nao encontrado.")
        return

    print("ID:", pedido["id"])
    print("Cliente:", pedido["nome_cliente"])
    print("Endereco:", pedido["endereco"])
    print("Prioridade:", pedido["prioridade"])
    print("Descricao:", pedido["descricao"])
    print("Status:", pedido["status"])
    print("Entregador:", pedido["id_entregador"])

def listar_entregadores_disponiveis():
    print("\n--- ENTREGADORES DISPONIVEIS ---")
    encontrou = False

    for entregador in entregadores:
        if entregador["disponibilidade"] == "disponivel":
            encontrou = True
            print(entregador["id"], "-", entregador["nome"], "-", entregador["veiculo"])

    if encontrou == False:
        print("Nenhum entregador disponivel.")

def mostrar_entregas_entregador():
    print("\n--- ENTREGAS DO ENTREGADOR ---")

    id_entregador = input("ID do entregador: ").strip()
    entregador = buscar_entregador(id_entregador)

    if entregador == None:
        print("Entregador nao encontrado.")
        return

    print("Entregador:", entregador["nome"])

    if len(entregador["pedidos_associados"]) == 0:
        print("Nenhum pedido associado.")
        return

    for id_pedido in entregador["pedidos_associados"]:
        pedido = buscar_pedido(id_pedido)
        if pedido != None:
            print(id_pedido, "-", pedido["status"], "-", pedido["nome_cliente"])

def menu_consultas():
    opcao = ""
    while opcao != "0":
        print("\n--- CONSULTAS ---")
        print("1 - Listar pedidos pendentes")
        print("2 - Listar pedidos entregues")
        print("3 - Buscar pedido por ID")
        print("4 - Listar entregadores disponiveis")
        print("5 - Entregas de um entregador")
        print("0 - Voltar")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            listar_pedidos_pendentes()
        elif opcao == "2":
            listar_pedidos_entregues()
        elif opcao == "3":
            buscar_pedido_por_id()
        elif opcao == "4":
            listar_entregadores_disponiveis()
        elif opcao == "5":
            mostrar_entregas_entregador()
        elif opcao == "0":
            print("Voltando ao menu principal...")
        else:
            print("Opcao invalida.")
