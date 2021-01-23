from Live import live_class
from GuessGame import guess_game_class
from MemoryGame import memory_game_class
from CurrencyRoulatteGame import currency_roulette_game_class
from Score import score_class
from Utils import utils_class



class main_game_class:

    def start_game(self):
        test = live_class(name = None, type = None, difficulty = None)
        test.welcome()
        type = test.load_game_type()
        difficulty = test.load_game_difficulty()
        if type == 1:
            test = memory_game_class()
            test.play_memory_game(difficulty)
        elif type == 2:
            test = guess_game_class()
            test.play_guess_game(difficulty)
        elif type == 3:
            test = currency_roulette_game_class()
            test.play_currency_game(difficulty)
        test1 = utils_class()
        test1.screen_cleaner()
        test1 = score_class(Score=None)
        exist = test1.add_score(difficulty)
        print("game finish")



x = main_game_class()
x.start_game()
