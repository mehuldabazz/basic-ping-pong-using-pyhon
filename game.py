import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Paddle dimensions
paddle_width = 10
paddle_height = 100

# Ball dimensions
ball_size = 10

# Initialize screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong Game")

# Fonts
font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 35)

# Game variables
clock = pygame.time.Clock()
def draw_ball(ball_x, ball_y):
    pygame.draw.rect(screen, white, (ball_x, ball_y, ball_size, ball_size))

def draw_paddles(paddle1_y, paddle2_y):
    pygame.draw.rect(screen, white, (50, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (screen_width - 50 - paddle_width, paddle2_y, paddle_width, paddle_height))

def draw_score(score1, score2):
    score_text = font.render(f"{score1} - {score2}", True, white)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 20))

def draw_menu():
    screen.fill(black)
    title_text = font.render("Ping Pong Game", True, white)
    play_text = small_font.render("Press 'P' to Play", True, white)
    ai_text = small_font.render("Press 'A' for AI Mode", True, white)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 4))
    screen.blit(play_text, (screen_width // 2 - play_text.get_width() // 2, screen_height // 2))
    screen.blit(ai_text, (screen_width // 2 - ai_text.get_width() // 2, screen_height // 2 + 50))
    pygame.display.flip()

def ai_movement(ball_y, paddle2_y, paddle_speed):
    if paddle2_y + paddle_height // 2 < ball_y:
        paddle2_y += paddle_speed
    if paddle2_y + paddle_height // 2 > ball_y:
        paddle2_y -= paddle_speed
    return paddle2_y
def main():
    menu = True
    ai_mode = False
    running = False
    
    paddle1_y = screen_height // 2 - paddle_height // 2
    paddle2_y = screen_height // 2 - paddle_height // 2
    ball_x = screen_width // 2
    ball_y = screen_height // 2
    ball_speed_x = 3
    ball_speed_y = 3
    paddle_speed = 5
    score1 = 0
    score2 = 0

    while True:
        while menu:
            draw_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        running = True
                        menu = False
                    if event.key == pygame.K_a:
                        running = True
                        menu = False
                        ai_mode = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and paddle1_y > 0:
                paddle1_y -= paddle_speed
            if keys[pygame.K_s] and paddle1_y < screen_height - paddle_height:
                paddle1_y += paddle_speed

            if not ai_mode:
                if keys[pygame.K_UP] and paddle2_y > 0:
                    paddle2_y -= paddle_speed
                if keys[pygame.K_DOWN] and paddle2_y < screen_height - paddle_height:
                    paddle2_y += paddle_speed
            else:
                paddle2_y = ai_movement(ball_y, paddle2_y, paddle_speed)

            ball_x += ball_speed_x
            ball_y += ball_speed_y

            if ball_y <= 0 or ball_y >= screen_height - ball_size:
                ball_speed_y *= -1

            if (ball_x <= 50 + paddle_width and paddle1_y < ball_y < paddle1_y + paddle_height) or (ball_x >= screen_width - 50 - paddle_width - ball_size and paddle2_y < ball_y < paddle2_y + paddle_height):
                ball_speed_x *= -1

            if ball_x <= 0:
                score2 += 1
                ball_x, ball_y = screen_width // 2, screen_height // 2
                ball_speed_x *= -1
            if ball_x >= screen_width - ball_size:
                score1 += 1
                ball_x, ball_y = screen_width // 2, screen_height // 2
                ball_speed_x *= -1

            screen.fill(black)
            draw_ball(ball_x, ball_y)
            draw_paddles(paddle1_y, paddle2_y)
            draw_score(score1, score2)
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    main()
