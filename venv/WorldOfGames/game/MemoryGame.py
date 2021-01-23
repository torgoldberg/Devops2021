import random
import time
import os


class memory_game_class:

    def __init__(self, generetedSequence=None, userList=None):
        self._generetedSequence = generetedSequence
        self._userList = userList

    @property
    def get_generated_sequence(self):
        """
        here we get the memeory game difficuty
        """
        return self._generetedSequence

    @property
    def get_user_list(self):
        """
        here we get the user list
        """
        return self._userList

    @get_generated_sequence.setter
    def set_generated_sequence(self):
        """
        here we set genereted sequesnce
        """
        self._generetedSequence

    @get_user_list.setter
    def set_user_ist(self):
        """
        here we set the user list
        """
        self._userList

    def generated_sequence(self, difficulty):
        """
        here we generate a list of random numbers
        """
        randomList = []
        for i in range(0, difficulty):
            n = random.randint(1, 101)
            randomList.append(n)
        self._generetedSequence = randomList
        print(randomList, end="\r")
        print(f"{randomList}", end="\t")
        time.sleep(3)
        print("", end="\r")
        print("TIMES UP!!!!!!!!!!!!")
        return self._generetedSequence

    def get_list_from_user(self, difficulty):
        """
        here we prompt a list of numbers from the user
        """
        self._userList = []
        number = int(input("pleas select the size on the array you want to create: "))
        if len(str(number)) > len(str(difficulty)):
            print("the array you created is to big")
            breakpoint()
        if len(str(number)) <= 0:
            print("the array you created is to small")
            breakpoint()
        else:
            for i in range(0, number):
                print("please enter a number from 1 to 101: ")
                element = int(input())
                if element < 1:
                    print("please enter a valid number, bigger then 1")
                    breakpoint()
                elif element > 101:
                    print("please enter a vaild number, smaler then 101")
                    breakpoint()
                else:
                    self._userList.append(element)
            print(self._userList)
        return self._userList

    def is_list_equel(self, generated_sequence, get_list_from_user):
        """
        here we check if the generated sequence list is equel to the user list
        """
        print("\n")
        print(generated_sequence)
        print(get_list_from_user)
        if generated_sequence != get_list_from_user:
            print("wrong, this is not the macthing umbers")
            return False
        else:
            print("success, you selected the correct numbers")
            return True

    def play_memory_game(self, difficulty):
        """
        here we start the memory game and return True or False
        """
        x = memory_game_class(generetedSequence=None, userList=None)
        generated_sequence = x.generated_sequence(difficulty)
        get_list_from_user = x.get_list_from_user(difficulty)
        compare_resut = x.is_list_equel(generated_sequence, get_list_from_user)
        if compare_resut == True:
            print("you win!!!")
            check = True
        else:
            print("you lose!!!")
            check = False
        return check
