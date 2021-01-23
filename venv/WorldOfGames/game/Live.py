import random

class live_class:

    def __init__(self, name=None, type=None, difficulty=None):
        self._name = name
        self._type = type
        self._difficulty = difficulty

    @property
    def get_name(self):
        """
        here we get the user name
        """
        return self._name

    @property
    def get_type(self):
        """
        here we get the game type
        """
        return self._type

    @property
    def get_difficulty(self):
        """
        here we get the game difficulty level
        """
        return self._difficulty

    @get_name.setter
    def set_name(self, x):
        """
        here we set the user name
        """
        user_name = x
        print("Hello", user_name, "and welcome to the World of Games (WoG).Here you can find many cool games to play.")
        self._name = user_name

    @get_type.setter
    def set_type(self, x):
        """
        here we set the user game type chosen
        """
        option_lists = [1, 2, 3]
        try:
            game_type = int(x)
        except ValueError:
            print("please enter an integer")
            breakpoint()
        if game_type in option_lists:
            game_type = game_type
        else:
            print("not a valid number, please enter a number from 1 to 3")
            raise breakpoint()
        self._type = game_type

    @get_difficulty.setter
    def set_difficulty(self, x):
        """
        here we set the game difficulty level
        """
        option_list = [1,2,3,4,5]
        try:
            game_difficulty = int(x)
        except ValueError:
            print("please enter an integer")
            breakpoint()
        if game_difficulty in option_list:
            game_difficulty = game_difficulty
        else:
            print("not a valid number, please enter a number from 1 to " + str(game_difficulty))
            raise breakpoint()
        self._difficulty = game_difficulty


    def welcome(self):
        """
        here we call the name method and entering a vaule
        """
        self.set_name = (input("please enter your name: "))
        return self.set_name

    def load_game_type(self):
        """
        here we call the type and difficult methods  and entering values
        """
        self.set_type = (input("Please choose a game to play:\n"
                           "1. Memory Game - a sequence of numbers will appear for 1 second and you have to "
                           "guess "
                           "it "
                           "back\n"
                           "2. Guess Game - guess a number and see if you chose like the computer\n"
                           "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))
        return self._type

    def load_game_difficulty(self,):
        self.set_difficulty = (input("please chose game difficultly from 1 to 5:\n"))
        return self._difficulty
