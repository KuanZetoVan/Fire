import pygame


class Fridge(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.__image = pygame.image.load('textures\Fridge.png')
        self.__image_Broken = pygame.image.load('textures\Fridge_Broken.png')
        self.__image.set_colorkey((0, 0, 0))
        self.__image_Broken.set_colorkey((0, 0, 0))
        self.__rect = self.__image.get_rect()
        self.__screen = screen
        self.__Sostoianie = 0
        self.__Printing = True
        self.__location = (1035, 428)

    def Get_Printing(self):
        return self.__Printing

    def Get_Location(self):
        return self.__location

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

    def Getsostoianie(self):
        return self.__Sostoianie

    def Change_Sostoianie(self):
        if self.__Sostoianie == 0:
            self.__Sostoianie = 1
        else:
            self.__Sostoianie = 0

    def Change_Printing(self):
        if self.__Printing:
            self.__Printing = False
            return
        if not self.__Printing:
            self.__Printing = True
            return

    def Print_On_Canvas(self):
        if self.__Printing:
            if self.__Sostoianie == 0:
                self.__screen.blit(self.__image, self.__location)
            if self.__Sostoianie == 1:
                self.__screen.blit(self.__image_Broken, self.__location)


class Store_Big(pygame.sprite.Sprite):  # класс большой фруктовой лавки
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.__image = pygame.image.load('textures\Fruits_Store_Big.png')
        self.__image_Broken = pygame.image.load('textures\Fruits_Store_Big_Broken.png')
        self.__image.set_colorkey((0, 0, 0))
        self.__image_Broken.set_colorkey((0, 0, 0))
        self.__rect = self.__image.get_rect()
        self.__screen = screen
        self.__Sostoianie = 0
        self.__Printing = True
        self.__location = (1015, 228)

    def Get_Printing(self):
        return self.__Printing

    def Get_Location(self):
        return self.__location

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

    def Getsostoianie(self):
        return self.__Sostoianie

    def Change_Sostoianie(self):
        if self.__Sostoianie == 0:
            self.__Sostoianie = 1
        else:
            self.__Sostoianie = 0

    def Change_Printing(self):
        if self.__Printing:
            self.__Printing = False
            return
        if not self.__Printing:
            self.__Printing = True
            return

    def Print_On_Canvas(self):
        if self.__Printing:
            if self.__Sostoianie == 0:
                self.__screen.blit(self.__image, self.__location)
            if self.__Sostoianie == 1:
                self.__screen.blit(self.__image_Broken, self.__location)


class Fruits_Store(pygame.sprite.Sprite):  # класс фруктовой лавки
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.__image = pygame.image.load('textures\Fruits_Store.png')
        self.__image_Broken = pygame.image.load('textures\Fruits_Store_Broken.png')
        self.__image.set_colorkey((0, 0, 0))
        self.__image_Broken.set_colorkey((0, 0, 0))
        self.__rect = self.__image.get_rect()
        self.__screen = screen
        self.__Sostoianie = 0
        self.__Printing = True
        self.__location = (815, 268)

    def Get_Printing(self):
        return self.__Printing

    def Get_Location(self):
        return self.__location

    def getrect(self):
        return self.__rect

    def Getsostoianie(self):
        return self.__Sostoianie

    def Change_Sostoianie(self):
        if self.__Sostoianie == 0:
            self.__Sostoianie = 1
        else:
            self.__Sostoianie = 0

    def Change_Printing(self):
        if self.__Printing:
            self.__Printing = False
            return
        if not self.__Printing:
            self.__Printing = True
            return

    def Print_On_Canvas(self):
        if self.__Printing:
            if self.__Sostoianie == 0:
                self.__screen.blit(self.__image, self.__location)
            if self.__Sostoianie == 1:
                self.__screen.blit(self.__image_Broken, self.__location)

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


class Extinguisher(pygame.sprite.Sprite):  # класс огнетушителя
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.__image = pygame.image.load('textures\extinguisher.png')
        self.__image.set_colorkey((0, 0, 0))
        self.__rect = self.__image.get_rect()
        self.__screen = screen
        self.__Sostoianie = 0
        self.__Print_First_Extinguisher = True
        self.__Print_Second_Extinguisher = True
        self.__count_Of_Extinguisher = 2

    def Get_Count_Of_Extinguisher(self):
        return self.__count_Of_Extinguisher

    def Take_Extinguisher(self):
        self.__count_Of_Extinguisher -= 1

    def Getsostoianie(self):
        return self.__Sostoianie

    def Change_Sostoianie(self):
        if self.__Sostoianie == 0:
            self.__Sostoianie = 1
        else:
            self.__Sostoianie = 0

    def Delete_First_Extinguisher(self):
        self.__Print_First_Extinguisher = False

    def Delete_Second_Extinguisher(self):
        self.__Print_First_Extinguisher = False

    def Print_On_Canvas(self):
        if self.__Sostoianie == 0:
            if self.__Print_Second_Extinguisher:
                self.__screen.blit(self.__image, (1435, 268))
            if self.__Print_First_Extinguisher:
                self.__screen.blit(self.__image, (965, 268))


class Windows(pygame.sprite.Sprite):  # класс окон
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.__image_Right_Top = pygame.image.load('textures\Right_Top_window.png')
        self.__image_Right_Top_Break = pygame.image.load('textures\Right_Top_window_Break.png')
        self.__image_Left_Top = pygame.image.load('textures\Left_Top_window.png')
        self.__image_Left_Top_Break = pygame.image.load('textures\Left_Top_Window_Break.png')
        self.__imaage_Right_Down = pygame.image.load('textures\Right_Down_Window.png')
        self.__imaage_Right_Down_Break = pygame.image.load('textures\Right_Down_Window_Break.png')
        self.__imaage_Glass_Shards = pygame.image.load('textures\Broken_Glass_Shards.png')
        self.__imaage_Glass_Shards.set_colorkey((0, 0, 0))
        self.__screen = screen
        self.__Sostoianie = 0

    def Change_Sostoianie(self):
        if self.__Sostoianie == 0:
            self.__Sostoianie = 1
        else:
            self.__Sostoianie = 0

    def Getsostoianie(self):
        return self.__Sostoianie

    def Print_On_Canvas(self):
        if self.__Sostoianie == 0:
            self.__screen.blit(self.__image_Right_Top, (313, 438))
            self.__screen.blit(self.__image_Right_Top, (518, 438))
            self.__screen.blit(self.__image_Left_Top, (58, 438))
            self.__screen.blit(self.__imaage_Right_Down, (313, 560))
            self.__screen.blit(self.__imaage_Right_Down, (518, 560))
        if self.__Sostoianie == 1:
            self.__screen.blit(self.__image_Right_Top_Break, (313, 438))
            self.__screen.blit(self.__image_Right_Top_Break, (518, 438))
            self.__screen.blit(self.__image_Left_Top_Break, (58, 438))
            self.__screen.blit(self.__imaage_Right_Down_Break, (313, 560))
            self.__screen.blit(self.__imaage_Right_Down_Break, (518, 560))
            self.__screen.blit(self.__imaage_Glass_Shards, (1100, 700))
            self.__screen.blit(self.__imaage_Glass_Shards, (1140, 690))


class Door(pygame.sprite.Sprite):  # класс двери
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.__image = pygame.image.load('textures\Door_Closed.png')
        self.__image_Open = pygame.image.load('textures\Door_Open.png')
        self.__rect = self.__image.get_rect()
        self.__screen = screen
        self.__Sostoianie = 0
        self.__location = (58, 560)

    def Change_Sostoianie(self):
        if self.__Sostoianie == 0:
            self.__Sostoianie = 1
        else:
            self.__Sostoianie = 0

    def Getsostoianie(self):
        return self.__Sostoianie

    def Print_On_Canvas(self):
        if self.__Sostoianie == 0:
            self.__screen.blit(self.__image, self.__location)
        if self.__Sostoianie == 1:
            self.__screen.blit(self.__image_Open, self.__location)

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

    def getimage(self):
        return self.__image


class Magazine(pygame.sprite.Sprite):  # класс Фона
    def __init__(self, location, screen):
        pygame.sprite.Sprite.__init__(self)
        self.__image = pygame.image.load('textures\shop.png')
        self.__image.set_colorkey((0, 0, 0))
        self.__rect = self.__image.get_rect()
        self.__rect.left, self.__rect.top = location
        self.__screen = screen
        self.__List_Of_Entity = []
        self.__fired = False

    def Change_Fired(self):
        self.__fired = True

    def Get_Fired(self):
        return self.__fired

    def Add_Entity(self, List):
        for i in List:
            self.__List_Of_Entity.append(i)

    def Print_All(self):
        self.__screen.blit(self.getimage(), (self.getleftcord(), self.gettopcord()))
        for Entity in self.__List_Of_Entity:
            Entity.Print_On_Canvas()

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

    def getimage(self):
        return self.__image
