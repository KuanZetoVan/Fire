import pygame
from random import randint


class People(pygame.sprite.Sprite):  # класс Человека
    def __init__(self, location, product, Can_Be_A_Hero, displacement):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.__image = pygame.image.load('textures\Standart_People_Stay.png')
        self.__image.set_colorkey((0, 0, 0))
        self.__rect = self.__image.get_rect()
        self.__rect.left, self.__rect.top = location
        self.__Can_Be_A_Hero = Can_Be_A_Hero
        self.__product = product
        self.__status_Of_Live = True
        self.__time = 0
        self.__move = False
        self.__Choice_Of_Picture = 0
        self.__direction = None
        self.__Podoshel = 0
        self.__timer_Of_Staying = 0
        self.__displacement = displacement
        self.__status_Of_Hero = False
        self.__Inventory = []
        self.__Number_Of_Extinguisher = None
        self.__Sostoianie_Of_Run = 0
        self.__List_Of_People = []
        self.__image_crown = pygame.image.load('textures\Hero_Special.png')
        self.__image_crown.set_colorkey((0, 0, 0))

    def Get_Peoples(self):
        return self.__List_Of_People

    def Paint_Peoples(self, screen, time):
        for Peoples in self.__List_Of_People:
            if time == 30:
                Peoples.Update_Picture()
            if time == 60:
                Peoples.Update_Picture()
            if time == 90:
                Peoples.Update_Picture()
            if not Peoples.Get_Status_Of_Hero_Now():  # для обычных людей
                if not Peoples.Get_Move():
                    screen.blit(Peoples.Get_Image(), (Peoples.getleftcord() + Peoples.Get_displacement()[0],
                                                      Peoples.gettopcord() + Peoples.Get_displacement()[1]))
                if Peoples.Get_Move():
                    if Peoples.Get_direction() == 'Вправо' or Peoples.Get_direction() == 'Вверх':
                        screen.blit(Peoples.Get_Right_Move()[Peoples.Get_Choice_Of_Picture()],
                                    (Peoples.getleftcord() + Peoples.Get_displacement()[0],
                                     Peoples.gettopcord() + Peoples.Get_displacement()[1]))
                    if Peoples.Get_direction() == 'Влево' or Peoples.Get_direction() == 'Вниз':
                        screen.blit(Peoples.Get_Left_Move()[Peoples.Get_Choice_Of_Picture()],
                                    (Peoples.getleftcord() + Peoples.Get_displacement()[0],
                                     Peoples.gettopcord() + Peoples.Get_displacement()[1]))

            if Peoples.Get_Status_Of_Hero() == 'yes':  # для героев  Get_Status_Of_Hero_Now
                if not Peoples.Get_Move():
                    screen.blit(self.__image_crown, (Peoples.getleftcord() + Peoples.Get_displacement()[0] + 10,
                                                     Peoples.gettopcord() + Peoples.Get_displacement()[1] - 30))
                    screen.blit(Peoples.Get_Image(), (Peoples.getleftcord() + Peoples.Get_displacement()[0],
                                                      Peoples.gettopcord() + Peoples.Get_displacement()[1]))
                if Peoples.Get_Move():
                    if Peoples.Get_direction() == 'Вправо' or Peoples.Get_direction() == 'Вверх':
                        screen.blit(self.__image_crown, (Peoples.getleftcord() + Peoples.Get_displacement()[0] + 10,
                                                         Peoples.gettopcord() + Peoples.Get_displacement()[1] - 30))
                        screen.blit(Peoples.Get_Right_Move()[Peoples.Get_Choice_Of_Picture()],
                                    (Peoples.getleftcord() + Peoples.Get_displacement()[0],
                                     Peoples.gettopcord() + Peoples.Get_displacement()[1]))
                    if Peoples.Get_direction() == 'Влево' or Peoples.Get_direction() == 'Вниз':
                        screen.blit(self.__image_crown, (Peoples.getleftcord() + Peoples.Get_displacement()[0] + 10,
                                                         Peoples.gettopcord() + Peoples.Get_displacement()[1] - 30))
                        screen.blit(Peoples.Get_Left_Move()[Peoples.Get_Choice_Of_Picture()],
                                    (Peoples.getleftcord() + Peoples.Get_displacement()[0],
                                     Peoples.gettopcord() + Peoples.Get_displacement()[1]))

    def Move_Peoples(self, fire_list, fruits_store, fruits_big_store, Fridge, extinguisher, fire):
        for Peopless in self.__List_Of_People:
            if len(fire_list) == 0:
                if Peopless.Get_Status():
                    if Peopless.get_Sostoina_OF_Run() == 0:
                        if Peopless.Get_Product() == 'Fruit':
                            if fruits_store.Get_Printing():
                                if Peopless.Podoshel() == 0:
                                    if Peopless.gettopcord() > 298:  # Поднялся до уровня лавки
                                        Peopless.Set_Direction('Вверх')
                                        Peopless.Move_top()
                                    if Peopless.gettopcord() == 298:
                                        if Peopless.getleftcord() > 900:  # подошел к ней
                                            Peopless.Set_Direction('Влево')
                                            Peopless.Move_left()
                                        if Peopless.getleftcord() == 900:  # остановился
                                            if Peopless.Get_timer_Of_Staying() < 2001:
                                                Peopless.Stop_Move()
                                                Peopless.Place_Timer_Of_Staying(Peopless.Get_timer_Of_Staying() + 1)
                                            if Peopless.Get_timer_Of_Staying() == 2000:
                                                Peopless.Podoshel_up()
                                                Peopless.Place_Timer_Of_Staying(0)
                                if Peopless.Podoshel() == 1:
                                    if Peopless.getleftcord() < 950:  # ушел от нее
                                        Peopless.Set_Direction('Вправо')
                                        Peopless.Move_Right()
                                    if Peopless.getleftcord() == 950:
                                        if Peopless.gettopcord() < 550:  # опустился до кассы
                                            Peopless.Set_Direction('Вниз')
                                            Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 550:  # стоит у кассы
                                        if Peopless.Get_timer_Of_Staying() < 2001:
                                            Peopless.Stop_Move()
                                            Peopless.Place_Timer_Of_Staying(Peopless.Get_timer_Of_Staying() + 1)
                                        if Peopless.Get_timer_Of_Staying() == 2000:
                                            Peopless.Podoshel_up()
                                            Peopless.Place_Timer_Of_Staying(0)
                                if Peopless.Podoshel() == 2:
                                    if Peopless.gettopcord() < 700:  # вышел
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 700:
                                        self.__List_Of_People.remove(Peopless)
                            if not fruits_store.Get_Printing():
                                if Peopless.getleftcord() < 950:  # ушел от нее
                                    Peopless.Set_Direction('Вправо')
                                    Peopless.Move_Right()
                                if Peopless.getleftcord() == 950:
                                    if Peopless.gettopcord() < 700:  # вышел
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 700:
                                        self.__List_Of_People.remove(Peopless)
                                if Peopless.getleftcord() == 960:
                                    if Peopless.gettopcord() < 700:  # вышел
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 700:
                                        self.__List_Of_People.remove(Peopless)

                        if Peopless.Get_Product() == 'Big_Fruit':
                            if fruits_big_store.Get_Printing():
                                if Peopless.Podoshel() == 0:
                                    if Peopless.gettopcord() > 310:  # Поднялся до уровня лавки
                                        Peopless.Set_Direction('Вверх')
                                        Peopless.Move_top()
                                    if Peopless.gettopcord() == 310:
                                        if Peopless.getleftcord() < 1050:  # подошел к ней
                                            Peopless.Set_Direction('Вправо')
                                            Peopless.Move_Right()
                                        if Peopless.getleftcord() == 1050:  # остановился
                                            if Peopless.Get_timer_Of_Staying() < 2001:
                                                Peopless.Stop_Move()
                                                Peopless.Place_Timer_Of_Staying(Peopless.Get_timer_Of_Staying() + 1)
                                            if Peopless.Get_timer_Of_Staying() == 2000:
                                                Peopless.Podoshel_up()
                                                Peopless.Place_Timer_Of_Staying(0)
                                if Peopless.Podoshel() == 1:
                                    if Peopless.getleftcord() > 950:  # ушел от нее
                                        Peopless.Set_Direction('Влево')
                                        Peopless.Move_left()
                                    if Peopless.getleftcord() == 950:
                                        if Peopless.gettopcord() < 550:  # опустился до кассы
                                            Peopless.Set_Direction('Вниз')
                                            Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 550:  # стоит у кассы
                                        if Peopless.Get_timer_Of_Staying() < 2001:
                                            Peopless.Stop_Move()
                                            Peopless.Place_Timer_Of_Staying(Peopless.Get_timer_Of_Staying() + 1)
                                        if Peopless.Get_timer_Of_Staying() == 2000:
                                            Peopless.Podoshel_up()
                                            Peopless.Place_Timer_Of_Staying(0)
                                if Peopless.Podoshel() == 2:
                                    if Peopless.gettopcord() < 700:  # вышел
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 700:
                                        self.__List_Of_People.remove(Peopless)
                            if not fruits_big_store.Get_Printing():
                                if Peopless.getleftcord() > 950:  # ушел от нее
                                    Peopless.Set_Direction('Влево')
                                    Peopless.Move_left()
                                if Peopless.getleftcord() == 950:
                                    if Peopless.gettopcord() < 700:  # вышел
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 700:
                                        self.__List_Of_People.remove(Peopless)
                                if Peopless.getleftcord() == 960:
                                    if Peopless.gettopcord() < 700:  # вышел
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 700:
                                        self.__List_Of_People.remove(Peopless)

                        if Peopless.Get_Product() == 'Ice_Cream':
                            if Fridge.Get_Printing():
                                if Peopless.Podoshel() == 0:
                                    if Peopless.gettopcord() > 470:  # Поднялся до уровня морозильника
                                        Peopless.Set_Direction('Вверх')
                                        Peopless.Move_top()
                                    if Peopless.gettopcord() == 470:
                                        if Peopless.getleftcord() < 1050:  # подошел к нему
                                            Peopless.Set_Direction('Вправо')
                                            Peopless.Move_Right()
                                        if Peopless.getleftcord() == 1050:  # остановился
                                            if Peopless.Get_timer_Of_Staying() < 2001:
                                                Peopless.Stop_Move()
                                                Peopless.Place_Timer_Of_Staying(Peopless.Get_timer_Of_Staying() + 1)
                                            if Peopless.Get_timer_Of_Staying() == 2000:
                                                Peopless.Podoshel_up()
                                                Peopless.Place_Timer_Of_Staying(0)
                                if Peopless.Podoshel() == 1:
                                    if Peopless.getleftcord() > 950:  # ушел от него
                                        Peopless.Set_Direction('Влево')
                                        Peopless.Move_left()
                                    if Peopless.getleftcord() == 950:
                                        if Peopless.gettopcord() < 550:  # опустился до кассы
                                            Peopless.Set_Direction('Вниз')
                                            Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 550:  # стоит у кассы
                                        if Peopless.Get_timer_Of_Staying() < 2001:
                                            Peopless.Stop_Move()
                                            Peopless.Place_Timer_Of_Staying(Peopless.Get_timer_Of_Staying() + 1)
                                        if Peopless.Get_timer_Of_Staying() == 2000:
                                            Peopless.Podoshel_up()
                                            Peopless.Place_Timer_Of_Staying(0)
                                if Peopless.Podoshel() == 2:
                                    if Peopless.gettopcord() < 700:  # вышел
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 700:
                                        self.__List_Of_People.remove(Peopless)
                            if not Fridge.Get_Printing():
                                if Peopless.getleftcord() > 950:  # ушел от нее
                                    Peopless.Set_Direction('Влево')
                                    Peopless.Move_left()
                                if Peopless.getleftcord() == 950:
                                    if Peopless.gettopcord() < 700:  # вышел
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 700:
                                        self.__List_Of_People.remove(Peopless)
                                if Peopless.getleftcord() == 960:
                                    if Peopless.gettopcord() < 700:  # вышел
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 700:
                                        self.__List_Of_People.remove(Peopless)
                    if Peopless.Get_Extinguisher():
                        if Peopless.gettopcord() < 650:
                            Peopless.Set_Direction('Вниз')
                            Peopless.Move_Bot()
                        if Peopless.gettopcord() == 650:
                            if Peopless.getleftcord() > 950:
                                Peopless.Set_Direction('Влево')
                                Peopless.Move_left()
                            if Peopless.getleftcord() == 950:
                                Peopless.Move_Bot()

                        if Peopless.getleftcord() == 950 and Peopless.gettopcord() < 700:
                            Peopless.Set_Direction('Вниз')
                            Peopless.Move_Bot()
                        if Peopless.gettopcord() == 700:
                            self.__List_Of_People.remove(Peopless)

            else:
                if Peopless.Get_Status_Of_Hero() == 'no':
                    if Peopless.Get_Product() == 'Fruit':
                        if Peopless.getleftcord() < 950:  # ушел от нее
                            Peopless.Set_Direction('Вправо')
                            Peopless.Move_Right()
                        if Peopless.getleftcord() == 950:
                            if Peopless.gettopcord() < 700:  # вышел
                                Peopless.Set_Direction('Вниз')
                                Peopless.Move_Bot()
                            if Peopless.gettopcord() == 700:
                                self.__List_Of_People.remove(Peopless)
                        if Peopless.getleftcord() == 960:
                            if Peopless.gettopcord() < 700:  # вышел
                                Peopless.Set_Direction('Вниз')
                                Peopless.Move_Bot()
                            if Peopless.gettopcord() == 700:
                                self.__List_Of_People.remove(Peopless)
                    if Peopless.Get_Product() == 'Big_Fruit':
                        if Peopless.getleftcord() > 950:  # ушел от нее
                            Peopless.Set_Direction('Влево')
                            Peopless.Move_left()
                        if Peopless.getleftcord() == 950:
                            if Peopless.gettopcord() < 700:  # вышел
                                Peopless.Set_Direction('Вниз')
                                Peopless.Move_Bot()
                            if Peopless.gettopcord() == 700:
                                self.__List_Of_People.remove(Peopless)
                        if Peopless.getleftcord() == 960:
                            if Peopless.gettopcord() < 700:  # вышел
                                Peopless.Set_Direction('Вниз')
                                Peopless.Move_Bot()
                            if Peopless.gettopcord() == 700:
                                self.__List_Of_People.remove(Peopless)
                    if Peopless.Get_Product() == 'Ice_Cream':
                        if Peopless.getleftcord() > 950:  # ушел от нее
                            Peopless.Set_Direction('Влево')
                            Peopless.Move_left()
                        if Peopless.getleftcord() == 950:
                            if Peopless.gettopcord() < 700:  # вышел
                                Peopless.Set_Direction('Вниз')
                                Peopless.Move_Bot()
                            if Peopless.gettopcord() == 700:
                                self.__List_Of_People.remove(Peopless)
                        if Peopless.getleftcord() == 960:
                            if Peopless.gettopcord() < 700:  # вышел
                                Peopless.Set_Direction('Вниз')
                                Peopless.Move_Bot()
                            if Peopless.gettopcord() == 700:
                                self.__List_Of_People.remove(Peopless)
                if Peopless.Get_Status_Of_Hero() == 'yes':
                    if extinguisher.Getsostoianie() == 1:  # если огнетушителей нету

                        if Peopless.Get_Product() == 'Fruit':
                            if Peopless.getleftcord() < 950:  # ушел от нее
                                Peopless.Set_Direction('Вправо')
                                Peopless.Move_Right()
                            if Peopless.getleftcord() == 950:
                                if Peopless.gettopcord() < 700:  # вышел
                                    Peopless.Set_Direction('Вниз')
                                    Peopless.Move_Bot()
                                if Peopless.gettopcord() == 700:
                                    self.__List_Of_People.remove(Peopless)
                            if Peopless.getleftcord() == 960:
                                if Peopless.gettopcord() < 700:  # вышел
                                    Peopless.Set_Direction('Вниз')
                                    Peopless.Move_Bot()
                                if Peopless.gettopcord() == 700:
                                    self.__List_Of_People.remove(Peopless)
                        if Peopless.Get_Product() == 'Big_Fruit':
                            if Peopless.getleftcord() > 950:  # ушел от нее
                                Peopless.Set_Direction('Влево')
                                Peopless.Move_left()
                            if Peopless.getleftcord() == 950:
                                if Peopless.gettopcord() < 700:  # вышел
                                    Peopless.Set_Direction('Вниз')
                                    Peopless.Move_Bot()
                                if Peopless.gettopcord() == 700:
                                    self.__List_Of_People.remove(Peopless)
                            if Peopless.getleftcord() == 960:
                                if Peopless.gettopcord() < 700:  # вышел
                                    Peopless.Set_Direction('Вниз')
                                    Peopless.Move_Bot()
                                if Peopless.gettopcord() == 700:
                                    self.__List_Of_People.remove(Peopless)
                        if Peopless.Get_Product() == 'Ice_Cream':
                            if Peopless.getleftcord() > 950:  # ушел от нее
                                Peopless.Set_Direction('Влево')
                                Peopless.Move_left()
                            if Peopless.getleftcord() == 950:
                                if Peopless.gettopcord() < 700:  # вышел
                                    Peopless.Set_Direction('Вниз')
                                    Peopless.Move_Bot()
                                if Peopless.gettopcord() == 700:
                                    self.__List_Of_People.remove(Peopless)
                            if Peopless.getleftcord() == 960:
                                if Peopless.gettopcord() < 700:  # вышел
                                    Peopless.Set_Direction('Вниз')
                                    Peopless.Move_Bot()
                                if Peopless.gettopcord() == 700:
                                    self.__List_Of_People.remove(Peopless)
                if Peopless.Get_Status_Of_Hero() == 'yes':
                    if extinguisher.Getsostoianie() == 0:  # если есть огнетушители
                        if not Peopless.Get_Extinguisher():
                            if extinguisher.Get_Count_Of_Extinguisher() == 0:

                                if Peopless.Get_Product() == 'Fruit':
                                    if Peopless.getleftcord() < 950:  # ушел от нее
                                        Peopless.Set_Direction('Вправо')
                                        Peopless.Move_Right()
                                    if Peopless.getleftcord() == 950:
                                        if Peopless.gettopcord() < 700:  # вышел
                                            Peopless.Set_Direction('Вниз')
                                            Peopless.Move_Bot()
                                        if Peopless.gettopcord() == 700:
                                            self.__List_Of_People.remove(Peopless)
                                    if Peopless.getleftcord() == 960:
                                        if Peopless.gettopcord() < 700:  # вышел
                                            Peopless.Set_Direction('Вниз')
                                            Peopless.Move_Bot()
                                        if Peopless.gettopcord() == 700:
                                            self.__List_Of_People.remove(Peopless)
                                if Peopless.Get_Product() == 'Big_Fruit':
                                    if Peopless.getleftcord() > 950:  # ушел от нее
                                        Peopless.Set_Direction('Влево')
                                        Peopless.Move_left()
                                    if Peopless.getleftcord() == 950:
                                        if Peopless.gettopcord() < 700:  # вышел
                                            Peopless.Set_Direction('Вниз')
                                            Peopless.Move_Bot()
                                        if Peopless.gettopcord() == 700:
                                            self.__List_Of_People.remove(Peopless)
                                    if Peopless.getleftcord() == 960:
                                        if Peopless.gettopcord() < 700:  # вышел
                                            Peopless.Set_Direction('Вниз')
                                            Peopless.Move_Bot()
                                        if Peopless.gettopcord() == 700:
                                            self.__List_Of_People.remove(Peopless)
                                if Peopless.Get_Product() == 'Ice_Cream':
                                    if Peopless.getleftcord() > 950:  # ушел от нее
                                        Peopless.Set_Direction('Влево')
                                        Peopless.Move_left()
                                    if Peopless.getleftcord() == 950:
                                        if Peopless.gettopcord() < 700:  # вышел
                                            Peopless.Set_Direction('Вниз')
                                            Peopless.Move_Bot()
                                        if Peopless.gettopcord() == 700:
                                            self.__List_Of_People.remove(Peopless)
                                    if Peopless.getleftcord() == 960:
                                        if Peopless.gettopcord() < 700:  # вышел
                                            Peopless.Set_Direction('Вниз')
                                            Peopless.Move_Bot()
                                        if Peopless.gettopcord() == 700:
                                            self.__List_Of_People.remove(Peopless)
                            if extinguisher.Get_Count_Of_Extinguisher() == 2:  # Левый огнетушитель на месте
                                if Peopless.getleftcord() < 960:
                                    Peopless.Set_Direction('Вправо')
                                    Peopless.Move_Right()
                                if Peopless.getleftcord() > 960:
                                    Peopless.Set_Direction('Влево')
                                    Peopless.Move_left()
                                if Peopless.getleftcord() == 960:
                                    if Peopless.gettopcord() > 250:
                                        Peopless.Set_Direction('Вверх')
                                        Peopless.Move_top()
                                    if Peopless.gettopcord() < 250:
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 250:
                                        Peopless.Change_Status_Of_Hero_Now()
                                        Peopless.set_Number_Of_Extinguisher(1)
                                        Peopless.Add_Extinguisher('Extinguisher')  # взял левый огнетушитель
                                        extinguisher.Take_Extinguisher()
                                        extinguisher.Delete_First_Extinguisher()
                                        extinguisher.Take_Extinguisher()
                        if Peopless.Get_Extinguisher():
                            if fire_list[0][0] <= 960:
                                if 900 < Peopless.getleftcord() <= 960:
                                    Peopless.Set_Direction('Вправо')
                                    Peopless.Move_Right()
                                if not 900 < Peopless.getleftcord() <= 960:
                                    if Peopless.gettopcord() > fire_list[0][1] + 50:
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_top()
                                    if Peopless.gettopcord() < fire_list[0][1] - 50:
                                        Peopless.Set_Direction('Вверх')
                                        Peopless.Move_Bot()

                                if fire_list[0][0] <= 960 and (Peopless.gettopcord() == fire_list[0][1] + 50) or (
                                        Peopless.gettopcord() == fire_list[0][1] - 50):
                                    Peopless.Stop_Move()
                                    fire.start_extinguishing()
                                    Peopless.Set_New_Image('Left')
                                    Peopless.Set_Sosoianie()

                            if 960 < fire_list[0][0] < 1100:  # если он находится в холодильниках
                                if Peopless.get_Sostoina_OF_Run() == 0:
                                    Peopless.Up_Run()
                                if Peopless.get_Sostoina_OF_Run() == 1:
                                    if Peopless.getleftcord() < 980:
                                        Peopless.Set_Direction('Вправо')
                                        Peopless.Move_Right()
                                    if Peopless.getleftcord() == 980:
                                        Peopless.Up_Run()
                                if Peopless.get_Sostoina_OF_Run() == 2:
                                    if Peopless.gettopcord() < fire_list[0][1]:
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == fire_list[0][1]:
                                        Peopless.Stop_Move()
                                        fire.start_extinguishing()
                                        Peopless.Set_New_Image('Right')
                                        Peopless.Set_Sosoianie()

                            if 1100 <= fire_list[0][0] < 1200:  # если он находится в холодильниках
                                if Peopless.get_Sostoina_OF_Run() == 0:
                                    Peopless.Up_Run()
                                if Peopless.get_Sostoina_OF_Run() == 1:
                                    if Peopless.gettopcord() < 320:
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == 320:
                                        Peopless.Up_Run()
                                if Peopless.get_Sostoina_OF_Run() == 2:
                                    if Peopless.getleftcord() < 1200:
                                        Peopless.Set_Direction('Вправо')
                                        Peopless.Move_Right()
                                    if Peopless.getleftcord() == 1200:
                                        Peopless.Up_Run()
                                if Peopless.get_Sostoina_OF_Run() == 3:
                                    if Peopless.gettopcord() > fire_list[0][1]:
                                        Peopless.Set_Direction('Вверх')
                                        Peopless.Move_top()
                                    if Peopless.gettopcord() < fire_list[0][1]:
                                        Peopless.Set_Direction('Вниз')
                                        Peopless.Move_Bot()
                                    if Peopless.gettopcord() == fire_list[0][1]:
                                        Peopless.Stop_Move()
                                        fire.start_extinguishing()
                                        Peopless.Set_New_Image('Left')
                                        Peopless.Set_Sosoianie()

                            if fire_list[0][0] >= 1200:  # если огонь в правой части экрана
                                if Peopless.Get_Number_Of_Extinguisher() == 1:
                                    if Peopless.getleftcord() <= 1200:
                                        if Peopless.gettopcord() < 310:
                                            Peopless.Set_Direction('Вверх')
                                            Peopless.Move_Bot()
                                        if Peopless.gettopcord() > 310:
                                            Peopless.Set_Direction('Вниз')
                                            Peopless.Move_top()
                                        if Peopless.gettopcord() == 310:
                                            Peopless.Set_Direction('Вправо')
                                            Peopless.Move_Right()
                                    if Peopless.getleftcord() > 1200:
                                        if Peopless.gettopcord() > fire_list[0][1]:
                                            if Peopless.getleftcord() < fire_list[0][0] - 50:
                                                Peopless.Set_Direction('Вправо')
                                                Peopless.Move_Right()
                                            if Peopless.getleftcord() == fire_list[0][0] - 50:
                                                Peopless.Up_Run()
                                            if Peopless.get_Sostoina_OF_Run() == 1:
                                                Peopless.Stop_Move()
                                                fire.start_extinguishing()
                                                Peopless.Set_New_Image('Right')
                                                Peopless.Set_Sosoianie()
                                        if Peopless.gettopcord() < fire_list[0][1] - 50:
                                            Peopless.Move_Bot()
                                            Peopless.Set_Direction('Вниз')
                                        if Peopless.gettopcord() == fire_list[0][1] - 50:
                                            Peopless.Up_Run()
                                        if Peopless.get_Sostoina_OF_Run() >= 1:
                                            Peopless.Stop_Move()
                                            fire.start_extinguishing()
                                            Peopless.Set_New_Image('Right')
                                            Peopless.Set_Sosoianie()

    def Create_Random_Peoples(self):

        Product = randint(1, 3)
        if Product == 1:
            Product = 'Fruit'
        elif Product == 2:
            Product = 'Big_Fruit'
        elif Product == 3:
            Product = 'Ice_Cream'

        Can_Be_A_Hero = randint(1, 5)
        if Can_Be_A_Hero == 1:
            Can_Be_A_Hero = 'yes'
        else:
            Can_Be_A_Hero = 'no'

        Type_Of_People = randint(1, 3)
        if Type_Of_People == 1:
            grand_Father = Grand_Father(Product, Can_Be_A_Hero, (960, 650), [randint(-10, 20), randint(-5, 20)])
            self.__List_Of_People.append(grand_Father)
        if Type_Of_People == 2:
            standard_People = Standard_People(Product, Can_Be_A_Hero, (960, 650), [randint(-10, 20), randint(-5, 20)])
            self.__List_Of_People.append(standard_People)
        if Type_Of_People == 3:
            african_People = African_People(Product, Can_Be_A_Hero, (960, 650), [randint(-10, 20), randint(-5, 20)])
            self.__List_Of_People.append(african_People)

    def del_Extinguisher(self):
        self.__Inventory = []

    def Set_Sosoianie(self):
        self.__Sostoianie_Of_Run = 1

    def Up_Run(self):
        self.__Sostoianie_Of_Run += 1

    def get_Sostoina_OF_Run(self):
        return self.__Sostoianie_Of_Run

    def Get_Number_Of_Extinguisher(self):
        return self.__Number_Of_Extinguisher

    def set_Number_Of_Extinguisher(self, number):
        self.__Number_Of_Extinguisher = number

    def Get_Extinguisher(self):
        for item in self.__Inventory:
            if item == 'Extinguisher':
                return True
            else:
                return False

    def Add_Extinguisher(self, Extinguisher):
        self.__Inventory.append(Extinguisher)

    def Change_Status_Of_Hero_Now(self):
        if self.__status_Of_Hero:
            self.__status_Of_Hero = False
        if not self.__status_Of_Hero:
            self.__status_Of_Hero = True

    def Get_Status_Of_Hero_Now(self):
        return self.__status_Of_Hero

    def Get_displacement(self):
        return self.__displacement

    def Get_Status_Of_Hero(self):
        return self.__Can_Be_A_Hero

    def Get_timer_Of_Staying(self):
        return self.__timer_Of_Staying

    def Place_Timer_Of_Staying(self, new):
        self.__timer_Of_Staying = new

    def Podoshel_up(self):
        self.__Podoshel += 1

    def Stop_Move(self):
        self.__move = False

    def Podoshel(self):
        return self.__Podoshel

    def Move_top(self):
        self.__move = True
        self.__rect.top -= 1

    def Move_Right(self):
        self.__move = True
        self.__rect.left += 1

    def Move_Bot(self):
        self.__move = True
        self.__rect.top += 1

    def Move_left(self):
        self.__move = True
        self.__rect.left -= 1

    def Get_Choice_Of_Picture(self):
        return self.__Choice_Of_Picture

    def Get_direction(self):
        return self.__direction

    def Set_Direction(self, New_Direction):
        self.__direction = New_Direction

    def Update_Picture(self):
        if self.__Choice_Of_Picture == 3:
            self.__Choice_Of_Picture = 0
        else:
            self.__Choice_Of_Picture += 1

    def Get_Move(self):
        return self.__move

    def Get_time(self):
        return self.__time

    def Get_Product(self):
        return self.__product

    def Change_Status(self):
        self.__status_Of_Live = False

    def Get_Status(self):
        return self.__status_Of_Live

    def Get_Image(self):
        return self.__image

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


