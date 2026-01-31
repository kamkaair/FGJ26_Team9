define coolChar = Character(
    "CoolGuy", color="ffcccc", what_size=28)

image coolCharacter = "images/cool.png"

# Layering technique 1
image character = Composite(
(536, 810),
(0, 0), "images/cool.png",
(0, 0), "images/[current_hat] hat.png"
)

# Layering technique 2
layeredimage characterLayer:
    always: 
        "coolCharacter"
    group hat:
        attribute long_Hat default:
            "images/long hat.png"

        attribute round_Hat:
            "images/round hat.png"

label layer_test:
    $hat_type = ["round", "long", "nohat"]
    $current_hat = hat_type[0]

    # Uses Composite() for grouping sprites for characters
    show character at left
    e "First hat"

    $current_hat = hat_type[1]
    e "Second"

    # Uses layers for for grouping sprites
    show characterLayer long_Hat at right
    e "Layer: long hat"

    show characterLayer round_Hat at right
    e "Layer: round hat"

    return