import Live
from Live import live_class
import random

class guess_game_class:

    def __init__(self, secretNumber = None, userNumber = None):
        self._secretNumber = secretNumber
        self._userNumber = userNumber

    @property
    def get_secret_number(self):
        """
        here we get the secret number
        """
        return self._secretNumber

    @property
    def get_user_number(self):
        """
        here we get the user number
        """
        return self._userNumber

    @get_secret_number.setter
    def set_secret_number(self, x):
        """
        here we set the secret number
        """
        secret_number = x
        self._secretNumber = secret_number

    @get_user_number.setter
    def set_user_number(self, x):
        """
        here we set the user number
        """
        try:
            user_number = int(x)
        except ValueError:
            print("please enter an integer")
            breakpoint()
        self._userNumber = user_number

    def generate_number(self, difficulty):
        """
        here we generate a secret number
        """
        self.set_secret_number = random.randint(1, difficulty)
        return self.set_secret_number

    def get_guess_from_user(self, difficulty):
        """
        here we generate a number from the user
        """
        self.set_user_number = int(input("please select a number between 1 to " + str(difficulty) + ":"))
        if self.set_user_number > difficulty:
            print("not a valid number, please enter a number from 1 to " + difficulty)
            raise breakpoint()
        return self._userNumber

    def compare_results(self, secret_number, user_number):
        print("\n")
        print(secret_number)
        print(user_number)
        if secret_number != user_number:
            print("wrong, this is not the secret number")
            return False
        else:
            print("success, you selected the correct number")
            return True

    def play_guess_game(self, difficulty):
        """
        here we start the guessing game and return True or False
        """
        x = guess_game_class(secretNumber=None, userNumber=None)
        secret_number = x.generate_number(difficulty)
        user_number = x.get_guess_from_user(difficulty)
        compare_resut = x.compare_results(secret_number, user_number)
        if compare_resut == True:
            print("you win!!!")
            return True
        else:
            print("you lose!!!")
            return False