class Grand_Father(People):
    def __init__(self, product, Can_Be_A_Hero, location, displacement):
        super().__init__(location, product, Can_Be_A_Hero, displacement)
        self.__Can_Be_A_Hero = Can_Be_A_Hero
        self.__product = product
        self.__image_file_Stay = pygame.image.load('textures\Gray_People_Stay.png')
        self.__image_file_Die = pygame.image.load('textures\Gray_People_Die.png')
        self.__image_list_right_walk = [pygame.image.load('textures\Gray_People_Move1_Right.png'),
                                        pygame.image.load('textures\Gray_People_Move2_Right.png'),
                                        pygame.image.load('textures\Gray_People_Move3_Right.png'),
                                        pygame.image.load('textures\Gray_People_Move4_Right.png')]
        for move in self.__image_list_right_walk:
            move.set_colorkey((0, 0, 0))
        self.__image_list_left_walk = [pygame.image.load('textures\Gray_People_Move1_Left.png'),
                                       pygame.image.load('textures\Gray_People_Move2_Left.png'),
                                       pygame.image.load('textures\Gray_People_Move3_Left.png'),
                                       pygame.image.load('textures\Gray_People_Move4_Left.png')]
        for move in self.__image_list_left_walk:
            move.set_colorkey((0, 0, 0))
        self.__image = pygame.image.load('textures\Gray_People_Stay.png')
        self.__image.set_colorkey((0, 0, 0))
        self.__image_file_Stay.set_colorkey((0, 0, 0))
        self.__image_file_Die.set_colorkey((0, 0, 0))

    def Set_New_Image(self, direction):
        if direction == 'Right':
            self.__image = pygame.image.load('textures\Gray_People_extinguishing_Right.png')
        if direction == 'Left':
            self.__image = pygame.image.load('textures\Gray_People_extinguishing_Left.png')
        self.__image.set_colorkey((0, 0, 0))

    def Get_Right_Move(self):
        return self.__image_list_right_walk

    def Get_Left_Move(self):
        return self.__image_list_left_walk

    def Get_Image(self):
        return self.__image

    def Die(self):
        self.__image = self.__image_file_Die


