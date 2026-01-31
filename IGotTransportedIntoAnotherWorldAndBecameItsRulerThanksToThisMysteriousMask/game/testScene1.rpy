label test_scene2:
    scene bg plant
    with dissolve
    
    define pov = Character("[povname]")

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Empty Name"

    pov "My name is [povname]!"

    menu:
        "Whats up"
        "ch1":
            "Great choice, [povname]."
            jump ch1
        
        "ch1 alt":
            "Mediocre choice, [povname]"
            jump ch1

        "ch2":
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