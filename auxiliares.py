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

