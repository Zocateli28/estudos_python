numPedidos: int = int(input())

pedidos: list = []

for i in range(1, numPedidos + 1):
    prato: str = input()
    calorias: int = int(input())
    ehVegano: str= input().strip().lower()
    pedido: dict = {}
    
    match ehVegano:

        case "s":
            pedido.update({'Num':i,'Prato':prato,'Calorias':calorias,'E vegano':'(Vegano)'})
            pedidos.append(pedido)

        case "n":
            pedido.update({'Num':i,'Prato':prato,'Calorias':calorias,'E vegano':'(Nao-Vegano)'})
            pedidos.append(pedido)

for pedidos_reg in pedidos:
    print(f'Pedido {pedidos_reg["Num"]}: {pedidos_reg["Prato"]} {pedidos_reg["E vegano"]} - {pedidos_reg["Calorias"]} calorias')



