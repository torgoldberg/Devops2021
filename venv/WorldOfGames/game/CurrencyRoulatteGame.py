import random
import requests

class currency_roulette_game_class:


    def __init__(self, get_url = None, get_guess_from_user = None):
        self._get_guess_from_user = get_guess_from_user
        self._get_url = get_url

    @property
    def get_user_guess(self):
        """
        here we get the user guess amount
        """
        return self._get_guess_from_user

    @property
    def get_url(self):
        """
        here we get the API url
        """
        return self._get_url

    @get_user_guess.setter
    def set_user_guess(self, x):
        """
        here we set the user guess amount
        """
        user_guess = x
        self._get_guess_from_user = user_guess

    @get_url.setter
    def set_url(self, x):
        """
        here we set the API url
        """
        url = x
        self._get_url = url

    def get_url(self):
        """
        here we get the currency exchange URL
        """
        YOUR_ACCESS_KEY = '69a97d4c656d4dcb804ccecdfa2640aa'
        self.set_url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)
        return self.set_url

    def get_money_interval(self,difficulty, random_number, url, user_guess):
        """
        here get the USD and convert it to ILS according to the difficulty level
        in addition here we check if the user guess is inside the correct number interval
        """
        interval_numbers = []
        data = requests.get(url).json()
        self.rates = data["rates"]
        # amount = random_number
        from_currency = 'USD'
        to_currency = 'ILS'
        if from_currency != "EUR":
            random_number = random_number / self.rates[from_currency]
        random_number = round(random_number * self.rates[to_currency], 2)
        random_number = int(random_number)
        if difficulty == 1:
            start_number = user_guess-5
            final_number = user_guess+6
            interval_numbers = list(range(start_number, final_number))
            while start_number <= 0 :
                start_number+1
        elif difficulty ==2:
            start_number = user_guess-4
            final_number = user_guess+5
            interval_numbers = list(range(start_number, final_number))
            while start_number <= 0 :
                start_number+1
        elif difficulty ==3:
            start_number = user_guess-3
            final_number = user_guess+4
            interval_numbers = list(range(start_number, final_number))
            while start_number <= 0 :
                start_number+1
        elif difficulty ==4:
            start_number = user_guess-2
            final_number = user_guess+3
            interval_numbers = list(range(start_number, final_number))
            while start_number <= 0 :
                start_number+1
        elif difficulty ==5:
            start_number = user_guess-1
            final_number = user_guess+2
            interval_numbers = list(range(start_number, final_number))
        interval_numbers = [number for number in interval_numbers if number>0]
        # print(random_number)
        # print(interval_numbers)
        # print('{} {} = {} {}'.format(amount, from_currency,random_number, to_currency))
        if random_number in interval_numbers:
            return True
        else:
            return False

    def get_guess_from_user(self, random_number):
        """
        here we take a guess from user and enter to amount of USD
        """
        user_guess = int(input("how mouch is " + str(random_number) + " USD in ILS?\n"))
        try:
            get_guess_from_user = int(user_guess)
        except ValueError:
            print("please enter an integer")
            breakpoint()
        if get_guess_from_user < 1:
            print("not a valid number, please enter a number bigger than 0")
            raise breakpoint()
        self.set_user_guess = user_guess
        return self.set_user_guess

    def play_currency_game(self, difficulty):
        """
        here we start the game, take the url and return True of False
        """
        x = currency_roulette_game_class(get_url=None,get_guess_from_user=None)
        random_number = random.randint(1, 100)
        url = x.get_url()
        user_guess = x.get_guess_from_user(random_number)
        converter = x.get_money_interval(difficulty, random_number, url, user_guess)
        if converter == True:
            print("you win!!!")
            return True
        else:
            print("you lose!!!")
            return False




