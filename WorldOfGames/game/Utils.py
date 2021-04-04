import os

SCORE_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 0


class utils_class:

    def __init__(self, txtFile = None, badCode = None):
        self._txtFile = txtFile
        self._badCode = badCode

    @property
    def get_txt_file(self):
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

    @get_txt_file.setter
    def set_txt_file(self, x):
        """
        here we set the file name
        """
        txt_file = x
        self._txtFile = txt_file

    @get_bad_code.setter
    def set_bad_code(self, x):
        """
        here we set the bad error
        """
        bad_error = x
        self._badCode = bad_error

    def start_utils(self):
        """
        here we start the game utils
        """
        self.set_bad_code = BAD_RETURN_CODE
        self.set_txt_file = SCORE_FILE_NAME
        return self.set_txt_file, self.set_bad_code

    def screen_cleaner(self):
        clear = lambda: os.system('cls')
        clear()

