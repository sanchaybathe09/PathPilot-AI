import pygame


class PathPilotVisualizer:
    """Visual display for the PathPilot AI robot."""

    def __init__(self, rows=5, cols=5, cell_size=100):
        pygame.init()

        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        self.width = cols * cell_size
        self.height = rows * cell_size + 85

        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )
        pygame.display.set_caption(
            "PathPilot AI | Robot Navigation"
        )

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 22)

        self.background = (245, 247, 250)
        self.grid_color = (200, 205, 215)
        self.obstacle_color = (65, 72, 85)
        self.start_color = (55, 120, 230)
        self.goal_color = (35, 170, 100)
        self.path_color = (190, 220, 255)
        self.robot_color = (240, 145, 35)
        self.text_color = (35, 40, 50)

    def draw_grid(
        self, start, goal, obstacles, route=None, robot_position=None
    ):
        self.screen.fill(self.background)

        route = route or []

        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(
                    col * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )

                position = (row, col)
                color = (255, 255, 255)

                if position == start:
                    color = self.start_color
                elif position == goal:
                    color = self.goal_color
                elif position in obstacles:
                    color = self.obstacle_color

                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(
                    self.screen, self.grid_color, rect, 1
                )

        # Draw the learned route as a line
        if len(route) > 1:
            points = [
                (
                    col * self.cell_size + self.cell_size // 2,
                    row * self.cell_size + self.cell_size // 2,
                )
                for row, col in route
            ]

            pygame.draw.lines(
                self.screen, self.path_color, False, points, 8
            )

        # Draw the moving robot
        if robot_position is not None:
            row, col = robot_position

            center = (
                col * self.cell_size + self.cell_size // 2,
                row * self.cell_size + self.cell_size // 2,
            )

            pygame.draw.circle(
                self.screen,
                self.robot_color,
                center,
                self.cell_size // 4,
            )

        title = self.font.render(
            "PATHPILOT AI", True, self.text_color
        )
        self.screen.blit(
            title, (10, self.rows * self.cell_size + 15)
        )

        if robot_position == goal:
            status_text = "DESTINATION REACHED!"
            status_color = (35, 140, 80)
        else:
            status_text = "ROBOT NAVIGATING..."
            status_color = (55, 100, 190)

        status = self.font.render(
            status_text, True, status_color
        )
        self.screen.blit(
            status,
            (10, self.rows * self.cell_size + 48),
        )

        pygame.display.flip()

    def close(self):
        pygame.quit()
