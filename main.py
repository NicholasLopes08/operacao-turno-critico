# ============================================
# Operacao Turno Critico - APPC
# Sistema de gestao de pedidos e entregadores
# ============================================

# Listas globais do sistema



# Verifica se o ID do pedido tem 1 letra + 4 numeros (ex: A1234)
def validar_id_pedido(id_pedido):
    if len(id_pedido) != 5:
        return False
    if id_pedido[0].isalpha() == False:
        return False
    if id_pedido[1].isdigit() == False:
        return False
    if id_pedido[2].isdigit() == False:
        return False
    if id_pedido[3].isdigit() == False:
        return False
    if id_pedido[4].isdigit() == False:
        return False
    return True


# Procura um pedido pelo ID
def buscar_pedido(id_pedido):
    for pedido in pedidos:
        if pedido["id"] == id_pedido:
            return pedido
    return None


# Procura um entregador pelo ID
def buscar_entregador(id_entregador):
    for entregador in entregadores:
        if entregador["id"] == id_entregador:
            return entregador
    return None


# Conta quantos pedidos ativos o entregador tem (Pendente ou Em Rota)
def contar_pedidos_ativos(entregador):
    total = 0
    for id_pedido in entregador["pedidos_associados"]:
        pedido = buscar_pedido(id_pedido)
        if pedido != None:
            if pedido["status"] == "Pendente" or pedido["status"] == "Em Rota":
                total = total + 1
    return total


# ---------- 1. Cadastro de pedidos ----------

def cadastrar_pedido():
    print("\n--- CADASTRO DE PEDIDO ---")

    id_pedido = input("ID do pedido (ex: A1234): ")
    id_pedido = id_pedido.strip()
    id_pedido = id_pedido.upper()

    if validar_id_pedido(id_pedido) == False:
        print("Erro: ID invalido. Use 1 letra + 4 numeros.")
        return

    if buscar_pedido(id_pedido) != None:
        print("Erro: ID de pedido ja cadastrado.")
        return

    nome_cliente = input("Nome do cliente: ")
    nome_cliente = nome_cliente.strip()

    endereco = input("Endereco: ")
    endereco = endereco.strip()

    prioridade = input("Prioridade (Alta/Normal): ")
    prioridade = prioridade.strip()

    if prioridade != "Alta" and prioridade != "Normal":
        print("Erro: Prioridade invalida.")
        return

    descricao = input("Descricao do pedido: ")
    descricao = descricao.strip()

    print("Status: Pendente, Em Rota, Entregue ou Cancelado")
    status = input("Status: ")
    status = status.strip()

    if status != "Pendente" and status != "Em Rota" and status != "Entregue" and status != "Cancelado":
        print("Erro: Status invalido.")
        return

    id_entregador = input("ID do entregador (deixe vazio se nao houver): ")
    id_entregador = id_entregador.strip()

    novo_pedido = {
        "id": id_pedido,
        "nome_cliente": nome_cliente,
        "endereco": endereco,
        "prioridade": prioridade,
        "descricao": descricao,
        "status": status,
        "id_entregador": id_entregador
    }

    pedidos.append(novo_pedido)
    print("Pedido cadastrado com sucesso!")


# ---------- 2. Cadastro de entregadores ----------

def cadastrar_entregador():
    print("\n--- CADASTRO DE ENTREGADOR ---")

    id_entregador = input("ID do entregador (4 numeros): ")
    id_entregador = id_entregador.strip()

    if len(id_entregador) != 4:
        print("Erro: ID deve ter exatamente 4 numeros.")
        return

    if id_entregador.isdigit() == False:
        print("Erro: ID deve ter exatamente 4 numeros.")
        return

    if buscar_entregador(id_entregador) != None:
        print("Erro: Entregador ja cadastrado.")
        return

    nome = input("Nome do entregador: ")
    nome = nome.strip()

    veiculo = input("Veiculo (carro/van/moto): ")
    veiculo = veiculo.strip()
    veiculo = veiculo.lower()

    if veiculo != "carro" and veiculo != "van" and veiculo != "moto":
        print("Erro: Veiculo invalido.")
        return

    disponibilidade = input("Disponibilidade (disponivel/indisponivel): ")
    disponibilidade = disponibilidade.strip()
    disponibilidade = disponibilidade.lower()

    if disponibilidade != "disponivel" and disponibilidade != "indisponivel":
        print("Erro: Disponibilidade invalida.")
        return

    novo_entregador = {
        "id": id_entregador,
        "nome": nome,
        "veiculo": veiculo,
        "pedidos_associados": [],
        "disponibilidade": disponibilidade
    }

    entregadores.append(novo_entregador)
    print("Entregador cadastrado com sucesso!")


