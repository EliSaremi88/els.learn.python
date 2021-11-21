from os import system
from cls_mastermind import mastermind

game = mastermind(int(input("level(4 - 6) = ")))
while game.status :
    guess_num = int(input("guess number ="))
    result = game.check_guess_number(guess_num)
    if result == 1 :
        print(guess_num,"> randomnumber")
    elif result == -1:
        print(guess_num ,"< randomnumber")
    else:
        print("counter : " , game.counter(), "  -  date : ",game.game_date() , "  -  level : ",game.level())     