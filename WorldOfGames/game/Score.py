from os import path

POINTS_OF_WINNING = 0


class score_class:

    def __init__(self, score=POINTS_OF_WINNING):
        self._score = score

    @property
    def get_user_score(self):
        """
        here we get the user acore
        """
        return self._score

    @get_user_score.setter
    def set_user_score(self, x):
        """
        here we set the user score
        """
        user_score = x
        self._score = user_score

    def add_score(self, difficulty, txt_file):
        POINTS_OF_WINNING = (difficulty * 3) + 5
        if path.exists(txt_file):
            with open(txt_file) as my_file:  # this function will check if the existing file is empty
                my_file.seek(0)
                first_char = my_file.read(1)
                if not first_char:
                    print("file is empty")
                    empty = True
                else:
                    print("file is not empty")
                    my_file.seek(0)
                    empty = False
            if empty == True:
                my_file = open(txt_file, "w")
                my_file.write('%d' % POINTS_OF_WINNING)
                self.set_user_score = POINTS_OF_WINNING
                return self._score
            else:
                my_file = open(txt_file, "r+")
                lines = my_file.readlines()
                del lines[0]
                my_file.close()
                my_file.seek(0)
                num = my_file.read(1)
                total = int(num) + POINTS_OF_WINNING
                my_file
                my_file.write('%d' % total)
                self.set_user_score = total
                return self._score
        else:
            print("file doesn't exist creating it")
            my_file = open(txt_file, "w")
            my_file.write('%d' % POINTS_OF_WINNING)
            self.set_user_score = POINTS_OF_WINNING
            return self._score
