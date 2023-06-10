import pygame
import sys

# Initialize Pygame
pygame.init()

FPS = 30
screen_width, screen_height = 1280, 1024
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Boilerplate")

# Set up the player
player_radius = 25
player_color = (255, 0, 0)  # Red
player_pos = [screen_width // 2, screen_height // 2]  # Place the player in the center of the screen

# Set up the movement variables
movement_speed = 5
move_up = False
move_down = False
move_left = False
move_right = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_up = True
            elif event.key == pygame.K_s:
                move_down = True
            elif event.key == pygame.K_a:
                move_left = True
            elif event.key == pygame.K_d:
                move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_up = False
            elif event.key == pygame.K_s:
                move_down = False
            elif event.key == pygame.K_a:
                move_left = False
            elif event.key == pygame.K_d:
                move_right = False

    # Update the player's position based on movement
    if move_up:
        player_pos[1] -= movement_speed
    if move_down:
        player_pos[1] += movement_speed
    if move_left:
        player_pos[0] -= movement_speed
    if move_right:
        player_pos[0] += movement_speed

    # Fill the screen with white color
    screen.fill((255, 255, 255))  # (R, G, B) values for white

    # Draw the player as a circle
    pygame.draw.circle(screen, player_color, player_pos, player_radius)

    # Update the display
    pygame.display.flip()
