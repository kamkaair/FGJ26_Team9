label a2e3:
    transform protagonistPos:
        xalign 0.33
        yalign 1.0
    transform evelynPos:
        xalign 0.66
        yalign 1.0
    transform aylaPos:
        xalign 0.99
        yalign 1.0
    transform susanPos:
        xalign 0.0
        yalign 1.0

    scene bg black
    show textTavern
    "Click to continue..."

    scene bg bar
    with dissolve

    "[sg_color] and [pg_color] are chatting, when [mc_color] and [lg_color] join up with them."

    show protagonist mask neutral at protagonistPos
    mc "I'm back!"

    mc "And I brought us a new friend. This is Eve-tan!"

    show evelyn happy at evelynPos
    lg "Hii! I'm [lg_color] Morningglory!"

    show ayla neutral at aylaPos
    pg "Hello [lg_color]. My name is [pg_color], and this is [sg_color]."

    show susan neutral at susanPos
    sg "Hi..."

    show protagonist mask neutral
    mc "Anyways, I'm finally gonna go and get something to eat."

    mc "You girls can get to know each other in the meantime."

    menu:
        "Go order dinner":
            pass


    scene bg black
    with fade
   
    jump a2e4
    