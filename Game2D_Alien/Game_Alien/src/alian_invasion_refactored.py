import pygame

from bullet_manager import BulletManager
from fleet_manager import FleetManager
from game_event_handler import GameEventHandler
from game_renderer import GameRenderer
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self) -> None:
        """Inicializa o jogo e cria os recursos básicos."""

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width,
                self.settings.screen_height
            )
        )

        pygame.display.set_caption("Alien Invasion")

        # Cria a nave
        self.ship = Ship(
            self.screen,
            self.settings
        )

        # Cor do plano de fundo
        self.bg_color = self.settings.bg_color

        # Gerencia os projéteis
        self.bullet_manager = BulletManager(
            self.screen,
            self.settings,
            self.ship
        )

        # Gerencia a frota de alienígenas
        self.fleet_manager = FleetManager(
            self.screen,
            self.settings,
            self.ship
        )

        # Gerencia os eventos do teclado e da janela
        self.event_handler = GameEventHandler(
            self.ship,
            self.bullet_manager
        )

        # Gerencia o desenho da tela
        self.renderer = GameRenderer(
            self.screen,
            self.bg_color,
            self.ship,
            self.bullet_manager.bullets,
            self.fleet_manager.aliens
        )

    def _update_game_state(self) -> None:
        """Atualiza a posição da nave, projéteis e alienígenas."""

        # Atualiza a nave
        self.ship.update()

        # Atualiza os projéteis e verifica colisões
        self.bullet_manager._update_bullets(
            self.fleet_manager.aliens
        )

        # Atualiza os alienígenas
        self.fleet_manager.update_aliens()

        # Verifica colisão entre nave e alienígenas
        self.fleet_manager.check_ship_collision()

    def run_game(self) -> None:
        """Executa o laço principal do jogo."""

        # Cria a frota de alienígenas
        self.fleet_manager.create_fleet()

        while True:

            # Verifica teclado e fechamento da janela
            self.event_handler._check_events()

            # Atualiza o estado do jogo
            self._update_game_state()

            # Desenha tudo na tela
            self.renderer.render_screen()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()