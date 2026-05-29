from cadastros import cadastrar_pedido, cadastrar_entregador
from atualizacoes import menu_atualizacao_pedidos
from consultas import menu_consultas
from relatorios import menu_relatorios

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

        opcao = input("Escolha uma opcao: ").strip()

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

menu_principal()
