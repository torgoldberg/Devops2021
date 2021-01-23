import os

SCORE_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 0

class utils_class:

    def __init__(self, txtFile = SCORE_FILE_NAME, badCode = BAD_RETURN_CODE):
        self._txtFile = txtFile
        self._badCode = badCode

    @property
    def get_txtFile(self):
        """
        here we get the txtFile
        """
        return self._txtFile

    @property
    def get_bad_code(self):
        """
        here we get the bad return code error
        """
        return self._badCode

    def screen_cleaner(self):
        clear = lambda: os.system('cls')
        clear()

