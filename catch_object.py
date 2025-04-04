import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 200  # Increased width for the player
PLAYER_HEIGHT = 30   # Decreased height for the player
OBJECT_WIDTH = 30
OBJECT_HEIGHT = 40   # Height for the falling objects
FPS = 60
MAX_MISSES = 6
FALLING_SPEED = 3    # Slower falling speed
PLAYER_SPEED = 20     # Increased player speed

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Object Game")

# Load images
player_image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_image.fill(BLACK)  # Placeholder for player
object_image = pygame.Surface((OBJECT_WIDTH, OBJECT_HEIGHT))
object_image.fill(RED)  # Placeholder for falling object

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    def move(self, dx):
        self.rect.x += dx
        # Keep player within screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - PLAYER_WIDTH:
            self.rect.x = SCREEN_WIDTH - PLAYER_WIDTH

    def draw(self):
        screen.blit(player_image, self.rect.topleft)

# Falling object class
class FallingObject:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH), 0, OBJECT_WIDTH, OBJECT_HEIGHT)

    def fall(self):
        self.rect.y += FALLING_SPEED  # Use the slower falling speed

    def draw(self):
        screen.blit(object_image, self.rect.topleft)

# Main game function
def main():
    clock = pygame.time.Clock()
    player = Player()
    falling_objects = []
    score = 0
    misses = 0
    running = True
    game_over = False

    while running:
        # Fill the screen with a white background
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            # Player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move(-PLAYER_SPEED)  # Use the increased player speed
            if keys[pygame.K_RIGHT]:
                player.move(PLAYER_SPEED)  # Use the increased player speed

            # Create new falling objects
            if random.randint(1, 60) == 1:  # Adjust frequency of falling objects (increased range)
                falling_objects.append(FallingObject())

            # Update and draw falling objects
            for obj in falling_objects[:]:
                obj.fall()
                if obj.rect.y > SCREEN_HEIGHT:
                    misses += 1
                    falling_objects.remove(obj)  # Remove if it falls off the screen
                if obj.rect.colliderect(player.rect):
                    score += 1
                    falling_objects.remove(obj)  # Remove object if caught

                obj.draw()

            # Draw player
            player.draw()

            # Display score and misses
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'Score: {score}', True, BLACK)
            misses_text = font.render(f'Misses: {misses}', True, BLACK)
            screen.blit(score_text, (10, 10))
            screen.blit(misses_text, (10, 50))

            # Check for game over
            if misses >= MAX_MISSES:
                game_over = True

        else:
            # Game Over screen
            font = pygame.font.Font(None, 74)
            game_over_text = font.render('Game Over', True, BLACK)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
            restart_text = font.render('Press R to Restart', True, BLACK)
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 20))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                main()  # Restart the game

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()