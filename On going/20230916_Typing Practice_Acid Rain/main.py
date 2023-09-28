from game import GameManager
from ui import UserInterface


# ----------------------------------------- Objective ------------------------------------- #
# [O] Get words from 'words.txt' and make different levels of word lists.
# [O] Make GUI.
# [X] - Change the icon.
# [O] Make words move downwards. Make them disappear when they hit the ground.
# [O] Calculate score and change stage.
# [X] Keep record of score, stage and username.
# [X] Change the profile image to its pH level.
# [O] Add special effect for blue-text.
# [O] - (Advantage) remove all rain.
# [O] - (Advantage) Stop rain moving.
# [O] - (Advantage) Move rain slower.
# [O] - (Disadvantage) Move rain faster.
# [O] - (Disadvantage) Hide all rain text.


game = GameManager()
game.get_words_from_the_file()
# ui = UserInterface(game)

game.update_record()
game.get_record()