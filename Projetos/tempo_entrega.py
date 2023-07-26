import textwrap
def menu():
    menu = """\n
    ======== MENU ========
    [0] Dogão da praça
    [1] Lanche do Centro
    [2] Batata turbinada
    [3] Pastel da Igreja
    [4] Cancelar Pedido

    =>"""
    return input(textwrap.dedent(menu))

def main():
    dogao = 15
    centro = 35
    batata = 25
    pastel = 30

    while True:
        opcao = menu()

        if opcao == "0":
            print(f"O restaurante Dogão da praça entrega em {dogao} minutos")
        
        elif opcao == "1":
            print(f"O restaurante Lanche do Centro entrega em {centro} minutos")
        
        elif opcao == "2":
             print(f"O restaurante Batata turbinada entrega em {batata} minutos")
        
        elif opcao == "3":
             print(f"O restaurante Pastel da Igreja entrega em {pastel} minutos")
        
        else:
            print(f"Volte sempre!")
            break

main()