class Standard_People(People):
    def __init__(self, product, Can_Be_A_Hero, location, displacement):
        super().__init__(location, product, Can_Be_A_Hero, displacement)
        self.__Can_Be_A_Hero = Can_Be_A_Hero
        self.__product = product
        self.__image_file_Stay = pygame.image.load('textures\Standart_People_Stay.png')
        self.__image_file_Die = pygame.image.load('textures\Standart_People_Die.png')
        self.__image_list_right_walk = [pygame.image.load('textures\Standart_People_Move1_Right.png'),
                                        pygame.image.load('textures\Standart_People_Move2_Right.png'),
                                        pygame.image.load('textures\Standart_People_Move3_Right.png'),
                                        pygame.image.load('textures\Standart_People_Move4_Right.png'), ]
        for move in self.__image_list_right_walk:
            move.set_colorkey((0, 0, 0))
        self.__image_list_left_walk = [pygame.image.load('textures\Standart_People_Move1_Left.png'),
                                       pygame.image.load('textures\Standart_People_Move2_Left.png'),
                                       pygame.image.load('textures\Standart_People_Move3_Left.png'),
                                       pygame.image.load('textures\Standart_People_Move4_Left.png'), ]
        for move in self.__image_list_left_walk:
            move.set_colorkey((0, 0, 0))
        self.__image = pygame.image.load('textures\Standart_People_Stay.png')
        self.__image_file_Die.set_colorkey((0, 0, 0))
        self.__image_file_Stay.set_colorkey((0, 0, 0))
        self.__image.set_colorkey((0, 0, 0))

    def Set_New_Image(self, direction):
        if direction == 'Right':
            self.__image = pygame.image.load('textures\Standart_People_extinguishing_Right.png')
        if direction == 'Left':
            self.__image = pygame.image.load('textures\Standart_People_extinguishing_Left.png')
        self.__image.set_colorkey((0, 0, 0))

    def Get_Right_Move(self):
        return self.__image_list_right_walk

    def Get_Left_Move(self):
        return self.__image_list_left_walk

    def Get_Image(self):
        return self.__image

    def Die(self):
        self.__image = self.__image_file_Die


