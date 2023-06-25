
from Button import *
from ClassPeople import *
from Class_Fire import Fire

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1545, 781))  # flags=pygame.NOFRAME убирает рамку приложения
font = pygame.font.SysFont('Constantia', 30)
magazine = Magazine((-5, 0), screen)  # Создание фона

list_Of_Peoples = People((0, 0), 0, 0, 0)
list_Of_Peoples.Create_Random_Peoples()
list_Of_Peoples.Create_Random_Peoples()
list_Of_Peoples.Create_Random_Peoples()

fridge = Fridge(screen)  # создание холодильника

Store_Big = Store_Big(screen)  # создание большой лавки фруктов

fruits_Store = Fruits_Store(screen)  # создание лавки фруктов

window = Windows(screen)  # создание окон

door = Door(screen)  # создание двери

extinguisher = Extinguisher(screen)  # создание огнетушителя

fire = Fire(screen, fridge, fruits_Store, Store_Big, window, door, list_Of_Peoples,magazine)  # создание огня

magazine.Add_Entity(
    [door, window, extinguisher, fruits_Store, Store_Big, fridge])  # добавление двери в список обьектов магазина
exit_sain = pygame.image.load('textures\Exit.png')
exit_sain.set_colorkey((255, 255, 255))
button = Interface(200, 30, screen, font, [window, extinguisher, fruits_Store, Store_Big, fridge, fire])
button_little = Interface(60, 30, screen, font, [window, extinguisher, fruits_Store, Store_Big, fridge])
play = True
time = 0
while play:
    magazine.Print_All(), screen.blit(exit_sain, (950, 700))
    list_Of_Peoples.Paint_Peoples(screen, time),list_Of_Peoples.Move_Peoples(fire.get_Fire_Cords(), fruits_Store, Store_Big, fridge, extinguisher, fire)
    fire.Print_On_Canvas(),fire.Confirm_Fire_On_A_People(), fire.ignition()
    button.Draw(10, 205, 'Начать пожар', 'start_Fire'),
    button.Draw(10, 30, 'Окно', 'okno')
    button.Draw(10, 65, 'Огнетушитель', 'exti'),
    button.Draw(10, 100, 'Лавка фруктов', 'fruits'),button_little.Draw(230, 100, '+', 'fruits_Change')
    button.Draw(10, 135, 'Большая лавка', 'big_Store'),button_little.Draw(230, 135, '+', 'big_Store_Change')
    button.Draw(10, 170, 'Холодильник', 'Fridge_Off'),button_little.Draw(230, 170, '+', 'Fridge_Change')
    if len(fire.get_Fire_Cords())==0:
        if not magazine.Get_Fired():
            if randint(1, 1100) == 1:
                list_Of_Peoples.Create_Random_Peoples()
    time += 1
    if time == 90:
        time = 0
    pygame.display.update()
    for event in pygame.event.get():  # функция корректного выхода из пай гейм
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
