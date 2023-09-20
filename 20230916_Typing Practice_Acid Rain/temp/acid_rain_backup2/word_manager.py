from turtle import RawTurtle


class Word(RawTurtle):

    def __init__(self):
        super().__init__()
        self.word = ""


class WordManager:

    def __init__(self):
        self.word_lists = self.get_word_list_from_text_file()

    def get_word_list_from_text_file(self):
        with open("./data/words.txt") as file:
            contents = file.readlines()

        stripped_word_list = [word.strip() for word in contents]
        return stripped_word_list
