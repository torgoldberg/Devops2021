from Utils import utils_class
from MainScores import main_scores_class
import os.path
from pathlib import Path
from os import path

POINTS_OF_WINNING = 0

class score_class:

    def __init__(self, Score = POINTS_OF_WINNING):
        self._Score = Score

    @property
    def get_user_score(self):
        """
        here we get the user acore
        """
        return self._Score

    @get_user_score.setter
    def set_user_score(self, x):
        """
        here we set the user score
        """
        user_score = x
        self._Score = user_score


    def add_score(self, difficulty):
        x = score_class(Score=None)
        POINTS_OF_WINNING = (difficulty * 3) + 5
        test = utils_class()
        if path.exists ("Scores.txt"):
            file_txt = "Scores.txt"
            print(file_txt)
            test = main_scores_class()
            test.score_server(file_txt)
            file = open(file_txt, "w")
            number = []
            for line in file:
                splitLines = line.split(",")
                number.append(splitLines[0])
            print(number)
            file.close()
        else:
            print("file doesn't exist creating it")
            file = open("Scores.txt", "w")
            file.write('%d' % POINTS_OF_WINNING)
            print(file)
            file.close()

