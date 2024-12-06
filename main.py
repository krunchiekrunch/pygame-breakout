import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout in pygame!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# clock to set the fps
clock = pygame.time.Clock()

paddle_width, paddle_height = 100, 10
paddle_x = (SCREEN_WIDTH - paddle_width) // 2
paddle_y = SCREEN_HEIGHT - 30
paddle_speed = 10

ball_radius = 8
ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
ball_dx, ball_dy = 4, -4

brick_rows, brick_cols = 5, 10
brick_width = SCREEN_WIDTH // brick_cols
brick_height = 20
bricks = []

# add bricks
for row in range(brick_rows):
    for col in range(brick_cols):
        bricks.append(pygame.Rect(col * brick_width, row * brick_height, brick_width, brick_height))

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move platform
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - paddle_width:
        paddle_x += paddle_speed

    # move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # ball collide with the walls
    if ball_x <= 0 or ball_x >= SCREEN_WIDTH - ball_radius:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy

    # ball collide with platform
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle_rect.collidepoint(ball_x, ball_y):
        ball_dy = -ball_dy

    # ball collide with bricks
    for brick in bricks[:]:
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_dy = -ball_dy
            break

    # add the platform
    pygame.draw.rect(screen, WHITE, paddle_rect)

    # add the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # add the bricks
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)

    # game over
    if ball_y > SCREEN_HEIGHT:
        print("Game Over!")
        running = False

    # FPS
    pygame.display.flip()
    clock.tick(60)

pygame.quit()