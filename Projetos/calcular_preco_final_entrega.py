valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

precoaPagar = (valorHamburguer*quantidadeHamburguer)+(valorBebida*quantidadeBebida)
troco = (valorPago - precoaPagar)

print(f"O preço final do pedido é R$ {precoaPagar:.2f}. Seu troco é R$ {troco:.2f}.")