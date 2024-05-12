import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
display_width = 640
display_height = 480
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake initial position and properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# Food position and properties
food_pos = [random.randrange(1, (display_width//10)) * 10, random.randrange(1, (display_height//10)) * 10]
food_spawn = True

# Score
score = 0

# Clock to control game speed
clock = pygame.time.Clock()

# Function to draw the snake on the screen
def snake(snake_list, game_display, color):
    for x, y in snake_list:
        pygame.draw.rect(game_display, color, (x, y, 10, 10))

# Function to draw the food on the screen
def food(food_x, food_y, game_display, color):
    pygame.draw.rect(game_display, color, (food_x, food_y, 10, 10))

# Function to update the snake's position based on its direction
def update_snake(snake_pos, snake_body, snake_direction):
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    if snake_direction == 'DOWN':
        snake_pos[1] += 10
    if snake_direction == 'LEFT':
        snake_pos[0] -= 10
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    return snake_pos, snake_body

# Function to check if the snake has eaten the food
def collision_food(snake_pos, food_pos):
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        return True
    return False

# Function to check if the snake has collided with itself
def collision_self(snake_pos, snake_body):
    for each in snake_body[1:]:
        if snake_pos[0] == each[0] and snake_pos[1] == each[1]:
            return True
    return False

# Function to check if the snake has hit the boundaries
def collision_boundary(snake_pos, display_width, display_height):
    if snake_pos[0] < 0 or snake_pos[0] >= display_width or snake_pos[1] < 0 or snake_pos[1] >= display_height:
        return True
    return False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Update snake direction
    if change_to != snake_direction:
        snake_direction = change_to

    # Update snake position
    snake_pos, snake_body = update_snake(snake_pos, snake_body, snake_direction)

    # Check for food collision
    if collision_food(snake_pos, food_pos):
        score += 1
        food_spawn = False
        snake_body.append(list(snake_pos))

    # Spawn food in a new random position
    if not food_spawn:
        food_pos = [random.randrange(1, (display_width//10)) * 10, random.randrange(1, (display_height//10)) * 10]
        food_spawn = True

    # Clear the screen
    game_display.fill(black)

    # Draw the snake
    snake(snake_body, game_display, green)

    # Draw the food
    food(food_pos[0], food_pos[1], game_display, white)

    # Check for self-collision and boundary collision
    if collision_self(snake_pos, snake_body) or collision_boundary(snake_pos, display_width, display_height):
        pygame.quit()
        quit()

    # Update score
    myfont = pygame.font.SysFont("times new roman", 25)
    score_surface = myfont.render(f'Score : {score}', True, red)
    game_display.blit(score_surface, [0, 0])

    # Update display
    pygame.display.update()

    # Control game speed
    clock.tick(10)
