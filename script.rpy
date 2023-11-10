# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define n = Character("Nejiko")
define ne= Character ("Negogo")

# The game starts here.

label start:
    stop music

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene rooom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nejiko_2

    # These display lines of dialogue.

    n "AAAAAH I JUST WOKE UP!ù finally  i got my 11hours of schleep."
    n "wha time is ti?"
    n" 14pm."

    show nejiko_1

    n "TIME TO GET BITCHES"
    hide nejiko_1

    show nejiko_3

    n " BUTR WHERE IZ PEPI ?????"

    n "I hab to find him"

    scene knechtor

    n " I am googling on my computer."
    n " omg pepi is kidnapped!!!! twitter says so"
    n " I have to go to monster girls university."

    scene cool

    "you are walking in the street."
    "but you hear a noise."
    "someone crying"
    "what do you do?"
    menu:

        "you check":
            "you hear the noise cry bigger."
            show negogo2
            ne "miaou miaou miaouuuuu"
            "it's a cat girl abandoned"
            "she looks malnourished"
            hide negogo2

            show negogo3
            play sound "audio/miaou.ogg"

            ne " MIAOUUUU euuurhhhgggg"
            ne " oh no i pukeed man not cool"
            n" have you seen a lil fox yellow fox pls"
            ne" yes but i wont tell you."
            n" what can i do ??"
            ne" you have to adopt me as your cat"
            n"ok"

        "no we must stay focus lets find pepi":
            "This is the result of the user choosing the second choice."

        "take off your pants lay flat down on the ground and hope nothing bad happens":
            "police girl show up and look at you with disgust."
            show police
            "you arearested"

    # This ends the game.

    return
