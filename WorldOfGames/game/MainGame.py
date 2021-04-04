from Live import live_class
from GuessGame import guess_game_class
from MemoryGame import memory_game_class
from CurrencyRoulatteGame import currency_roulette_game_class
from Score import score_class
from Utils import utils_class


class main_game_class:
    def start_game(self):
        utils = utils_class(txtFile=None, badCode=None)
        txt_file, bad_code = utils.start_utils()
        start_game = live_class(name=None, type=None, difficulty=None)
        start_game.welcome()
        game_type = start_game.load_game_type()
        difficulty = start_game.load_game_difficulty()
        if game_type == 1:
            memory_game = memory_game_class()
            outcome = memory_game.play_memory_game(difficulty)
        elif game_type == 2:
            guess_game = guess_game_class()
            outcome = guess_game.play_guess_game(difficulty)
        elif game_type == 3:
            roullete_game = currency_roulette_game_class()
            outcome = roullete_game.play_currency_game(difficulty)
            utils.screen_cleaner()
        if outcome == True:
            score_check = score_class(score=None)
            score_check.add_score(difficulty, txt_file)
        else:
            print("game finish")
