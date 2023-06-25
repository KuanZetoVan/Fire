from Class_Magazin import *
from Class_Fire import *


class Interface:
    def __init__(self, width, height, screen, font, entity_list):
        self.__width = width
        self.__height = height
        self.__inactive_color = (25, 190, 225)
        self.__hover_color = (75, 225, 255)
        self.__active_color = (50, 150, 255)
        self.__textcol = (255, 255, 255)
        self.__screen = screen
        self.__font = font
        self.__entity_list = entity_list

    def Start_Fire(self):
        for Fires in self.__entity_list:
            if isinstance(Fires, Fire):
                Fires.Start_Fire()

    def Change_Windows(self):
        for window in self.__entity_list:
            if isinstance(window, Windows):
                window.Change_Sostoianie()

    def Change_Extinguisher(self):
        for Extinguishers in self.__entity_list:
            if isinstance(Extinguishers, Extinguisher):
                Extinguishers.Change_Sostoianie()

    def Change_Sostoianie_Fruits(self):
        for store in self.__entity_list:
            if isinstance(store, Fruits_Store):
                store.Change_Sostoianie()

    def Change_Sostoianie_Fruits_Big(self):
        for store in self.__entity_list:
            if isinstance(store, Store_Big):
                store.Change_Sostoianie()

    def Change_Fruits_Store(self):
        for store in self.__entity_list:
            if isinstance(store, Fruits_Store):
                store.Change_Printing()

    def Change_Fruits_Store_Big(self):
        for store in self.__entity_list:
            if isinstance(store, Store_Big):
                store.Change_Printing()

    def Change_Fridge(self):
        for Fridges in self.__entity_list:
            if isinstance(Fridges, Fridge):
                Fridges.Change_Printing()

    def Change_Fridge_Sostoianie(self):
        for Fridges in self.__entity_list:
            if isinstance(Fridges, Fridge):
                Fridges.Change_Sostoianie()

    def Draw(self, x, y, text, action):
        if action == 'start_Fire':
            action = self.Start_Fire
        if action == 'okno':
            action = self.Change_Windows
        if action == 'exti':
            action = self.Change_Extinguisher
        if action == 'fruits':
            action = self.Change_Fruits_Store
        if action == 'big_Store':
            action = self.Change_Fruits_Store_Big
        if action == 'fruits_Change':
            action = self.Change_Sostoianie_Fruits
        if action == 'big_Store_Change':
            action = self.Change_Sostoianie_Fruits_Big
        if action == 'Fridge_Off':
            action = self.Change_Fridge
        if action == 'Fridge_Change':
            action = self.Change_Fridge_Sostoianie
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.__width:
            if y < mouse[1] < y + self.__height:
                pygame.draw.rect(self.__screen, self.__active_color, (x, y, self.__width, self.__height))
                if click[0] == 1 and action is not None:
                    pygame.time.delay(200)
                    action()
            else:
                pygame.draw.rect(self.__screen, self.__inactive_color, (x, y, self.__width, self.__height))
        else:
            pygame.draw.rect(self.__screen, self.__inactive_color, (x, y, self.__width, self.__height))
        text_img = self.__font.render(text, True, self.__textcol)
        if len(text) > 6:
            self.__screen.blit(text_img, (x, y + self.__height / 2 - 15))
        if len(text) < 6:
            self.__screen.blit(text_img, (x + 20, y + self.__height / 2 - 15))
