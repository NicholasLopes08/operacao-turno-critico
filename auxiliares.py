from dados import pedidos, entregadores

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

def buscar_pedido(id_pedido):
    for pedido in pedidos:
        if pedido["id"] == id_pedido:
            return pedido
    return None

def buscar_entregador(id_entregador):
    for entregador in entregadores:
        if entregador["id"] == id_entregador:
            return entregador
    return None

def contar_pedidos_ativos(entregador):
    total = 0
    for id_pedido in entregador["pedidos_associados"]:
        pedido = buscar_pedido(id_pedido)
        if pedido != None:
            if pedido["status"] == "Pendente" or pedido["status"] == "Em Rota":
                total = total + 1
    return total
