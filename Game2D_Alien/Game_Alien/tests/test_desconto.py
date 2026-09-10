import pytest

from src.desconto import DescontoNormal, DescontoVIP, DescontoPremium


def test_desconto_normal():

    desconto_normal = DescontoNormal()

    resultado = desconto_normal.calcular(100)

    assert resultado == 10, f"Esperado: 10, mas obteve: {resultado}"


@pytest.fixture
def desconto_vip():
    return DescontoVIP()


def test_desconto_100_vip(desconto_vip):

    resultado = desconto_vip.calcular(100)
    assert resultado == 20, f"Esperado: 20, mas obteve: {resultado}"


def test_desconto_200_vip(desconto_vip):

    resultado = desconto_vip.calcular(200)
    assert resultado == 40, f"Esperado: 40, mas obteve: {resultado}"


@pytest.mark.parametrize(
    "valor, esperado", [(100, 30), (200, 60), (300, 90)]
)

def test_desconto_premium(valor, esperado):
    desconto_premium = DescontoPremium()

    resultado = desconto_premium.calcular(valor)

    assert resultado == esperado, f"Esperado: {esperado}, mas obteve: {resultado}"