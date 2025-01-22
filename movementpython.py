import pygame #Импортируем библиотеку pygame
import sys #Импортируем библиотеку sys

pygame.init() #Инициализируем pygame
HEIGHT = 900 #Задаем переменную высоты
WIDTH = 1800 #Задаем переменную ширины
MainScreen = pygame.display.set_mode((WIDTH, HEIGHT)) #Создаем главное окно
pygame.display.set_caption("Movement Test v1") #Название окна

sprites_group = pygame.sprite.Group() #Создаем группу для спрайтов

class Player(pygame.sprite.Sprite): #Создаем спрайт с классом игрока
    def __init__(self): #Создаем функцию для инициализации спрайта
        pygame.sprite.Sprite.__init__(self) #Специальная строка для встроенной инициализации
        self.image = pygame.Surface((25, 25)) #Задаем внешний вид спрайта (квадрат 45 на 45 пикселей)
        self.image.fill((255, 255, 255)) #Заполняем его белым цветом
        self.rect = self.image.get_rect() #Создаем для него хитбокс (область определения объекта в 2D пространстве)
        self.rect.center = (WIDTH/2, HEIGHT/2) #Задаем начальную точку спрайта
        
        self.canmoving = True #Переменная проверяющая возможномть движения (если False делает игрока не управляемым)
        self.moving = None #Переменная для определения направления и движения
        self.speed = 1 #Переменная скорости (не рекомендуется ставить меньше 1)
    def update(self): #Создаем функцию которая будет срабатывать при обновлениии группы спрайдов
        if self.moving == "up": #Проверка на движение вверх
            self.rect.y -= self.speed #Передвижение вверх
        elif self.moving == "down": #Проверка на движение вниз
            self.rect.y += self.speed #Передвижение вниз
        elif self.moving == "left": #Проверка на движение влево
            self.rect.x -= self.speed #Проверка на движение влево
        elif self.moving == "right": #Проверка на движение вправо
            self.rect.x += self.speed #Проверка на движение вправо
    def move(self, direction): #Функция изменения переменной передвижения
        if self.canmoving == True: #Проверяем может ли двигаться игрок
            self.moving = direction #Изменяем направление движения

player = Player() #Создаем объект класса Player
sprites_group.add(player) #Добавляем player в группу спрайтов

while True: #Создаем основной цикл программы
    for event in pygame.event.get(): #Перебираем все ивенты pygame
        if event.type == pygame.QUIT: #Проверяем является ли ивент QUIT (выход)
            pygame.quit() #Разинициализируем pygame
            sys.exit() #Выходим из системы
        if event.type == pygame.KEYDOWN: #Проверяем является ли ивент KEYDOWN (нажатие клавиши)
            if event.key == pygame.K_w or event.key == pygame.K_UP: #Проверяем нажатие клавиши w или стрелки вверх
                player.move("up") #Вызываем функцию изменения направления движения (move())
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN: #Проверяем нажатие клавиши s или стрелки вниз
                player.move("down") #Вызываем функцию изменения направления движения (move())
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT: #Проверяем нажатие клавиши a или стрелки влево
                player.move("left") #Вызываем функцию изменения направления движения (move())
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT: #Проверяем нажатие клавиши d или стрелки вправо
                player.move("right") #Вызываем функцию изменения направления движения (move())
        if event.type == pygame.KEYUP: #Проверяем является ли ивент KEYUP (отпускание клавиши)
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and player.moving == "up": #Проверяем нажатие клавиши w или стрелки вверх а также движется ли игрок в этом напрвлении
                player.move(None) #Вызываем функцию изменения направления движения (move())
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and player.moving == "down": #Проверяем нажатие клавиши s или стрелки вниз а также движется ли игрок в этом напрвлении
                player.move(None) #Вызываем функцию изменения направления движения (move())
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and player.moving == "left": #Проверяем нажатие клавиши a или стрелки влево а также движется ли игрок в этом напрвлении
                player.move(None) #Вызываем функцию изменения направления движения (move())
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and player.moving == "right": #Проверяем нажатие клавиши d или стрелки вправо а также движется ли игрок в этом напрвлении
                player.move(None) #Вызываем функцию изменения направления движения (move())
    
    sprites_group.update() #Обновляем группу спрайтов
    MainScreen.fill((0, 0, 0)) #Устанавливаем цвет экрана
    sprites_group.draw(MainScreen) #Отрисовываем спрайты на главном экране
    pygame.display.flip() #Обновляем экран
