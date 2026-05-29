from dados import pedidos, entregadores
from auxiliares import validar_id_pedido, buscar_pedido, buscar_entregador

def cadastrar_pedido():
    print("\n--- CADASTRO DE PEDIDO ---")

    id_pedido = input("ID do pedido (ex: A1234): ").strip().upper()

    if validar_id_pedido(id_pedido) == False:
        print("Erro: ID invalido. Use 1 letra + 4 numeros.")
        return

    if buscar_pedido(id_pedido) != None:
        print("Erro: ID de pedido ja cadastrado.")
        return

    nome_cliente = input("Nome do cliente: ").strip()
    endereco = input("Endereco: ").strip()
    prioridade = input("Prioridade (Alta/Normal): ").strip()

    if prioridade != "Alta" and prioridade != "Normal":
        print("Erro: Prioridade invalida.")
        return

    descricao = input("Descricao do pedido: ").strip()

    print("Status: Pendente, Em Rota, Entregue ou Cancelado")
    status = input("Status: ").strip()

    if status != "Pendente" and status != "Em Rota" and status != "Entregue" and status != "Cancelado":
        print("Erro: Status invalido.")
        return

    id_entregador = input("ID do entregador (deixe vazio se nao houver): ").strip()

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

def cadastrar_entregador():
    print("\n--- CADASTRO DE ENTREGADOR ---")

    id_entregador = input("ID do entregador (4 numeros): ").strip()

    if len(id_entregador) != 4:
        print("Erro: ID deve ter exatamente 4 numeros.")
        return

    if id_entregador.isdigit() == False:
        print("Erro: ID deve ter exatamente 4 numeros.")
        return

    if buscar_entregador(id_entregador) != None:
        print("Erro: Entregador ja cadastrado.")
        return

    nome = input("Nome do entregador: ").strip()

    veiculo = input("Veiculo (carro/van/moto): ").strip().lower()

    if veiculo != "carro" and veiculo != "van" and veiculo != "moto":
        print("Erro: Veiculo invalido.")
        return

    disponibilidade = input("Disponibilidade (disponivel/indisponivel): ").strip().lower()

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
