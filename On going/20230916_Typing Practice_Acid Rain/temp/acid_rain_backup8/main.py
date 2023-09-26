from game import GameManager
from ui import UserInterface


# ----------------------------------------- Objective ------------------------------------- #
# [O] Get words from 'words.txt' and make different levels of word lists.
# [O] Make GUI.
# [X] - Change the icon.
# [O] Make words move downwards. Make them disappear when they hit the ground.
# [O] Calculate score and change stage.
# [X] Keep the highest score, stage and the username.
# [X] Change the profile image to its pH level.
# [X] Add some event with blue text.
# [X] - (Advantage) Disappear all the texts on the screen.
# [X] - (Disadvantage) Hide all the texts on the screen.
# [X] - (Advantage) Make the movement of the words slower.
# [X] - (Disadvantage) Make the movement of the words faster.


game = GameManager()
game.get_words_from_the_file()
ui = UserInterface(game)
