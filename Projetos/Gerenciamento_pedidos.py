def main():
    n: int = int(input())
  
    total: float = 0
    
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome: str = pedido[0]
        valor: float = float(pedido[1])
        total += valor
        

    desconto: str = input()
    match desconto:
        case '10%':
            valor_desconto: float = total * 0.1
            total -= valor_desconto

        case '20%':
            valor_desconto: float = total * 0.2
            total -= valor_desconto

    print(f"Valor total: {total:.2f}")

   

if __name__ == "__main__":
    main()
