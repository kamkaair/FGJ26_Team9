define coolChar = Character(
    "CoolGuy", color="ffcccc", what_size=28)

# Layering technique 2
layeredimage MainCharacter:
    always "images/cool.png"

    group hat:
        attribute round_hat "images/round hat.png"
        attribute long_hat "images/long hat.png"
        attribute empty_hat "images/empty hat.png"

#python:
    #from enum import Enum
    #class Hats(Enum):
        #NO_HAT = 0
        #ROUND_HAT = 1
        #LONG_HAT = 2

# Layering technique 1
image character = Composite(
(536, 810),
(0, 0), "images/cool.png",
(0, 0), "images/[current_hat] hat.png"
)

label layer_test:
    $hat_type = ["empty", "round", "long"]
    $current_hat = hat_type[0]

    # Uses Composite() for grouping sprites for characters
    show character at left
    e "No hat"

    $current_hat = hat_type[1]
    e "First"

    $current_hat = hat_type[2]
    e "Second"

    # Uses layers for for grouping sprites
    show MainCharacter long_hat at right
    e "Layer: long hat"

    show MainCharacter round_hat at right
    e "Layer: round hat"

    show MainCharacter empty_hat at right
    e "Layer: no hat"

    return