class African_People(People):
    def __init__(self, product, Can_Be_A_Hero, location, displacement):
        super().__init__(location, product, Can_Be_A_Hero, displacement)
        self.__Can_Be_A_Hero = Can_Be_A_Hero
        self.__product = product
        self.__image_file_Stay = pygame.image.load('textures\African_People_Stay.png')
        self.__image_file_Die = pygame.image.load('textures\African_People_Die.png')
        self.__image_list_right_walk = [pygame.image.load('textures\African_People_Move1_Right.png'),
                                        pygame.image.load('textures\African_People_Move2_Right.png'),
                                        pygame.image.load('textures\African_People_Move3_Right.png'),
                                        pygame.image.load('textures\African_People_Move4_Right.png'), ]
        for move in self.__image_list_right_walk:
            move.set_colorkey((0, 0, 0))
        self.__image_list_left_walk = [pygame.image.load('textures\African_People_Move1_Left.png'),
                                       pygame.image.load('textures\African_People_Move2_Left.png'),
                                       pygame.image.load('textures\African_People_Move3_Left.png'),
                                       pygame.image.load('textures\African_People_Move4_Left.png'), ]
        for move in self.__image_list_left_walk:
            move.set_colorkey((0, 0, 0))
        self.__image = pygame.image.load('textures\African_People_Stay.png')
        self.__image.set_colorkey((0, 0, 0))
        self.__image_file_Stay.set_colorkey((0, 0, 0))
        self.__image_file_Die.set_colorkey((0, 0, 0))

    def Set_New_Image(self, direction):
        if direction == 'Right':
            self.__image = pygame.image.load('textures\African_People_extinguishing_Right.png')
        if direction == 'Left':
            self.__image = pygame.image.load('textures\African_People_extinguishing_Left.png')
        self.__image.set_colorkey((0, 0, 0))

    def Get_Right_Move(self):
        return self.__image_list_right_walk

    def Get_Left_Move(self):
        return self.__image_list_left_walk

    def Get_Image(self):
        return self.__image

    def Die(self):
        self.__image = self.__image_file_Die