# ---------- 3. Atualizacao de pedidos ----------

def alterar_status_pedido():
    print("\n--- ALTERAR STATUS DO PEDIDO ---")

    id_pedido = input("ID do pedido: ")
    id_pedido = id_pedido.strip()
    id_pedido = id_pedido.upper()

    pedido = buscar_pedido(id_pedido)

    if pedido == None:
        print("Pedido nao encontrado.")
        return

    print("Novo status: Pendente, Em Rota, Entregue ou Cancelado")
    novo_status = input("Novo status: ")
    novo_status = novo_status.strip()

    if novo_status != "Pendente" and novo_status != "Em Rota" and novo_status != "Entregue" and novo_status != "Cancelado":
        print("Status invalido.")
        return

    # Pedido entregue nao pode voltar para pendente
    if pedido["status"] == "Entregue" and novo_status == "Pendente":
        print("Erro: Pedido entregue nao pode voltar para Pendente.")
        return

    pedido["status"] = novo_status
    print("Status atualizado com sucesso!")


def cancelar_pedido():
    print("\n--- CANCELAR PEDIDO ---")

    id_pedido = input("ID do pedido: ")
    id_pedido = id_pedido.strip()
    id_pedido = id_pedido.upper()

    pedido = buscar_pedido(id_pedido)

    if pedido == None:
        print("Pedido nao encontrado.")
        return

    pedido["status"] = "Cancelado"
    print("Pedido cancelado com sucesso!")


def associar_entregador_pedido():
    print("\n--- ASSOCIAR ENTREGADOR AO PEDIDO ---")

    id_pedido = input("ID do pedido: ")
    id_pedido = id_pedido.strip()
    id_pedido = id_pedido.upper()

    pedido = buscar_pedido(id_pedido)

    if pedido == None:
        print("Pedido nao encontrado.")
        return

    # Pedido cancelado nao pode ser associado
    if pedido["status"] == "Cancelado":
        print("Erro: Pedido cancelado nao pode ser associado a entregador.")
        return

    id_entregador = input("ID do entregador: ")
    id_entregador = id_entregador.strip()

    entregador = buscar_entregador(id_entregador)

    if entregador == None:
        print("Entregador nao encontrado.")
        return

    if entregador["disponibilidade"] != "disponivel":
        print("Erro: Entregador indisponivel.")
        return

    # Cada entregador pode ter no maximo 3 pedidos ativos
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

    id_pedido = input("ID do pedido: ")
    id_pedido = id_pedido.strip()
    id_pedido = id_pedido.upper()

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

        opcao = input("Escolha: ")
        opcao = opcao.strip()

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


# ---------- 4. Consultas ----------

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

    id_pedido = input("ID do pedido: ")
    id_pedido = id_pedido.strip()
    id_pedido = id_pedido.upper()

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

    id_entregador = input("ID do entregador: ")
    id_entregador = id_entregador.strip()

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

        opcao = input("Escolha: ")
        opcao = opcao.strip()

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


# ---------- 5. Relatorios operacionais ----------

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

        opcao = input("Escolha: ")
        opcao = opcao.strip()

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


# ---------- Menu principal ----------

def menu_principal():
    opcao = ""
    while opcao != "0":
        print("\n========================================")
        print("   OPERACAO TURNO CRITICO - APPC")
        print("========================================")
        print("1 - Cadastrar pedido")
        print("2 - Cadastrar entregador")
        print("3 - Atualizar pedidos")
        print("4 - Consultas")
        print("5 - Relatorios operacionais")
        print("0 - Finalizar sistema")

        opcao = input("Escolha uma opcao: ")
        opcao = opcao.strip()

        if opcao == "1":
            cadastrar_pedido()
        elif opcao == "2":
            cadastrar_entregador()
        elif opcao == "3":
            menu_atualizacao_pedidos()
        elif opcao == "4":
            menu_consultas()
        elif opcao == "5":
            menu_relatorios()
        elif opcao == "0":
            print("\nSistema encerrado. Obrigado por usar a Operacao Turno Critico!")
        else:
            print("Opcao invalida. Tente novamente.")


# Inicio do programa
menu_principal()
