from desconto import *


def main():

    valor = float(input("Digite o valor do produto: "))

    tipo = input(
        "Digite o tipo de desconto (normal, vip, premium): "
    ).lower()

    if tipo == "normal":
        desconto = DescontoNormal()

    elif tipo == "vip":
        desconto = DescontoVIP()

    elif tipo == "premium":
        desconto = DescontoPremium()

    else:
        print("Tipo de desconto inválido.")
        return

    if tipo != "vip":

        valor_desconto = aplicar_desconto(
            desconto,
            valor
        )

        print(f"Desconto: {valor_desconto}")
        print(f"Valor Final: {valor - valor_desconto}")

    else:

        valor_desconto, usuario_vip, cupom_aplicado = validar_vip(
            desconto,
            valor
        )

        print(f"Desconto: {valor_desconto}")
        print(f"Valor Final: {valor - valor_desconto}")
        print(f"Usuário VIP: {usuario_vip}")
        print(f"Cupom Aplicado: {cupom_aplicado}")


def aplicar_desconto(
    desconto: IDesconto,
    valor: float
) -> float:

    return desconto.calcular(valor)


def validar_vip(
    desconto: DescontoVIP,
    valor: float
) -> tuple:

    return (
        desconto.calcular(valor),
        desconto.validar_usuario_vip("vip"),
        desconto.aplicar_cupom("CUPOMVIP")
    )


if __name__ == "__main__":
    main()