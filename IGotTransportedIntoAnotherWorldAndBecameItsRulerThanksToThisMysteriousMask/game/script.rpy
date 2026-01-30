# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image testImage = "images/truckLogo.png" # Load images like this



# The game starts here.

label start:

    # Test scenes
    menu:
        "Which scene do you want to play?"
        "All of them:":
            call test_scene1
            call test_scene2
        "Test scene 1:":
            jump test_scene1
        "Test scene 2:":
            jump test_scene2

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # Default stuff
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
