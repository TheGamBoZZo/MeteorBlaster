# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:25:58 2024

@author: Muhammad Raees Fakie
"""

import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meteor Blaster")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255, 215, 0)  

# Load sounds
pygame.mixer.music.load("retro.mp3")  # Background music
crash_sound = pygame.mixer.Sound("crash.mp3")  # Crash sound effect

# Start background music
pygame.mixer.music.play(-1)  # -1 means it loops indefinitely

spaceship_speed = 5
spaceship_color = GREEN

projectile_speed = 7
projectile_width = 5
projectile_height = 10

meteor_speed = 3
meteor_width = 50
meteor_height = 50

# Rapid-fire settings
rapid_fire_duration = 5  # 5 seconds of rapid-fire mode
rapid_fire_enabled = False
rapid_fire_end_time = 0

# Fonts
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 72)

# Score, time, and game status
score = 0
game_over = False
start_time = None

# Create the spaceship object
class Spaceship:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 80
        self.width = 40
        self.height = 40
        self.speed = spaceship_speed
        self.projectiles = []
        self.last_shot_time = 0  # Track time for shots in rapid-fire mode

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        global rapid_fire_enabled
        current_time = time.time()
        
        # Determine fire rate based on rapid-fire status
        fire_delay = 0.2 if rapid_fire_enabled else 0.5
        
        if len(self.projectiles) < 5 and (current_time - self.last_shot_time > fire_delay):
            self.projectiles.append(Projectile(self.x + self.width // 2, self.y))
            self.last_shot_time = current_time

    def draw(self):
        # Draw the spaceship as an oval with gaps between the wings
        pygame.draw.ellipse(screen, spaceship_color, (self.x, self.y, self.width, self.height))  # Body
        pygame.draw.polygon(screen, spaceship_color, [(self.x - 20, self.y + 15), (self.x, self.y + 10), (self.x, self.y + 30)])  # Left wing
        pygame.draw.polygon(screen, spaceship_color, [(self.x + self.width, self.y + 10), (self.x + self.width + 20, self.y + 15), (self.x + self.width, self.y + 30)])  # Right wing
        
        for projectile in self.projectiles:
            projectile.move()
            projectile.draw()

class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = projectile_speed

    def move(self):
        self.y -= self.speed
        if self.y < 0:
            self.kill()

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, projectile_width, projectile_height))

    def kill(self):
        spaceship.projectiles.remove(self)

class Meteor:
    def __init__(self):
        self.x = random.randint(0, WIDTH - meteor_width)
        self.y = random.randint(-100, -40)
        self.speed = meteor_speed

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.reset()

    def reset(self):
        self.x = random.randint(0, WIDTH - meteor_width)
        self.y = random.randint(-100, -40)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, meteor_width, meteor_height))

    def check_collision(self):
        global score, game_over
        # Check collision with spaceship
        if (self.x < spaceship.x < self.x + meteor_width or self.x < spaceship.x + spaceship.width < self.x + meteor_width) and \
           (self.y < spaceship.y < self.y + meteor_height or self.y < spaceship.y + spaceship.height < self.y + meteor_height):
            crash_sound.play()  # Play crash sound
            game_over = True
        # Check collision with projectiles
        for projectile in spaceship.projectiles:
            if (self.x < projectile.x < self.x + meteor_width or self.x < projectile.x + projectile_width < self.x + meteor_width) and \
               (self.y < projectile.y < self.y + meteor_height):
                spaceship.projectiles.remove(projectile)
                self.reset()  # Respawn meteor
                score += 10  # Increase score by 10 for each meteor hit
                return False
        return False

# Golden star bonus object
class GoldenStar:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 20)
        self.y = random.randint(-100, -40)
        self.speed = meteor_speed / 2  

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.reset()

    def reset(self):
        self.x = random.randint(0, WIDTH - 20)
        self.y = random.randint(-100, -40)

    def draw(self):
        pygame.draw.circle(screen, GOLD, (self.x, self.y), 10)

    def check_collision(self):
        global rapid_fire_enabled, rapid_fire_end_time
        if (self.x < spaceship.x < self.x + 20 or self.x < spaceship.x + spaceship.width < self.x + 20) and \
           (self.y < spaceship.y < self.y + 20 or self.y < spaceship.y + spaceship.height < self.y + 20):
            rapid_fire_enabled = True
            rapid_fire_end_time = time.time() + rapid_fire_duration
            self.reset()  

# Game over screen function
def game_over_screen():
    global score, game_over
    end_time = time.time()
    time_survived = int(end_time - start_time)

    while game_over:
        screen.fill(BLACK)

        game_over_text = large_font.render("Game Over", True, RED)
        score_text = font.render(f"Score: {score}", True, WHITE)
        time_text = font.render(f"Time: {time_survived} sec", True, WHITE)
        play_again_text = font.render("Press R to Play Again or ESC to Exit", True, WHITE)

        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 4))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        screen.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, HEIGHT // 2 + 40))
        screen.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT - 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_game()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

# Function to restart the game
def restart_game():
    global score, game_over, spaceship, meteors, golden_star, start_time
    score = 0
    game_over = False
    spaceship = Spaceship()
    meteors = [Meteor() for _ in range(5)]
    golden_star = GoldenStar()
    start_time = time.time()

# Create game objects
spaceship = Spaceship()
meteors = [Meteor() for _ in range(5)]
golden_star = GoldenStar()

# Game loop
running = True
clock = pygame.time.Clock()
start_time = time.time()

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Spaceship movement
        keys = pygame.key.get_pressed()
        spaceship.move(keys)

        # Check rapid-fire mode expiration
        if rapid_fire_enabled and time.time() > rapid_fire_end_time:
            rapid_fire_enabled = False

        # Draw and move meteors
        for meteor in meteors:
            meteor.move()
            meteor.draw()
            meteor.check_collision()

        # Draw and move golden star
        golden_star.move()
        golden_star.draw()
        golden_star.check_collision()

        # Draw spaceship
        spaceship.draw()

        # Display score and time
        score_text = font.render(f"Score: {score}", True, WHITE)
        time_survived = int(time.time() - start_time)
        time_text = font.render(f"Time: {time_survived} sec", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 40))

        # Update screen
        pygame.display.flip()

        clock.tick(60)
    else:
        game_over_screen()

pygame.quit()
