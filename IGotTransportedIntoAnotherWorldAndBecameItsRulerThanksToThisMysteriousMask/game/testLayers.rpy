define coolChar = Character(
    "CoolGuy", color="ffcccc", what_size=28)

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