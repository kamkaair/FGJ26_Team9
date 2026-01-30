label test_scene2:
    scene bg plant
    with dissolve

    menu:
        #jump ch1

        #jump ch2

        "Whats up"
        "Option 1":
            "Great choice."
            jump ch1

        "Option 2":
            "BAD choice, feller"
            jump ch1
        
        "Option 3":
            "Mediocre choice"
            jump ch1

        "Option 4":
            jump ch2  

    label ch1:
        #$ menu_flag = True
        e "ja niin seuraavana aamuna..."

        jump cont

    label ch2:
        #$ menu_flag = False
        e "a CRAZY secret"

        jump cont

    label cont:
        "We continue..."

    return