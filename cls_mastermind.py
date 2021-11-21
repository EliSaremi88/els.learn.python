from random import randint
from datetime import datetime
class mastermind :
    '''description mastermind
    '''
    def __init__ (self , level) :
        self.__set_level( level )
        self.__set_random_number()
        self.__status == True
        self.__set_game_date()
        self.__set_counter()

    @property
    def status (self) :
        return self.__status    
    @property
    def counter (self) :
        return self.__counter

    def __set_counter(self) :
        self.__counter = 0  
    @property
    def game_date (self) :
        return self.__date

    def __set_game_date(self) :
        self.__date = datetime.now()


    def __set_random_number(self) :
         self.__random_number = mastermind.__create_random_number(self.__level)

    def __set_level(self , level):
        if level not in range (4 , 10):
            raise ValueError("invalid level!!!")   
        self.__level = level  
    @property
    def level (self):
        return self.__level      
@staticmethod
def __create_random_number (level):
    return randint(10**(level -1), 10**(level)-1)

def check_guess_number (self , number):
    self.__counter += 1
    if number < self.__random_number :
        return -1
    elif number > self.__random_number : 
        return 1
    else :
        self.__status == False
        self.__date = datetime.now() - self.__date
        return 0       

