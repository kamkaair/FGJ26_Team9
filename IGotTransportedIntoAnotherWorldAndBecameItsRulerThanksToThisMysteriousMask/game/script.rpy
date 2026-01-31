# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image testImage = "images/truckLogo.png" # Load images like this, used inside the scene 1

define health = 100
# The game starts here.
label takeDamage:
    python:
        if(health <= 0):
            message = "You're already dead, stop."
        else:
            newHealth = health - 25
            health = newHealth
            message = "Took damage. Remaining: " + str(newHealth) 
    "[message]"
    

label start:

    show susan
    sg "Hello"

    mc "Moi"

    show susan shy
    sg "You are so handsome"

    show tessa at left
    cg "Meowwww!"
    show susan at center
    pg "Hello" 
    show susan at right
    lg "I am the light"

    bm "I am boos man!"
    # Test scenes
    menu:
        "Which scene do you want to play?"
        "All of them:":
            call test_scene1
            call test_scene2
        "Conversation, sprite rendering, movement, backgrounds, transitions:":
            jump test_scene1
        "Input name and Menu:":
            jump test_scene2
        "Take damage:":
            "Aiiii"
            call takeDamage
        "None of them":
            jump continue   

    #define pov = Character("[povname]")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # Default stuff
    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label continue:
    return