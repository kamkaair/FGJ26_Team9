label test_scene1:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cool

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show cool
    e "Hey, I'm Cool~"
    #show logo base at right
    show cool happy
    e "I am so happy I could crhy right now waa"

    # image cool happy = "images/cool happy.png"
    show cool angry
    e "This is really PISSING me off"

    show cool angry at right
    e "I'm so very PISSED OFF"

    show cool angry at left
    e "I'm so very PISSED OFF"
    # These display lines of dialogue.

    e "Look at this fella"
    show testImage at right
    e "Who the HECK do they think they are"

    hide testImage
    e "gET OUT"
    #show cool angry as cool left
    #e "I'm so very PISSED OFF"

    e "Look at this transition"
    show bg forest
    with dissolve
    e "again"
    show bg cool
    with dissolve

    hide cool angry
    e "Imma head out"
    return