import pygame
import math

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255) # bg color
BLACK = (0, 0, 0) # rope
RED = (255, 0, 0) # bob

# Pendulum properties
origin = (WIDTH // 2, 100)
length = 300 # Length of the rope pixels
mass = 20 # BOB MASS
angle = math.pi /1.5  # Starting angle

gravity = 0.998


theta_velocity = 0  # How fast the pendulam swings
theta_acceleration = 0  # Change of speed
damping = 0.995  # air resistance, making the pendulam slow down

# Simulation loop
running = True
clock = pygame.time.Clock() # For motion like fps,  making it look smooth

while running:
    screen.fill(WHITE)

    # Calculate acceleration (Torque = -mgLsin(theta) / moment of inertia)
    # τ = Iα to solve for α: α = τ / I. Substituting the torque equation, we get: α = (-mgLsin(θ) / I) / I.

    theta_acceleration = (-gravity / length) * math.sin(angle) # affected by gravity here

    # Update velocity and angle
    theta_velocity += theta_acceleration  #swining motion calculation,
    theta_velocity *= damping  # damping applied so the pendulam doesnt move forever
    angle += theta_velocity #   angle updated to move the pendulam

    # Calculate pendulum bob position using formula
    bob_x = origin[0] + length * math.sin(angle)
    bob_y = origin[1] + length * math.cos(angle)
    bob_position = (int(bob_x), int(bob_y))

    # Draw pendulum
    pygame.draw.line(screen, BLACK, origin, bob_position, 3)
    pygame.draw.circle(screen, RED, bob_position, mass)

    # FOR QUITTING THE EXECUTION
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60) # 60 frames making it smooth

pygame.quit()
