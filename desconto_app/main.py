from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.adapters.controllers.pedido_controller import PedidoController


if __name__ == "__main__":

    # Banco de dados
    database = MemoryDatabase()

    # Repository
    repository = MemoryPedidoRepository(database)

    # Use Case
    criar_pedido = CriarPedido(repository)

    # Controller
    controller = PedidoController(criar_pedido)

    # Criando pedidos através do Controller
    controller.criar_pedido(
        "Cliente 1",
        100.0,
        "normal"
    )

    controller.criar_pedido(
        "Cliente 2",
        100.0,
        "vip"
    )

    controller.criar_pedido(
        "Cliente 3",
        100.0,
        "premium"
    )

    # Listando os pedidos
    pedidos = controller.listar_pedidos()

    print("\n========== PEDIDOS REGISTRADOS ==========\n")

    for pedido in pedidos:
        tipo_desconto = pedido.desconto.__class__.__name__.replace("Desconto", "")

        print(f"Cliente: {pedido.cliente}")
        print(f"Tipo de desconto: {tipo_desconto}")
        print(f"Valor original: R$ {pedido.valor_original:.2f}")
        print(f"Valor do desconto: R$ {pedido.valor_desconto():.2f}")
        print(f"Valor final: R$ {pedido.valor_final():.2f}")
        print("-----------------------------------------")

    print(f"Total de pedidos: {len(pedidos)}")