import pygame
import time
import random

# Инициализация Pygame
pygame.init()

# Определяем размеры экрана и цвет
width, height = 600, 400
snake = (0, 0, 0)
white = (255, 255, 255)
text_color = (213, 50, 80)
food = (0, 255, 0)
bg = (0, 0, 0)

# Настройки экрана
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake_Game')

# Размер блока и скорость змейки
block_size = 10
snake_speed = 15

# Шрифт
font_style = pygame.font.SysFont(None, 20)

# Функция для отображения сообщения
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

# Функция для игры
def gameLoop():
    game_over = False
    game_close = False

    # Начальная позиция змейки
    x1 = width / 2
    y1 = height / 2

    # Изменения позиции змейки
    x1_change = 0
    y1_change = 0

    # Длина змейки и начальная длина
    snake_List = []
    Length_of_snake = 1

    # Позиция пищи
    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close == True:
            dis.fill(bg)
            message("Вы проиграли! Нажмите C для продолжения или Q для выхода", text_color)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(bg)
        pygame.draw.rect(dis, food, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in snake_List:
            pygame.draw.rect(dis, snake, [x[0], x[1], block_size, block_size])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()