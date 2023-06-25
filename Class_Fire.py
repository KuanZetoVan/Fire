import pygame
from random import randint


class Fire(pygame.sprite.Sprite):  # класс огня
    def __init__(self, screen, Fridge, Fruits, BigsFruits, window, door, list_Of_Peoples, magazin):
        pygame.sprite.Sprite.__init__(self)
        self.__image1 = pygame.image.load('textures\Fire_1.png')
        self.__image1.set_colorkey((0, 0, 0))
        self.__image2 = pygame.image.load('textures\Fire_2.png')
        self.__image2.set_colorkey((0, 0, 0))
        self.__image3 = pygame.image.load('textures\Fire_3.png')
        self.__image3.set_colorkey((0, 0, 0))
        self.__rect = self.__image1.get_rect()
        self.__screen = screen
        self.__Fridgefired = True
        self.__Fridge = Fridge
        self.__Fruitsfired = True
        self.__Fruits = Fruits
        self.__BigsFruitsfired = True
        self.__BigsFruits = BigsFruits
        self.__window = window
        self.__door = door
        self.__Changed = True
        self.__List_OF_fire_cords = []
        self.__magazin = magazin
        self.__list_Of_Peoples = list_Of_Peoples
        self.__extinguishing = False
        self.__Started_fire = []

    def Take_New_Fire(self):
        return self.__Started_fire

    def Add_Started_Fire(self, new_fire):
        self.__Started_fire.append(new_fire)

    def start_extinguishing(self):
        self.__extinguishing = True

    def getrect(self):
        return self.__rect

    def gettopcord(self):
        return self.__rect.top

    def getleftcord(self):
        return self.__rect.left

    def getrightcord(self):
        return self.__rect.right

    def getbottomcord(self):
        return self.__rect.bottom

    def getallcord(self):
        return self.gettopcord(), self.getleftcord(), self.getrightcord(), self.getbottomcord()

    def get_Fire_Cords(self):
        return self.__List_OF_fire_cords

    def Confirm_Fire_On_A_People(self):
        if len(self.__List_OF_fire_cords) == 0:
            return
        if len(self.__list_Of_Peoples.Get_Peoples()) == 0:
            return
        for People in self.__list_Of_Peoples.Get_Peoples():
            if People.Get_Status():
                for fire in self.__List_OF_fire_cords:
                    if People.getleftcord() - 5 < fire[0] < (People.getrightcord() + 5):
                        if People.gettopcord() - 5 < fire[1] < (People.getbottomcord() + 5):
                            People.Change_Status()
                            People.Stop_Move()
                            People.Die()

    def Print_On_Canvas(self):

        for i in range(len(self.__List_OF_fire_cords)):
            style = randint(1, 3)
            if style == 1:
                self.__screen.blit(self.__image1, (self.__List_OF_fire_cords[i][0], self.__List_OF_fire_cords[i][1]))
            if style == 2:
                self.__screen.blit(self.__image2, (self.__List_OF_fire_cords[i][0], self.__List_OF_fire_cords[i][1]))
            if style == 3:
                self.__screen.blit(self.__image3, (self.__List_OF_fire_cords[i][0], self.__List_OF_fire_cords[i][1]))

    def extinguishing(self):

        for fire in self.__List_OF_fire_cords:
            Chances = randint(1, 1000)
            if Chances == 1:
                self.__List_OF_fire_cords.remove(fire)
        if len(self.__List_OF_fire_cords) == 0:
            self.__extinguishing = False

    def ignition(self):
        if not self.__extinguishing:
            for i in range(len(self.__List_OF_fire_cords)):
                Chances = randint(1, 100)  # шанс возникновения нового огня
                if Chances == 1:
                    x = randint(1, 3)
                    y = randint(1, 3)
                    if x == 1:
                        if y == 1:
                            if (self.__List_OF_fire_cords[i][0] - 20 > 820) and (
                                    self.__List_OF_fire_cords[i][1] - 20 > 320):
                                if [self.__List_OF_fire_cords[i][0] - 20,
                                    self.__List_OF_fire_cords[i][1] - 20] \
                                        not in self.__List_OF_fire_cords:
                                    self.__List_OF_fire_cords.append(
                                        [self.__List_OF_fire_cords[i][0] - 20, self.__List_OF_fire_cords[i][1] - 20])

                        if y == 2:
                            if self.__List_OF_fire_cords[i][0] - 20 > 820:
                                if [self.__List_OF_fire_cords[i][0] - 20,
                                    self.__List_OF_fire_cords[i][1]] \
                                        not in self.__List_OF_fire_cords:
                                    self.__List_OF_fire_cords.append(
                                        [self.__List_OF_fire_cords[i][0] - 20, self.__List_OF_fire_cords[i][1]])
                        if y == 3:
                            if (self.__List_OF_fire_cords[i][0] - 20 > 820) and (
                                    self.__List_OF_fire_cords[i][1] + 20 < 730):
                                if [self.__List_OF_fire_cords[i][0] - 20,
                                    self.__List_OF_fire_cords[i][1] + 20] \
                                        not in self.__List_OF_fire_cords:
                                    self.__List_OF_fire_cords.append(
                                        [self.__List_OF_fire_cords[i][0] - 20, self.__List_OF_fire_cords[i][1] + 20])
                    if x == 2:
                        if y == 1:
                            if self.__List_OF_fire_cords[i][1] - 20 > 320:
                                if [self.__List_OF_fire_cords[i][0],
                                    self.__List_OF_fire_cords[i][1] - 20] \
                                        not in self.__List_OF_fire_cords:
                                    self.__List_OF_fire_cords.append(
                                        [self.__List_OF_fire_cords[i][0], self.__List_OF_fire_cords[i][1] - 20])
                        if y == 3:
                            if self.__List_OF_fire_cords[i][1] + 20 < 730:
                                if [self.__List_OF_fire_cords[i][0],
                                    self.__List_OF_fire_cords[i][1] + 20] \
                                        not in self.__List_OF_fire_cords:
                                    self.__List_OF_fire_cords.append(
                                        [self.__List_OF_fire_cords[i][0], self.__List_OF_fire_cords[i][1] + 20])
                    if x == 3:
                        if y == 1:
                            if (self.__List_OF_fire_cords[i][0] + 20 < 1480) and (
                                    self.__List_OF_fire_cords[i][1] - 20 > 320):
                                if [self.__List_OF_fire_cords[i][0] + 20,
                                    self.__List_OF_fire_cords[i][1] - 20] \
                                        not in self.__List_OF_fire_cords:
                                    self.__List_OF_fire_cords.append(
                                        [self.__List_OF_fire_cords[i][0] + 20, self.__List_OF_fire_cords[i][1] - 20])
                        if y == 2:
                            if self.__List_OF_fire_cords[i][0] + 20 < 1480:
                                if [self.__List_OF_fire_cords[i][0] + 20,
                                    self.__List_OF_fire_cords[i][1]] \
                                        not in self.__List_OF_fire_cords:
                                    self.__List_OF_fire_cords.append(
                                        [self.__List_OF_fire_cords[i][0] + 20, self.__List_OF_fire_cords[i][1]])
                        if y == 3:
                            if (self.__List_OF_fire_cords[i][0] + 20 < 1480) and (
                                    self.__List_OF_fire_cords[i][1] + 20 < 730):
                                if [self.__List_OF_fire_cords[i][0] + 20,
                                    self.__List_OF_fire_cords[i][1] + 20] \
                                        not in self.__List_OF_fire_cords:
                                    self.__List_OF_fire_cords.append(
                                        [self.__List_OF_fire_cords[i][0] + 20, self.__List_OF_fire_cords[i][1] + 20])
                    if len(self.__List_OF_fire_cords) > 0:  # сгорание обьектов
                        if self.__Fridgefired:  # холодильник если не сгорел идет в условие
                            if 1025 < self.__List_OF_fire_cords[len(self.__List_OF_fire_cords) - 1][0] < 1202:
                                if 428 < self.__List_OF_fire_cords[len(self.__List_OF_fire_cords) - 1][1] < 520:
                                    self.__Fridgefired = False
                                    self.__Fridge.Change_Sostoianie()
                        if self.__BigsFruitsfired:  # Большая лавка если не сгорела идет в условие
                            if 1005 < self.__List_OF_fire_cords[len(self.__List_OF_fire_cords) - 1][0] < 1211:
                                if 228 < self.__List_OF_fire_cords[len(self.__List_OF_fire_cords) - 1][1] < 356:
                                    self.__BigsFruitsfired = False
                                    self.__BigsFruits.Change_Sostoianie()
                        if self.__Fruitsfired:  # лавка если не сгорела идет в условие
                            if 805 < self.__List_OF_fire_cords[len(self.__List_OF_fire_cords) - 1][0] < 897:
                                if 268 < self.__List_OF_fire_cords[len(self.__List_OF_fire_cords) - 1][1] < 400:
                                    self.__Fruitsfired = False
                                    self.__Fruits.Change_Sostoianie()
                    if self.__Changed:
                        if not self.__BigsFruitsfired and not self.__Fridgefired and not self.__Fruitsfired:
                            self.__Changed = False
                            self.__window.Change_Sostoianie()
                            self.__door.Change_Sostoianie()

        if self.__extinguishing:
            self.extinguishing()

    def Start_Fire(self, ):
        self.__magazin.Change_Fired()
        self.__List_OF_fire_cords.append([randint(820, 1400), randint(400, 690)])
        self.Add_Started_Fire(self.__List_OF_fire_cords[0])

        # if len(self.__List_OF_fire_cords) == 0: #возможность рандомного возгорания
        #     Chance = randint(1, 500)  # первое возгорание
        #     if Chance == 1:
        #         self.__List_OF_fire_cords.append([randint(820, 1400), randint(400, 690)])
