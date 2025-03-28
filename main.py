import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pendulum Simulation")

# BG , rope, bob =>
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Pendulum starting point
origin = (WIDTH // 2, 100)
length = 300  # rope
mass = 20  # bob
angle_degrees = 120  # start angle
angle = math.radians(angle_degrees)  #  degrees => radians

gravity = 9.8  # def gravity

theta_velocity = 0
theta_acceleration = 0
damping = 0.995

paused = False

def calculate_period():
    return 2 * math.pi * math.sqrt(length / gravity) if gravity > 0 else 0


clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close window
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Reset
                angle_degrees = 120
                angle = math.radians(angle_degrees)
                theta_velocity = 0
            elif event.key == pygame.K_SPACE:  # pause func
                paused = not paused
            elif event.key == pygame.K_UP:  # Rope long
                length = min(500, length + 10)
            elif event.key == pygame.K_DOWN:  # rope short
                length = max(100, length - 10)

            elif event.key == pygame.K_LEFT:
                gravity = max(0.1, gravity - 0.5)
            elif event.key == pygame.K_RIGHT:
                gravity += 0.5

    if not paused:
        theta_acceleration = (-gravity / length) * math.sin(angle)
        theta_velocity += theta_acceleration
        theta_velocity *= damping
        angle += theta_velocity

    # Calculate bob pos
    bob_x = origin[0] + length * math.sin(angle)
    bob_y = origin[1] + length * math.cos(angle)
    bob_position = (int(bob_x), int(bob_y))


    pygame.draw.line(screen, BLACK, origin, bob_position, 3)  # Rope
    pygame.draw.circle(screen, RED, bob_position, mass)  # Bob

    # Display
    font = pygame.font.Font(None, 30)
    gravity_text = font.render(f"Gravity: {gravity:.2f} m/s²", True, BLACK)
    length_text = font.render(f"Rope Length: {length} px", True, BLACK)
    period_text = font.render(f"Period (T): {calculate_period():.2f} s", True, BLACK)
    instructions = font.render(
        "Press R to Reset | SPACE to Pause | Left/Right Arrows to Change Gravity | Up/Down Arrows to Change Rope Length",
        True, BLACK)

    #ToS
    screen.blit(gravity_text, (20, 20))
    screen.blit(length_text, (20, 50))
    screen.blit(period_text, (20, 80))
    screen.blit(instructions, (20, HEIGHT - 40))

    pygame.display.flip()
    clock.tick(60)  #60 fps?

pygame.quit()
