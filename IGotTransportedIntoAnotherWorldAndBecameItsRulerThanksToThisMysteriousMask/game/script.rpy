# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Layering technique 2
layeredimage MainCharacter:
    always "images/cool.png"

    group hat:
        attribute round_hat "images/round hat.png"
        attribute long_hat "images/long hat.png"
        attribute empty_hat "images/empty hat.png"

define e = Character("Eileen")

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

    jump start # looks kinda scary to call main again, but works without problems(?)
    
label setName:

    menu:
        "Would you like to change your name? (Protagonist-kun)"
        "Yes":
            python:
                povname = renpy.input("Please enter your name: ", length=32)
                povname = povname.strip()

                if povname:
                    mc = Character(name=povname, who_color=CharactersInfo[0][2])
                    mc_color = "{color=#dda732}" + povname + "{/color}"
                    
                else:
                    mc = Character(name=CharactersInfo[0][0], who_color=CharactersInfo[0][2])
            
        "No":
            $ mc = Character(name=CharactersInfo[0][0], who_color=CharactersInfo[0][2])
    
    
    return # remember to return, otherwise we are in loop

#layeredimage coolguy:
    #attribute 

label start:
    call setName
    jump a0e1

label continue:
    return