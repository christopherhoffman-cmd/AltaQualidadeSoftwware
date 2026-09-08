from desconto import *


class Pedido:

    def __init__(self, desconto: IDesconto):
        self.desconto = desconto

    def total(self, valor):
        return valor - self.desconto.calcular(valor)


def main():

    valor = float(input("Digite o valor do produto: "))

    tipo = input(
        "Digite o tipo de desconto (normal, vip, premium): "
    ).lower()

    if tipo == "normal":
        pedido = Pedido(DescontoNormal())

    elif tipo == "vip":
        pedido = Pedido(DescontoVIP())

    elif tipo == "premium":
        pedido = Pedido(DescontoPremium())

    else:
        print("Tipo de desconto inválido.")
        return

    print(f"Valor Final: {pedido.total(valor)}")


if __name__ == "__main__":
    main()