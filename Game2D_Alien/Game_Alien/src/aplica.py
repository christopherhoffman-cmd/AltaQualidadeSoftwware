from desconto import *


    
def main():

    normal = DescontoNormal()
    vip = DescontoVIP()
    premium = DescontoPremium()

    
    
    valor = int(input("Digite o valor do produto: "))

    tipo = input("Digite o tipo de desconto (normal, vip, premium): ").lower()

    if tipo == "normal":
        print(f"Desconto Normal: {normal.calcular_desconto(valor)}")
        valor -= normal.calcular_desconto(valor)
        print(f"Valor Final: {valor}")
    elif tipo == "vip":
        print(f"Desconto VIP: {vip.calcular_desconto(valor)}")
        valor -= vip.calcular_desconto(valor)
        print(f"Valor Final: {valor}")
    elif tipo == "premium":
        print(f"Desconto Premium: {premium.calcular_desconto(valor)}")
        valor -= premium.calcular_desconto(valor)
        print(f"Valor Final: {valor}")
    else:
        print("Tipo de desconto inválido.")
        return



if __name__ == "__main__":
    main()

