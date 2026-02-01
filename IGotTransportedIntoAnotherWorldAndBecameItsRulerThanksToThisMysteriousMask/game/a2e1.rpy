label a2e1:
    image bg black = "#000000"
    image textTavern = Transform(Text("At the tavern:", size=60), yalign=0.5)

    show bg black
    show textTavern
    "Click to continue..."

    scene bg bar # PLACEHOLDER
    with dissolve

    #show MainCharacter empty_hat at center
    show protagonist mask happy at center

    #show ayla neutral at left:

    "Our beloved [mc_color] wakes up the next day when the sun is already high in the sky, feeling refreshed"

    show protagonist mask at center

    mc "Ahh, that was some of the best sleep I’ve ever had "
    "I wonder how the girls are doing..."

    hide protagonist mask

    "[mc_color] makes their way to the main area of the tavern, where [pg_color] and [sg_color] are enjoying lunch"
    show susan at right
    show ayla neutral at left

    sg "...and then they punched me! And I got turned into a girl!"

    pg "So, that’s how they cured you from that awful curse."

    show ayla happy at left
    pg "“It’s great that you ran into a great hero, such as the Masked One"

    show ayla surprised at left
    sg "Ah, no. I-I was never cursed…"

    show protagonist mask happy at center
    mc "Gooood morning girls!"

    show ayla happy at left
    pg "Ara ara. You finally woke up!"

    show ayla neutral at left
    pg "I was worried that someone had assassinated you in your sleep or something…"


    menu:
        "Assassinated...?":
            show protagonist mask surprised at center
            mc "Assassinated..?"
            show ayla surprised at left
            pg "Oh, yes! You’re not from around here."
            show ayla neutral at left
            pg "Assassinations of stronger people are pretty common. It’s an easy way to weed out the competition for Town Mayor’s Selection."

            mc "Oh…"
            pass
        "Ignore comment":
            pass

    show ayla neutral at left
    pg "In any case, there were some reports of a monster made of lightning wreaking havoc in a nearby forest."


    pg "Sounds like a job for you."

    "[mc_color]’s stomach rumbles loudly."

    show protagonist mask at center
    mc "I’ll go after I’ve eaten breakfast..?"

    show ayla angry at left
    pg "Nonsense! You must go straight away!"

    pg "Otherwise the monster might kill someone."

    show protagonist mask sad at center
    mc "But I’m hungry…"

    pg "NOW!"

    "Narrator: [mc_color] escapes from the tavern, and runs straight out of the town."

    "[mc_color] escapes from the tavern, and runs straight out of the town."

    scene bg black # PLACEHOLDER
    with dissolve

    jump a2e2
    